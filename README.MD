# 🌤️ Weather App

A modern, elegant desktop weather application built with Python and Tkinter. Get real-time weather information for any city worldwide with a beautiful, user-friendly interface.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![OpenWeather](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=for-the-badge)

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌍 **Global Search** | Find weather for any city worldwide |
| 🎨 **Modern UI** | Clean, professional interface with beautiful color scheme |
| 📱 **Responsive Design** | Adapts seamlessly to different window sizes |
| ⚡ **Real-time Data** | Live weather updates from OpenWeatherMap API |
| 📊 **Detailed Metrics** | Temperature, feels-like, humidity, wind speed, and conditions |
| 🔍 **Smart Validation** | Input validation with visual feedback |
| 🎯 **Quick Results** | Fast API responses with instant display |

## 🖼️ Application Preview

![alt text](<Output Screens/Screenshot 2025-11-23 150058.png>)

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Internet connection
- OpenWeatherMap API key (free)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install requests
   ```

3. **Get your API key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Navigate to API Keys in your dashboard
   - Copy your API key

4. **Configure the application**
   Edit `apikey.txt`:
   ```txt
   api_key = 'your_actual_api_key_here'
   ```

5. **Run the application**
   ```bash
   python main_file.py
   ```

## 🛠️ How to Use

1. **Launch** the application
2. **Enter** a city name in the search box (e.g., "Paris", "Tokyo", "New York")
3. **Press Enter** or click the **Search** button
4. **View** comprehensive weather information:
   - Current temperature and conditions
   - Feels-like temperature
   - Humidity percentage
   - Wind speed

## 📁 Project Structure

```
weather-app/
├── 📄 main_file.py         # Main application & GUI
├── 📄 weather_data.py      # API integration & data handling
├── 📄 apikey.txt           # API configuration
├── 📄 API_SETUP.md         # API configuration guide
├── 📄 README.md            # This documentation
├── 📄 STATEMENT.md         # Documenting project purpose and scope.
```

## 🔧 Technical Architecture

### Core Components

| Component | Purpose | Key Features |
|-----------|---------|--------------|
| **WeatherApp Class** | Main GUI application | Tkinter window management, UI layout, event handling |
| **WeatherData Class** | API communication | HTTP requests, data parsing, error handling |
| **OpenWeatherMap API** | Data source | Real-time weather data, global coverage |

### Key Technologies
- **Frontend**: Tkinter (Python's built-in GUI toolkit)
- **Networking**: Requests library for API calls
- **Data Format**: JSON for API responses
- **Styling**: Custom fonts and color schemes

## 🎨 UI Design Features

- **Color Scheme**: Modern blues and clean whites
- **Typography**: Segoe UI font family for optimal readability
- **Layout**: Card-based design with clear information hierarchy
- **Responsive**: Dynamic resizing with minimum window constraints
- **Interactive**: Hover effects and visual feedback

## 🌐 API Integration

The app uses OpenWeatherMap's Current Weather Data API:

```python
# API Endpoint
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Parameters
params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'  # Celsius
}
```

### Data Points Retrieved
- 🌡️ Temperature (current and feels-like)
- 💧 Humidity percentage
- 💨 Wind speed and direction
- ☁️ Weather conditions and descriptions
- 🏙️ City information

## ⚠️ Error Handling

The application gracefully handles various error scenarios:

- **Invalid City Names**: Shows "Not found" with clear indication
- **API Connection Issues**: Fails gracefully without crashing
- **Empty Search**: Visual feedback with temporary color change
- **Rate Limiting**: Respects API limits (60 calls/minute free tier)

## 🔄 Development

### Extending the Application

**Adding New Weather Metrics:**
```python
# In weather_data.py
def get_weather(self, city):
    # Add new data points
    new_metric = self.data['new']['metric']
    return {**existing_data, 'new_metric': new_metric}
```

**Creating New UI Components:**
```python
# In main_file.py
def _create_detail_row(self, label_text, key):
    # Follow existing pattern for new detail rows
```

### Code Quality Features
- PEP 8 compliance
- Modular architecture
- Descriptive variable names
- Comprehensive error handling
- Separation of concerns (GUI vs. Data logic)

## 📊 Performance

- **API Response Time**: Typically < 1 second
- **GUI Responsiveness**: Instant updates
- **Memory Usage**: Lightweight (~50MB)
- **Startup Time**: Immediate

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed description
2. **Suggest Features**: Propose new functionality or improvements
3. **Code Contributions**: Submit pull requests for enhancements
4. **Documentation**: Help improve documentation and examples

### Development Setup
```bash
# Fork and clone the repository
git clone <your-fork-url>
cd weather-app

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install requests
```
## Screenshots
* Startup Screen ![on startup](<Output Screens/Screenshot 2025-11-23 150058.png>)


* Query 1![alt text](<Output Screens/Screenshot 2025-11-23 150124.png>)
* Query 2![alt text](<Output Screens/Screenshot 2025-11-23 150139.png>)
* Query 3![alt text](<Output Screens/Screenshot 2025-11-23 150211.png>)
* Error Handling Demonstration![alt text](<Output Screens/Screenshot 2025-11-23 151852.png>)
## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **"API key invalid"** | Verify key in `apikey.txt` and account activation |
| **City not found** | Check spelling and try major cities first |
| **No internet** | Ensure stable internet connection |
| **Application crashes** | Verify Python version and dependencies |



## 🙏 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Built with Python and Tkinter
- Icons and design inspired by modern weather applications

## 📞 Support

- **Documentation**: Check this README and code comments
- **Issues**: Use the GitHub issue tracker
- **Questions**: Open a discussion in the repository

---

<div align="center">

**Enjoy using the Weather App! 🌈**

*Stay informed about the weather, wherever you are!*

</div>

---

*Note: This application requires an active internet connection and a valid OpenWeatherMap API key for functionality.*