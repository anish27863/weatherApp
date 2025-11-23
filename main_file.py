import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from weather_data import WeatherData
wd=WeatherData()

# GUI Configuration / constants
WIN_WIDTH = 350
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

    def _create_main_panels(self):
        main_frame = tk.Frame(self.container, bg=BG_COLOR)
        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_frame, bg=BG_COLOR)
        left_frame.pack(side="left", fill="both", expand=True)

        shadow = tk.Frame(left_frame, bg="#E6EAF2", bd=0)
        shadow.place(relx=0.02, rely=0.05, relwidth=0.94, relheight=0.9)

        self.temp_box = tk.Frame(left_frame, bg=TEMP_BOX_COLOR, bd=0)
        self.temp_box.place(relx=0.0, rely=0.0, relwidth=0.94, relheight=0.9)

        self.city_label = tk.Label(self.temp_box, text="City", bg=TEMP_BOX_COLOR, fg=TEXT_SECONDARY,
                                   font=self.font_small)
        self.city_label.pack(anchor="nw", padx=18, pady=(14, 0))

        self.condition_label = tk.Label(self.temp_box, text="Condition", bg=TEMP_BOX_COLOR, fg=TEXT_SECONDARY,
                                        font=self.font_small)
        self.condition_label.pack(anchor="nw", padx=18, pady=(2, 0))

        temp_frame = tk.Frame(self.temp_box, bg=TEMP_BOX_COLOR)
        temp_frame.pack(expand=True)

        self.temp_label = tk.Label(temp_frame, text="0°C", bg=TEMP_BOX_COLOR, fg=TEXT_PRIMARY,
                                   font=self.font_large)
        self.temp_label.pack(anchor="center")

        right_frame = tk.Frame(main_frame, bg=BG_COLOR, width=220)
        right_frame.pack(side="right", fill="y", padx=(14, 0))

        self.small_box = tk.Frame(right_frame, bg=SMALL_BOX_COLOR, bd=0)
        self.small_box.pack(fill="both", expand=True)

        small_title = tk.Label(self.small_box, text="Details", bg=SMALL_BOX_COLOR, fg=TEXT_SECONDARY,
                               font=self.font_medium)
        small_title.pack(anchor="nw", padx=12, pady=(12, 6))

        self.details_container = tk.Frame(self.small_box, bg=SMALL_BOX_COLOR)
        self.details_container.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self._create_detail_row("Feels like:", "feels_like")
        self._create_detail_row("Humidity:", "humidity")
        self._create_detail_row("Wind:", "wind")

    def _create_detail_row(self, label_text, key):
        row = tk.Frame(self.details_container, bg=SMALL_BOX_COLOR)
        row.pack(fill="x", pady=6)

        lbl = tk.Label(row, text=label_text, bg=SMALL_BOX_COLOR, fg=TEXT_SECONDARY, font=self.font_small)
        lbl.pack(side="left")

        val = tk.Label(row, text="—", bg=SMALL_BOX_COLOR, fg=TEXT_PRIMARY, font=self.font_small)
        val.pack(side="right")

        setattr(self, f"detail_{key}", val)

    def update_weather(self, data: dict):
        self.city_label.config(text=data.get("city", "—"))
        self.condition_label.config(text=data.get("condition", "—"))
        self.temp_label.config(text=data.get("temp", "—"))
        self.detail_feels_like.config(text=data.get("feels_like", "—"))
        self.detail_humidity.config(text=data.get("humidity", "—"))
        self.detail_wind.config(text=data.get("wind", "—"))

    def _add_placeholder(self, entry: tk.Entry, placeholder: str):
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg=TEXT_PRIMARY)

        def on_focus_out(event):
            if not entry.get().strip():
                entry.insert(0, placeholder)
                entry.config(fg=PLACEHOLDER_COLOR)

        entry.insert(0, placeholder)
        entry.config(fg=PLACEHOLDER_COLOR)
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def _on_search(self, event=None):
        query = self.search_var.get()
        if not query or query.startswith("Enter city"):
            original_bg = self.search_entry["bg"]
            self.search_entry.config(bg="#FFEFEF")
            self.after(220, lambda: self.search_entry.config(bg=original_bg))
            return

        data = self.wd.get_weather(query)
        if data:
            self.update_weather({
                "city": query.title(),
                "temp": f"{self.wd.main['temp']}°C",
                "feels_like": f"{self.wd.main['feels_like']}°C",
                "humidity": f"{self.wd.main['humidity']}%",
                "condition": self.wd.weather_desc,
                "wind": f"{self.wd.data['wind']['speed']} kmph",
            })
        else:
            self.update_weather({
                "city": "Not found",
                "temp": "—",
                "feels_like": "—",
                "humidity": "—",
                "condition": "Not available",
                "wind": "—",
            })

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()