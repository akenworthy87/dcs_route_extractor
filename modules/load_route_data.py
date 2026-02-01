import luadata

def load_route_data(filepath = r'') -> dict:
    route_data = luadata.read(filepath, encoding='utf-8')
    return route_data