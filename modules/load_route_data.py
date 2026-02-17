from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pathlib import Path

from typing import TypedDict
import luadata


def load_routes_data(filepath: Path) -> RoutesData:
    """
    Loads and converts a DCS route planning tool file from luadata to py-dict

    Arguments:
        filepath {str} -- filepath to DCS route file

    Returns:
        dict -- Converted dict of route file data
    """
    routes_data: RoutesData = luadata.read(filepath, encoding='utf-8')
    return routes_data



class Waypoint(TypedDict):
    """One point in a DCS‑route file."""
    speed_locked: bool
    type: str
    ETA: int
    ETA_locked: bool
    y: float
    x: float
    name: str
    action: str
    alt_type: str
    alt: float



class RoutesData(TypedDict):
    """A named route consisting of an ordered list of waypoints."""
    # routes_data = dict[str, list[Waypoint]]
    route_name: str
    waypoints: list[Waypoint]
