import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from weather_data import WeatherData
wd=WeatherData()

# GUI Configuration / constants
WIN_WIDTH = 800
WIN_HEIGHT = 400
BG_COLOR = "#F3F6FA"
PANEL_COLOR = "#FFFFFF"
ACCENT = "#2B90FF"
TEXT_PRIMARY = "#1F2937"
TEXT_SECONDARY = "#667085"
TEMP_BOX_COLOR = "#FFFFFF"
SMALL_BOX_COLOR = "#F8FAFF"
PLACEHOLDER_COLOR = "#9AA4B2"

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.minsize(700, 350)
        self.configure(bg=BG_COLOR)

        # Fonts
        self.font_large = tkfont.Font(family="Segoe UI", size=42, weight="bold")
        self.font_medium = tkfont.Font(family="Segoe UI", size=14)
        self.font_small = tkfont.Font(family="Segoe UI", size=11)
        self.font_button = tkfont.Font(family="Segoe UI", size=11, weight="bold")

        # WeatherData instance
        self.wd = WeatherData()

        # Main container frame
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(fill="both", expand=True, padx=20, pady=18)

        self._create_search_bar()
        self._create_main_panels()