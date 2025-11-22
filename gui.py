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

    def _create_search_bar(self):
        top_frame = tk.Frame(self.container, bg=BG_COLOR)
        top_frame.pack(fill="x", pady=(0, 14))

        # Search Entry with placeholder behavior
        entry_bg = PANEL_COLOR
        self.search_var = tk.StringVar()
        entry_frame = tk.Frame(top_frame, bg=entry_bg, bd=0)
        entry_frame.pack(side="left", fill="x", expand=True)

        self.search_entry = tk.Entry(
            entry_frame,
            textvariable=self.search_var,
            fg=TEXT_PRIMARY,
            bg=entry_bg,
            relief="flat",
            font=self.font_medium,
            insertbackground=TEXT_PRIMARY,
            highlightthickness=0,
        )
        self.search_entry.pack(fill="x", ipady=10, padx=(10, 0))
        self.search_entry.bind("<Return>", self._on_search)
        self._add_placeholder(self.search_entry, "Enter city name, e.g. London")

        # Search Button
        search_btn = tk.Button(
            top_frame,
            text="Search",
            command=self._on_search,
            bg=ACCENT,
            fg="white",
            bd=0,
            activebackground="#1E7CE8",
            font=self.font_button,
            padx=20,
            pady=8,
            cursor="hand2",
        )
        search_btn.pack(side="right", padx=(12, 0))
