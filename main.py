import sys
from modules.load_route_data import load_route_data
from modules.process_waypoints import process_waypoints
from modules.export_to_csv import export_to_csv


def main(argv: list[str] | None = None):
    if argv is None:
        argv = sys.argv

    filepath = r'Kola.lua'
    routename = 'Radars2'
    
    # Load DCS route data 
    route_data = load_route_data(filepath)
    
    # Process waypoints in route
    waypoints = process_waypoints(route_data, routename)
    
    # Export waypoints to CSV
    export_to_csv(waypoints)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
