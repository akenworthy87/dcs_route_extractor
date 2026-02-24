from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
import sys
from modules.load_route_data import load_routes_data
from modules.process_waypoints import process_waypoints
from modules.export_to_csv import export_to_csv
from modules.process_argv import process_argv
from modules.open_file_dialog import open_file_dialog
from modules.select_routename import select_routename
from modules.load_terrain_specs import load_terrain_specs
from modules.process_terrain_spec import process_terrain_spec, TerrainSpec
from pathlib import Path
from modules.load_route_data import Waypoint
from modules.build_waypoint_coords import build_waypoint_coords


    
@given('Map is {map_name}') # pyright: ignore[reportCallIssue]
def step_given_map_name(context, map_name:str):
    context.map_name = map_name.title()
    # Load terrain specs
    try:
        context.terrain_specs_init = load_terrain_specs(Path(context.map_name), bypass_file_check=True)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        assert False, f"Failed to load terrain specs for map: {context.map_name}. Error: {e}"
    # Create TerrainSpec object
    context.terrain_spec = process_terrain_spec(context.terrain_specs_init)

@when('Metric: X{x} Z{z}') # pyright: ignore[reportCallIssue]
def step_when_metric(context, x, z):
    context.metric = {
        'x': float(x),
        'z': float(z)
    }
    waypoint: Waypoint = {
        "speed_locked": False,
        "type": "Turning Point",
        "action": "Turning Point",
        "ETA_locked": True,
        "y": context.metric['z'],
        "x": context.metric['x'],
        "name": "TEST WAYPOINT",
        "ETA": 900,
        "alt_type": "RADIO",
        "alt": 1000
    }
    context.waypoint = waypoint
    
    context.result = build_waypoint_coords(context.waypoint, context.terrain_spec)
    
    
@then(u'Lat Long Precise: {lat_prec}   {long_prec}') # pyright: ignore[reportCallIssue]
def step_lat_long_prec(context, lat_prec, long_prec):
    context.lat_long_prec = {
        'lat_prec': lat_prec,
        'long_prec': long_prec
    }
    assert context.result['lat_precise'] == context.lat_long_prec['lat_prec'], f"Expected Lat Precise: {context.lat_long_prec['lat_prec']}, but got: {context.result['lat_precise']}"
    assert context.result['lon_precise'] == context.lat_long_prec['long_prec'], f"Expected Long Precise: {context.lat_long_prec['long_prec']}, but got: {context.result['lon_precise']}"


@then(u'Lat Long Decimal Minutes: {lat_dm}   {long_dm}') # pyright: ignore[reportCallIssue]
def step_lat_long_dm(context, lat_dm, long_dm):
    context.lat_long_dm = {
        'lat_dm': lat_dm,
        'long_dm': long_dm
    }
    assert context.result['lat_dm'] == context.lat_long_dm['lat_dm'], f"Expected Lat DM: {context.lat_long_dm['lat_dm']}, but got: {context.result['lat_dm']}"
    assert context.result['lon_dm'] == context.lat_long_dm['long_dm'], f"Expected Long DM: {context.lat_long_dm['long_dm']}, but got: {context.result['lon_dm']}"


@then(u'MGRS GRID: {mgrs}') # pyright: ignore[reportCallIssue]
def step_mgrs(context, mgrs):
    context.mgrs = mgrs
    assert context.result['mgrs_pretty'] == context.mgrs, f"Expected MGRS: {context.mgrs}, but got: {context.result['mgrs_pretty']}"