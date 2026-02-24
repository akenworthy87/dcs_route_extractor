import annotationlib
from modules.build_waypoint_coords import build_waypoint_coords, WaypointCoords
from modules.process_terrain_spec import TerrainSpec
from modules.load_route_data import Waypoint




class Test_Build_Waypoint_Coords:
    
    # Mock terrain spec and waypoint data for testing
    terrain_spec = TerrainSpec(
        origin_mgrs="34W EA 62702 43625",
        central_meridian=21,
        scale_factor=0.9996
    )
    
    waypoint: Waypoint = {
        "speed_locked": False,
        "type": "Turning Point",
        "action": "Turning Point",
        "ETA_locked": True,
        "y": 332102.0625,
        "x": 202541.640625,
        "name": "TEST WAYPOINT",
        "ETA": 900,
        "alt_type": "RADIO",
        "alt": 1000
    }

    result = build_waypoint_coords(waypoint, terrain_spec)

    def test_check_result_keys(self):
        assert self.result.keys() == annotationlib.get_annotations(WaypointCoords).keys()

    def test_check_result_instances(self):
        result = self.result

        assert isinstance(result['name'], str)
        assert isinstance(result['altitude'], float)
        assert isinstance(result['altitude_type'], str)
        assert isinstance(result['north_offset'], float)
        assert isinstance(result['east_offset'], float)
        assert isinstance(result['latitude'], float)
        assert isinstance(result['longitude'], float)
        assert isinstance(result['lat_prcise'], str)
        assert isinstance(result['lon_prcise'], str)
        assert isinstance(result['lat_dm'], str)
        assert isinstance(result['lon_dm'], str)
        assert isinstance(result['mgrs_compact'], str)
        assert isinstance(result['mgrs_pretty'], str)

    def test_result_name(self):
        assert self.result['name'] == "TEST WAYPOINT"
        
    def test_result_altitude(self):
        assert self.result['altitude'] == 1000.0
        assert self.result['altitude_type'] == "RADIO"
        
    def test_result_offsets(self):
        assert self.result['north_offset'] == 202541.640625
        assert self.result['east_offset'] == 332102.0625
        
    def test_result_latlon(self):
        assert self.result['latitude'] == 69.52839064396765
        assert self.result['longitude'] == 31.15499773059966

    def test_result_latlon_precise(self):
        assert self.result['lat_prcise'] == "69°31'42.20"
        assert self.result['lon_prcise'] == "31°9'17.99"

    def test_result_latlon_dm(self):
        assert self.result['lat_dm'] == "69°31.703"
        assert self.result['lon_dm'] == "31°9.299"
        
    def test_result_mgrs(self):
        assert self.result['mgrs_compact'] == "36WVC2799414368"
        assert self.result['mgrs_pretty'] == "36W VC 27994 14368"
