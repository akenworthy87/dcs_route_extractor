from mgrs import MGRS
from pyproj import Transformer, CRS


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
