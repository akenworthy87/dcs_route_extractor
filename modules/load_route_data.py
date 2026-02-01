from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pathlib import Path

import luadata


def load_route_data(filepath: Path) -> dict:
    """
    Loads and converts a DCS route planning tool file from luadata to py-dict

    Arguments:
        filepath {str} -- filepath to DCS route file

    Returns:
        dict -- Converted dict of route file data
    """
    route_data = luadata.read(filepath, encoding='utf-8')
    return route_data
