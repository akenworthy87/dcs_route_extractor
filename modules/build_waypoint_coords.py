from modules.convert_offset_to_coords import convert_offset_to_coords
from modules.format_latlongs import latlon_to_decimal_minutes, latlon_to_dms
from modules.load_route_data import Waypoint
from modules.process_terrain_spec import TerrainSpec

from typing import TypedDict


def build_waypoint_coords(waypoint: Waypoint, terrain_spec: TerrainSpec) -> WaypointCoords:
    """
    Takes a waypoint and builds a waypoint coord object containing the exported coordinate data

    Arguments:
        waypoint {dict} -- Waypoint dict from route data

    Returns:
        WaypointCoords -- Extracted coordinates from waypoint
    """

    name = waypoint['name'].upper()
    
    alt = float(waypoint['alt'])
    alt_type = waypoint['alt_type']
    
    north_offset = waypoint['x']
    east_offset = waypoint['y']
    
    lat_new, lon_new, mgrs_result, pretty_mgrs = convert_offset_to_coords(
        terrain_spec, north_offset, east_offset)

    lat_dms, lon_dms = latlon_to_dms(lat_new, lon_new)
    lat_dm, lon_dm = latlon_to_decimal_minutes(lat_new, lon_new)

    waypoint_coords: WaypointCoords = {
        'name': name,
        'altitude': alt,
        'altitude_type': alt_type,
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


class WaypointCoords(TypedDict):
    name: str
    altitude: float
    altitude_type: str
    north_offset: float
    east_offset: float
    latitude: float
    longitude: float
    lat_prcise: str
    lon_prcise: str
    lat_dm: str
    lon_dm: str
    mgrs_compact: str
    mgrs_pretty: str
