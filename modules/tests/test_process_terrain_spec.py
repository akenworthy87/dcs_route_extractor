from modules.process_terrain_spec import process_terrain_spec, TerrainSpec
from pyproj import Transformer, CRS
from pytest import approx


class Test_Process_Terrain_Spec:
    kola_spec_data = {
        'origin_mgrs': "34W EA 62702 43625",
        'central_meridian': 21,
        'scale_factor': 0.9996
    }
    
    kola_terrain_spec = process_terrain_spec(kola_spec_data)
    
    
    def test_isinstance(self):
        assert isinstance(self.kola_terrain_spec, TerrainSpec)
        
    def test_set_attributes(self):
        assert self.kola_terrain_spec.origin_mgrs == "34W EA 62702 43625"
        assert self.kola_terrain_spec.central_meridian == 21
        assert self.kola_terrain_spec.scale_factor == 0.9996
        
    def test_mgrs_to_latlon(self):
        assert self.kola_terrain_spec.lat_origin == approx(68.00, 0.1)
        assert self.kola_terrain_spec.lon_origin == approx(22.50, 0.1)
        
    def test_make_transformers(self):
        assert isinstance(self.kola_terrain_spec.terrain_proj, CRS)
        assert isinstance(self.kola_terrain_spec.to_terrain_proj, Transformer)
        assert isinstance(self.kola_terrain_spec.from_terrain_proj, Transformer)