from modules.convert_offset_to_coords import convert_offset_to_coords
from modules.format_latlongs import latlon_to_decimal_minutes, latlon_to_dms

from modules.process_terrain_spec import TerrainSpec



def build_waypoint_coords(waypoint, terrain_spec: TerrainSpec) -> dict:
    """
    Takes a waypoint and builds a waypoint coord object containing the exported coordinate data

    Arguments:
        waypoint {dict} -- Waypoint dict from route data

    Returns:
        dict -- Extracted coordinates from waypoint
    """    
    waypoint_coords = {}

    name = waypoint['name'].upper()
    north_offset = waypoint['x']
    east_offset = waypoint['y']
    lat_new, lon_new, mgrs_result, pretty_mgrs = convert_offset_to_coords(terrain_spec, north_offset, east_offset)

    lat_dms, lon_dms = latlon_to_dms(lat_new, lon_new)
    lat_dm, lon_dm = latlon_to_decimal_minutes(lat_new, lon_new)

    waypoint_coords = {
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
    return waypoint_coords
