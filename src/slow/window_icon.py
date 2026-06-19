import sys
from tkinter import PhotoImage, TclError

from .paths import resource_path_string


def set_window_icon(window):
    """Set the SLOW window icon without making startup depend on icon support."""
    ico_path = resource_path_string("Logo_Slow_Icon_Map.ico")
    png_path = resource_path_string("Logo_Slow_Icon_Map.png")

    if sys.platform.startswith("win"):
        try:
            window.iconbitmap(ico_path)
            return
        except TclError:
            pass

    try:
        icon = PhotoImage(master=window, file=png_path)
        window.iconphoto(True, icon)
        window._slow_icon_image = icon
    except (OSError, TclError):
        try:
            window.iconbitmap(ico_path)
        except TclError:
            pass
