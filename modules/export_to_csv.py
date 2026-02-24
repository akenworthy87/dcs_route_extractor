import csv

def export_to_csv(waypoints: list):
    with open('waypoint_coords.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow([
            'Index',
            'name',
            'altitude',
            'altitude_type',
            'north_offset',
            'east_offset',
            'latitude',
            'longitude',
            'lat_precise',
            'lon_precise',
            'lat_dm',
            'lon_dm',
            'mgrs_compact',
            'mgrs_pretty'
        ])
        # Write waypoint data
        for waypoint in waypoints:
            writer.writerow(waypoint)
