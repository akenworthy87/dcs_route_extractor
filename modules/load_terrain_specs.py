from pathlib import Path
import yaml


def load_terrain_specs(filepath: Path):
    terrain_name = split_filename_from_path(Path(filepath))
    terrain_specs_init = load_terrain_specs_from_file(terrain_name)
    validate_terrain_specs(terrain_specs_init)
    return terrain_specs_init


def validate_terrain_specs(terrain_specs_init: dict|None):
    required_keys = ['origin_mgrs', 'central_meridian', 'scale_factor']
    assert isinstance(terrain_specs_init, dict), "Terrain specs should be a dictionary."
    for key in required_keys:
        if key not in terrain_specs_init:
            raise ValueError(
                f"Missing required key '{key}' in terrain specs. Please check the yaml file and try again.")

def list_available_terrain_specs():
    filelist = sorted([f.stem for f in Path('terrain_specs').glob('*.yaml')])
    return filelist


def load_terrain_specs_from_file(terrain_name: str) -> dict:
    """
    Loads terrain specs from yaml file

    Arguments:
        terrain_name {str} -- Name of terrain to load specs for
    """
    # terrain_specs_init = None
    filelist = list_available_terrain_specs()
    if terrain_name not in filelist:
        print(
            f"Error: Terrain specs file for {terrain_name} not found. Terrain specs available for selection:")
        spec_name = select_terrain_spec(filelist)
    else:
        spec_name = terrain_name

    with open(f'terrain_specs/{spec_name}.yaml', 'r') as f:
        terrain_specs_init = yaml.safe_load(f)
    return terrain_specs_init


def select_terrain_spec(filelist: list[str] | None = None) -> str:
    if filelist is None:
        filelist = []
    enumerate_keys = list(enumerate(filelist, start=1))
    if len(enumerate_keys) == 0:
        print("No terrain specs files found in terrain_specs folder. Please add a yaml file with terrain specs and try again.")
        raise FileNotFoundError(
            "No terrain specs files found in terrain_specs folder.")

    print("Select a route name:")
    for i, key in enumerate_keys:
        print(f"{i}: {key}")
    while True:
        choice = input("Enter the number of the route name: ")
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(enumerate_keys):
                terrain_name = enumerate_keys[choice_int - 1][1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return terrain_name


def split_filename_from_path(filepath: Path) -> str:
    filename = filepath.stem
    return filename.capitalize()
