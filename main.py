import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import requests

# coordinates for the cities
cities = {
    "Istanbul": {"lat": 41.015137, "lon": 28.979530},
    "Tekirdağ": {"lat": 40.977779, "lon": 27.515278},
    "Tokat": {"lat": 40.316667, "lon": 36.55}
}

selected_city = "Istanbul"
API_KEY = "3556c30d49b807fffbe5214c6bccde78"  # Replace with your valid API key

# weather icons
weather_icon_mapping = {
    "Clouds": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\cloudy.png",
    "Drizzle": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\mixed.png",
    "Rain": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\raining.png",
    "Shower rain": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\showering.png",
    "Snow": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\snowing.png",
    "Thunderstorm": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\storm.png",
    "Clear": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\sunny.png",
    "Mist": "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\warm-cloudy.png"
}

# get weather data from api
def fetch_weather_data(lat, lon):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def fetch_air_pollution_data(lat, lon):
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status() # raise error for bad response
        air_quality_data = response.json()
        return air_quality_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching air pollution data: {e}")
        return None

def update_air_quality():
    global selected_city
    city_coords = cities[selected_city]
    air_quality_data = fetch_air_pollution_data(city_coords["lat"], city_coords["lon"])

    if air_quality_data is None:
        print("Air pollution data is not available")
        return
    
    # extract the first record from the list
    pollution_info = air_quality_data["list"][0]
    aqi = pollution_info["main"]["aqi"]
    components = pollution_info["components"]

    # clear the frame
    for widget in frame2.winfo_children():
        widget.destroy()

    # display AQI
    aqi_label = tk.Label(frame2, text=f"Air Quality Ingex (AQI): {aqi}", font=("Helvetica", 14))
    aqi_label.pack()

    # display detailed polutant data
    pollutant_labels = {
        "CO": f"CO: {components['co']} µg/m³",
        "NO": f"NO: {components['no']} µg/m³",
        "NO2": f"NO2: {components['no2']} µg/m³",
        "O3": f"O3: {components['o3']} µg/m³",
        "SO2": f"SO2: {components['so2']} µg/m³",
        "PM2.5": f"PM2.5: {components['pm2_5']} µg/m³",
        "PM10": f"PM10: {components['pm10']} µg/m³",
        "NH3": f"NH3: {components['nh3']} µg/m³"
    }

    for key, text in pollutant_labels.items():
        pollutant_label = tk.Label(frame2, text=text, font=("Helvetica", 12))
        pollutant_label.pack(anchor="w", padx=20)
    
    # interpretation of AQI
    if aqi <= 50:
        quality_text = "Good: Air quality is considered satisfactory."
    elif aqi <= 100:
        quality_text = "Moderate: Air quality is acceptable; some pollutants may pose a moderate health concern for sensitive people."
    elif aqi <= 150:
        quality_text = "Unhealthy for Sensitive Groups: People with respiratory or heart conditions may experience effects."
    elif aqi <= 200:
        quality_text = "Unhealthy: Everyone may begin to experience health effects."
    elif aqi <= 300:
        quality_text = "Very Unhealthy: Health alert; everyone may experience more serious health effects."
    else:
        quality_text = "Hazardous: Health warnings of emergency conditions. The entire population is more likely to be affected."

    quality_label = tk.Label(frame2, text=quality_text, font=("Helvetica", 12), fg="red")
    quality_label.pack(pady=10)

def update_weather():
    global selected_city
    city_coords = cities[selected_city]
    weather_data = fetch_weather_data(city_coords["lat"], city_coords["lon"])

    if weather_data is None:
        print("Weather data is not available.")
        return

    # update 3-hour forecast
    for i in range(8):  # Adjust this number based on how many intervals you want to display
        interval_weather = weather_data["list"][i]
        temp = interval_weather["main"]["temp"]
        weather_descirption = interval_weather["weather"][0]["main"]   # get the main weather description

        # extract and format time from dt_txt
        raw_time = interval_weather["dt_txt"]
        formatted_time = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S").strftime("%H:%M")

        # map the weather description to the corresponding local image
        icon_path = weather_icon_mapping.get(weather_descirption, "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\default.png")

        day_label[i].config(text=formatted_time)
        temp_label[i].config(text=f"{temp}°C")
        
        # load weather icon from local path
        img = Image.open(icon_path)
        img = img.resize((50,50), Image.LANCZOS)
        icon_img = ImageTk.PhotoImage(img)
        icon_label[i].config(image=icon_img)
        icon_label[i].image = icon_img

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

def on_city_selected(selection):
    global selected_city
    selected_city = selection
    location_label.config(text=selected_city)
    update_weather()
    update_air_quality()


root = tk.Tk()
root.title("Weather Forecast & News Broadcast")
root.geometry("900x600")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Frame for date, time, location, 7-day forecast (now 3-hour intervals)
frame1 = tk.Frame(root, width=600, height=200, relief="ridge", bd=2, background="white")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Frame for 24-hour temperature bars (now 8 intervals)
frame2 = tk.Frame(root, width=600, height=300, relief="ridge", bd=2, background="white")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Frame for news headlines
frame3 = tk.Frame(root, width=250, height=600, relief="ridge", bd=2, background="white")
frame3.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

# Date, time & location labels
date_label = tk.Label(frame1, text=datetime.now().strftime("%A, %d, %B, %Y"), font=("Helvetica", 14))
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

time_label = tk.Label(frame1, text=datetime.now().strftime("%H:%M:%S"), font=("Helvetica", 14))
time_label.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

location_label = tk.Label(frame1, text="Istanbul", font=("Helvetica", 14))
location_label.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

# dropdown menu for city selection
city_var = tk.StringVar(value=selected_city)
city_menu = tk.OptionMenu(frame1, city_var, *cities.keys(), command=on_city_selected)
city_menu.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

# Configuration of the grid for the frame
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)
frame1.grid_rowconfigure(2, weight=1)
frame1.grid_rowconfigure(3, weight=1)

# 3-hour forecast layout (adjusted from 7-day layout)
forecast_frame = tk.Frame(frame1)
forecast_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="sew")
forecast_frame.grid_columnconfigure(tuple(range(8)),weight=1)  # Adjusted for 8 intervals

icon_label = [None] * 8
day_label = [None] * 8
temp_label = [None] * 8

# 3-hour forecast layout
for i in range(8):  # Adjusted to display 8 intervals
    day_frame = tk.Frame(forecast_frame, relief="ridge", bd=1)
    day_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

    icon_label[i] = tk.Label(day_frame)
    icon_label[i].pack()

    day_label[i] = tk.Label(day_frame, font=("Helvetica", 10))
    day_label[i].pack(pady=5)

    temp_label[i] = tk.Label(day_frame, font=("Helvetica", 12))
    temp_label[i].pack(side=tk.BOTTOM, pady=5)

update_time()
update_weather()
update_air_quality()

root.mainloop()
