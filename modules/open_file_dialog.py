from pathlib import Path
from tkinter import filedialog


def open_file_dialog() -> Path|None:
    """
    Opens a file dialog to select a DCS route file.

    Returns:
        Path -- Path to the selected file
    """


    initialdir = Path.home() / r"Saved Games/DCS/Config/RouteToolPresets"
    filepath = filedialog.askopenfilename(
        title="Select DCS Route File",
        initialdir=initialdir,
        filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")]
    )
    if not filepath:
        return None
    #     raise FileNotFoundError("No file selected.")

    return Path(filepath)
