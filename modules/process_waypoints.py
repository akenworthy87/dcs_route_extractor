from modules.build_waypoint_coords import build_waypoint_coords
from modules.process_terrain_spec import TerrainSpec


def process_waypoints(route_data: dict, route_name: str, terrain_spec: TerrainSpec) -> list[tuple]:
    """
    Takes a route data dict and processes the waypoints in the selected route name.

    Arguments:
        route_data {dict} -- route data dict
        route_name {str} -- route name

    Returns:
        list -- list of processed waypoint data
    """    
    waypoints: list[tuple] = []
    for i, waypoint in enumerate(route_data[route_name]):

        info = build_waypoint_coords(waypoint, terrain_spec)

        waypoints.append((
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

    return waypoints
