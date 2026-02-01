from pathlib import Path

def process_argv(argv: list) -> tuple[Path|None, str|None]:
    filepath = None
    routename = None
    
    if len(argv) > 1:
        filepath = Path(argv[1])
    if len(argv) > 2:
        routename = argv[2]

    return (filepath, routename)