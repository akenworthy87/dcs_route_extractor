import sys
from modules.load_route_data import load_routes_data
from modules.process_waypoints import process_waypoints
from modules.export_to_csv import export_to_csv
from modules.process_argv import process_argv
from modules.open_file_dialog import open_file_dialog
from modules.select_routename import select_routename
from modules.load_terrain_specs import load_terrain_specs
from modules.process_terrain_spec import process_terrain_spec, TerrainSpec


def main(argv: list[str] | None = None):
    if argv is None:
        argv = sys.argv


    # filepath = r'Kola.lua'
    # routename = 'Radars2'
    filepath, routename = process_argv(argv)
    
    # If no filepath provided, open file dialog
    if filepath is None:
        filepath = open_file_dialog()
    if filepath is None:
        # Assume the user has cancelled out, so exit gracefully
        sys.exit(0)
    
    # Load DCS route data 
    try:
        route_data = load_routes_data(filepath)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    
    # If no route name provided, select one
    if routename is None:
        try:
            routename = select_routename(route_data)
        except ValueError as e:
            print(e)
            sys.exit(1)
            
    
    try:
        # Load terrain specs
        terrain_specs_init = load_terrain_specs(filepath)
        # Create TerrainSpec object
        terrain_spec = process_terrain_spec(terrain_specs_init)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)
        
    # Process waypoints in route
    waypoints = process_waypoints(route_data, routename, terrain_spec)
    
    # Export waypoints to CSV
    export_to_csv(waypoints)


if __name__ == "__main__":
    sys.exit(main(sys.argv))


