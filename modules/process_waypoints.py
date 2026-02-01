from modules.build_waypoint_coords import build_waypoint_coords


def process_waypoints(route_data, route_name):
    waypoints = []
    for i, radar in enumerate(route_data[route_name]):

        info = build_waypoint_coords(radar)

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
