Weather Forecast & News Broadcast App

Overview
This is a Python-based desktop application that provides real-time weather forecasts, air quality information, and the latest news headlines. The application fetches data from the OpenWeatherMap API and BBC News, presenting it in a user-friendly interface using Tkinter.

Features
Real-Time Weather Forecast: Displays a 24-hour weather forecast, showing temperature and weather conditions in 3-hour intervals.
Air Quality Index (AQI): Provides detailed air quality data, including pollutants such as CO, NO, NO2, O3, SO2, PM2.5, PM10, and NH3.
Latest News Headlines: Fetches and displays the latest headlines from BBC News in a scrollable format.
City Selection: Users can choose between multiple cities (Istanbul, Tekirdağ, Tokat) to view localized weather and air quality information.
Dynamic Updates: The app dynamically updates time, weather, air quality, and news without restarting.


Installation
Prerequisites
Python 3.x: Ensure you have Python 3.x installed.
pip: Python package installer should be installed.

git clone https://github.com/TurtleWithGlasses/weather-news-app.git
cd weather-news-app


Install Required Libraries
Install the necessary Python packages using pip:

pip install requests
pip install Pillow
pip install beautifulsoup4


Setup API Key
Create an account at OpenWeatherMap to obtain your free API key.
Replace the placeholder API_KEY in the script with your actual OpenWeatherMap API key.

Usage
Run the Application: Execute the following command in your terminal to start the app:

python main.py

Select a City: Use the dropdown menu to select a city. The app will update the weather, air quality, and news based on the selected city.

View Data:
Weather: The top left of the window shows a 24-hour weather forecast.
Air Quality: Below the weather forecast, the AQI and pollutant details are displayed.
News: On the right side, the latest headlines from BBC News are presented in a scrollable format.

Project Structure

weather-news-app/
│
├── main.py                 # Main application script
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── assets/
    ├── cloudy.png          # Weather icons
    ├── sunny.png
    └── ... (other icons)
Contributions
Contributions are welcome! If you'd like to improve the app or add new features, feel free to fork the repository and submit a pull request.

Acknowledgments
OpenWeatherMap: For providing the weather and air quality data.
BBC News: For the latest headlines.
Python & Tkinter: For making it easy to build desktop applications.
