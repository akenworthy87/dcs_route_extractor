


def test_split_filename_from_path():
    from modules.load_terrain_specs import split_filename_from_path
    from pathlib import Path
    
    # Test case 1: Regular filename
    filepath1 = Path("C:/path/to/terrain_spec.lua")
    assert split_filename_from_path(filepath1) == "terrain_spec"
    
    # Test case 2: Filename with multiple dots
    filepath2 = Path("C:/path/to/terrain.spec.lua")
    assert split_filename_from_path(filepath2) == "terrain.spec"
    
    # Test case 3: Filename without extension
    filepath3 = Path("C:/path/to/terrain_spec")
    assert split_filename_from_path(filepath3) == "terrain_spec"
    
    # Test case 4.1: Filename with spaces
    filepath4p1 = Path("C:/path/to/terrain spec.lua")
    assert split_filename_from_path(filepath4p1) == "terrain spec"
    # Test case 4.2: Filename with spaces
    filepath4p2 = Path("C:/path/to/Terrain Spec.lua")
    assert split_filename_from_path(filepath4p2) == "Terrain Spec"
    
    # Test case 5: Filename in PacalCase
    filepath5 = Path("C:/path/to/TerrainSpec.lua")
    assert split_filename_from_path(filepath5) == "TerrainSpec"
    
    print("All test cases passed for split_filename_from_path()")


def test_list_available_terrain_specs():
    from modules.load_terrain_specs import list_available_terrain_specs
    
    # Assuming there are some yaml files in the terrain_specs folder for testing
    available_specs = list_available_terrain_specs()
    
    # Check that the function returns a list
    assert isinstance(available_specs, list)
    
    # Check that length is at least 1
    assert len(available_specs) >= 1
    
    # Check that the list contains strings (filenames without extension)
    for spec in available_specs:
        assert isinstance(spec, str)
    
    print("All test cases passed for list_available_terrain_specs()")
    
