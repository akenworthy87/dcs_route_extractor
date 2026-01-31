# %%
import luadata
from pprint import pp
from mgrs import MGRS
from pyproj import Transformer, CRS
import csv

# %%
ORIGIN_MGRS = "34W EA 62702 43625"

# %%
data = luadata.read(r'Kola.lua', encoding='utf-8')

# %%
pp(data['Radars2'])

# %%
# import sys
# import subprocess

# convert an MGRS string, add east/north offsets (meters) in the local planar grid,
# and return the resulting lat/lon and MGRS coordinate.
# (Requires mgrs and pyproj; this cell will install them if missing.)


# def _ensure(pkg):
#     try:
#         __import__(pkg)
#     except Exception:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# _ensure("mgrs")
# _ensure("pyproj")


# Input
def convert_offset_to_coords(origin_mgrs, north_offset, east_offset):
    # origin_mgrs = "34W EA 62702 43625"
    # north_offset = 202541  # meters to add (north)
    # east_offset = 332102   # meters to add (east)

    # normalize MGRS string (mgrs library accepts compact form)
    mgrs_str = origin_mgrs.replace(" ", "")

    m = MGRS()

    # convert MGRS -> lat, lon
    # mgrs.toLatLon sometimes returns (lat, lon)
    lat_lon = m.toLatLon(mgrs_str)
    if isinstance(lat_lon, (bytes, bytearray)):
        # unlikely, but decode if needed
        lat_lon = lat_lon.decode()

    # ensure we have floats (some mgrs versions return tuple)
    if isinstance(lat_lon, tuple) and len(lat_lon) == 2:
        lat_origin, lon_origin = float(lat_lon[0]), float(lat_lon[1])
    else:
        raise RuntimeError("Unexpected return from mgrs.toLatLon")

    # build an Azimuthal Equidistant projection centered on the origin.
    # In this projection, x ~ east (meters), y ~ north (meters).
    # aeqd_proj = CRS.from_proj4(f"+proj=tmerc +lat_0={lat_origin} +lon_0={lon_origin} +datum=WGS84 +units=m +no_defs +k_0=1")
    # aeqd_proj = CRS.from_proj4(f"+proj=tmerc +lat_0={lat_origin} +lon_0={lon_origin} +datum=WGS84 +units=m +no_defs +k_0=0.9996")
    # aeqd_proj = CRS.from_proj4(f"+proj=aeqd +lat_0={lat_origin} +lon_0={lon_origin} +datum=WGS84 +units=m +no_defs")
    
    
    # Conversion method from https://github.com/pydcs/dcs/blob/master/dcs/terrain/projections/transversemercator.py
    aeqd_proj = CRS.from_proj4(
            " ".join(
                [
                    "+proj=tmerc",
                    "+lat_0=0",
                    f"+lon_0=21",
                    f"+k_0=0.9996",
                    f"+x_0={lon_origin}",
                    f"+y_0={lat_origin}",
                    "+towgs84=0,0,0,0,0,0,0",
                    "+units=m",
                    "+vunits=m",
                    "+ellps=WGS84",
                    "+no_defs",
                    "+axis=neu",
                ]
            ))

    to_aeqd = Transformer.from_crs(CRS("WGS84"), aeqd_proj, always_xy=True)   # input is lon,lat
    from_aeqd = Transformer.from_crs(aeqd_proj, CRS("WGS84"), always_xy=True) # output is lon,lat

    # origin in AEQD coordinates (should be near 0,0)
    x0, y0 = to_aeqd.transform(lon_origin, lat_origin)

    # add offsets (east -> +x, north -> +y)
    x_new = x0 + (east_offset)
    y_new = y0 + (north_offset)
    # x_new = x0 + (east_offset * 0.9996)
    # y_new = y0 + (north_offset * 0.9996)

    # transform back to geographic coordinates
    lon_new, lat_new = from_aeqd.transform(x_new, y_new)

    # convert result back to MGRS. Use precision 5 to match 1-meter digits (same as input).
    # mgrs.toMGRS(lat, lon, precision) may return bytes on some installs, handle that.
    mgrs_result = m.toMGRS(lat_new, lon_new, MGRSPrecision=5)
    if isinstance(mgrs_result, (bytes, bytearray)):
        mgrs_result = mgrs_result.decode()

    # pretty-format MGRS (insert spaces similar to original: zone(3) + 2 letters + easting + northing)
    zone = mgrs_result[:3]
    letters = mgrs_result[3:5]
    digits = mgrs_result[5:]
    half = len(digits) // 2
    easting = digits[:half]
    northing = digits[half:]
    pretty_mgrs = f"{zone} {letters} {easting} {northing}"

    # print("Origin MGRS:", origin_mgrs)
    # print("Origin lat, lon:", lat_origin, lon_origin)
    # print("Offsets (north, east) m:", north_offset, east_offset)
    # print("New lat, lon:", lat_new, lon_new)
    # print("New MGRS (compact):", mgrs_result)
    # print("New MGRS (spaced):", pretty_mgrs)
    return lat_new, lon_new, mgrs_result, pretty_mgrs

