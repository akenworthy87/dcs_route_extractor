from dataclasses import dataclass
from typing import Optional
from mgrs import MGRS
from pyproj import Transformer, CRS


@dataclass()
class TerrainSpec:
    origin_mgrs: str
    central_meridian: int
    scale_factor: float
    
    # Calculated fields
    origin_mgrs_compact: Optional[str] = None
    lat_origin: Optional[float] = None
    lon_origin: Optional[float] = None
    terrain_proj: Optional[CRS] = None
    to_terrain_proj: Optional[Transformer] = None
    from_terrain_proj: Optional[Transformer] = None


    def make_transformers(self):
        # Conversion method from https://github.com/pydcs/dcs/blob/master/dcs/terrain/projections/transversemercator.py
        self.terrain_proj = CRS.from_proj4(
            " ".join(
                [
                    "+proj=tmerc",
                    "+lat_0=0",
                    f"+lon_0={self.central_meridian}",
                    f"+k_0={self.scale_factor}",
                    f"+x_0={self.lon_origin}",
                    f"+y_0={self.lat_origin}",
                    "+towgs84=0,0,0,0,0,0,0",
                    "+units=m",
                    "+vunits=m",
                    "+ellps=WGS84",
                    "+no_defs",
                    "+axis=neu",
                ]
            ))

        self.to_terrain_proj = Transformer.from_crs(
            CRS("WGS84"), self.terrain_proj, always_xy=True)   # input is lon,lat
        self.from_terrain_proj = Transformer.from_crs(self.terrain_proj, CRS(
            "WGS84"), always_xy=True)  # output is lon,lat


    def mgrs_to_latlon(self):
        """convert MGRS -> lat, lon"""
        m = MGRS()
        # mgrs.toLatLon sometimes returns (lat, lon)
        lat_lon = m.toLatLon(self.origin_mgrs_compact)
        if isinstance(lat_lon, (bytes, bytearray)):
            # unlikely, but decode if needed
            lat_lon = lat_lon.decode()
        # ensure we have floats (some mgrs versions return tuple)
        if isinstance(lat_lon, tuple) and len(lat_lon) == 2:
            self.lat_origin, self.lon_origin = float(
                lat_lon[0]), float(lat_lon[1])
        else:
            raise RuntimeError("Unexpected return from mgrs.toLatLon")

    def __post_init__(self):
        # Validate MGRS format
        self.origin_mgrs_compact = self.origin_mgrs.replace(" ", "")
        self.mgrs_to_latlon()
        self.make_transformers()
        
        
def process_terrain_spec(terrain_spec_data: dict) -> TerrainSpec:
    """
    Takes a terrain spec data dict and processes it into a TerrainSpec object.

    Arguments:
        terrain_spec_data {dict} -- terrain spec data dict
    Returns:
        TerrainSpec -- processed terrain spec object
    """
    terrain_spec = TerrainSpec(
        origin_mgrs=terrain_spec_data['origin_mgrs'],
        central_meridian=terrain_spec_data['central_meridian'],
        scale_factor=terrain_spec_data['scale_factor']
    )
    return terrain_spec