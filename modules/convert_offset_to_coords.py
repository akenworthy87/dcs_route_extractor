from mgrs import MGRS
from pyproj import Transformer, CRS
from modules.process_terrain_spec import TerrainSpec


# TODO: #4 Would be good to refactor this by splitting into seperate functions
#   * MGRS conversion and creating the projection transformers only need to run once
#   * This is doing the above every waypoint instead just once per run
#   ? Maybe convert to a class method?
def convert_offset_to_coords(terrain_spec: TerrainSpec, north_offset: float, east_offset: float):
    """
    Convert MGRS coordinates with applied north and east offsets to new coordinates.
    This function takes an origin point in MGRS format and applies north/east offsets
    (in meters) to calculate a new geographic location. It uses a Transverse Mercator
    projection centered at the origin to accurately apply the offsets.
    Args:
        terrain_spec (TerrainSpec): TerrainSpec object containing the origin MGRS 
                and latitude/longitude of the origin, as well as projection methods.
        north_offset (float): Distance in meters to offset northward (positive values
                             move north, negative values move south).
        east_offset (float): Distance in meters to offset eastward (positive values
                            move east, negative values move west).
    Returns:
        tuple: A tuple containing four elements:
            - lat_new (float): Latitude of the new location in decimal degrees.
            - lon_new (float): Longitude of the new location in decimal degrees.
            - mgrs_result (str): New location in compact MGRS format (no spaces).
            - pretty_mgrs (str): New location in formatted MGRS format with spaces
                                (e.g., "34W EA 62702 43625").
    Raises:
        RuntimeError: If the MGRS to lat/lon conversion returns an unexpected format.
    Note:
        Uses a Transverse Mercator projection (tmerc) with WGS84 datum for accurate
        offset application. The projection is configured with specific parameters
        matching DCS terrain projection conventions.
    """
    lat_origin = terrain_spec.lat_origin
    lon_origin = terrain_spec.lon_origin
    
    to_terrain_proj:Transformer = terrain_spec.to_terrain_proj # type: ignore
    from_terrain_proj:Transformer = terrain_spec.from_terrain_proj # type: ignore


    # origin in AEQD coordinates (should be near 0,0)
    x0, y0 = to_terrain_proj.transform(lon_origin, lat_origin)

    # add offsets (east -> +x, north -> +y)
    x_new = x0 + (east_offset)
    y_new = y0 + (north_offset)

    # transform back to geographic coordinates
    lon_new, lat_new = from_terrain_proj.transform(x_new, y_new)

    # convert result back to MGRS. Use precision 5 to match 1-meter digits (same as input).
    # mgrs.toMGRS(lat, lon, precision) may return bytes on some installs, handle that.
    mgrs_result = MGRS().toMGRS(lat_new, lon_new, MGRSPrecision=5)
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

    return lat_new, lon_new, mgrs_result, pretty_mgrs