# %%
convert_offset_to_coords('34W EA 62702 43625', 202541, 332102)

# %%
def trunc_round(num, precision=3):
    parts = (str(num).split('.'))
    if len(parts) < 2:
        return (str(num) + '.' + ('0' * precision)) # no decimal part
    
    integer = parts[0]
    decimal = parts[1][:precision]
    if len(decimal) < precision:
        decimal = decimal + ('0' * (precision - len(decimal)))
    return (integer + '.' + decimal)

# print(trunc_round(lat_dms[2], 6), trunc_round(lon_dms[2], 6))
# print(trunc_round(60, 6), trunc_round(60.0, 6))

# %%
def latlon_to_dms(lat, lon):
    '''Converts lat_new to DMS precise format (degrees, minutes, seconds)'''
    def to_dms(value):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        return degrees, minutes, seconds

    lat_deg, lat_min, lat_sec = to_dms(lat)
    lon_deg, lon_min, lon_sec = to_dms(lon)

    return (f"{lat_deg}°{lat_min}'{trunc_round(lat_sec, 2)}"), (f"{lon_deg}°{lon_min}'{trunc_round(lon_sec, 2)}")

lat_dms, lon_dms = latlon_to_dms(67.99999682172047, 22.499998619459987)
print("New lat DMS:", lat_dms)
print("New lon DMS:", lon_dms)

# %%
def latlon_to_decimal_minutes(lat, lon):
    '''Converts lat_new to Decimal Minutes format'''
    def to_decimal_minutes(value):
        degrees = int(value)
        minutes_full = abs((value - degrees) * 60)
        return degrees, minutes_full

    lat_deg, lat_min = to_decimal_minutes(lat)
    lon_deg, lon_min = to_decimal_minutes(lon)

    return (f'{lat_deg}°{trunc_round(lat_min,3)}'), (f'{lon_deg}°{trunc_round(lon_min,3)}')

lat_dm, lon_dm = latlon_to_decimal_minutes(67.99999682172047, 22.499998619459987)
print("New lat Decimal Minutes:", lat_dm)
print("New lon Decimal Minutes:", lon_dm)

# %%
def build_radar_coords(radar):
    radar_coords = {}
    
    name = radar['name'].upper()
    north_offset = radar['x']
    east_offset = radar['y']
    lat_new, lon_new, mgrs_result, pretty_mgrs = convert_offset_to_coords(ORIGIN_MGRS, north_offset, east_offset)
    
    lat_dms, lon_dms = latlon_to_dms(lat_new, lon_new)
    lat_dm, lon_dm = latlon_to_decimal_minutes(lat_new, lon_new)
    
    
    radar_coords = {
        'name': name,
        'north_offset': north_offset,
        'east_offset': east_offset,
        'latitude': lat_new,
        'longitude': lon_new,
        'lat_prcise': lat_dms,
        'lon_prcise': lon_dms,
        'lat_dm': lat_dm,
        'lon_dm': lon_dm,
        'mgrs_compact': mgrs_result,
        'mgrs_pretty': pretty_mgrs
    }
    return radar_coords

# %%
radars = []
for i, radar in enumerate(data['Radars2']):
    
    info = build_radar_coords(radar)
    
    radars.append((
        i+1,
        info['name'],
        info['north_offset'],
        info['east_offset'],
        info['latitude'],
        info['longitude'],
        info['lat_prcise'],
        info['lon_prcise'],
        info['lat_dm'],
        info['lon_dm'],
        info['mgrs_compact'],
        info['mgrs_pretty']
    ))

# %%
radars

# %%
# Export radars to CSV with headers
with open('radar_coords.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow([
        'Index',
        'name',
        'north_offset',
        'east_offset',
        'latitude',
        'longitude',
        'lat_prcise',
        'lon_prcise',
        'lat_dm',
        'lon_dm',
        'mgrs_compact',
        'mgrs_pretty'
    ])
    # Write radar data
    for radar in radars:
        writer.writerow(radar)


