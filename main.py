import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime


root = tk.Tk()
root.title("Weather Forecast & News Broadcast")
root.geometry("800x600")


# frame for date, time, location, 7-dat forecast
frame1 = tk.Frame(root, width=600, height=300, relief="ridge", bd=2, background="white")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# frame for 24-hour temperature bars
frame2 = tk.Frame(root, width=600, height=150, relief="ridge", bd=2, background="white")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

# frame for news headlines
frame3 = tk.Frame(root, width=250, height=600, relief="ridge", bd=2, background="white")
frame3.grid(row=0, column=1, rowspan=2, padx=10, sticky="nw")

# date, time & location labels
date_label = tk.Label(frame1, text=datetime.now().strftime("%A, %d, %B, %Y"), font=("Helvetica", 14))
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

time_label = tk.Label(frame1, text=datetime.now().strftime("%H:%M:%S"), font=("Helvetica", 14))
time_label.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

location_label = tk.Label(frame1, text="Istanbul", font=("Helvetica", 14))
location_label.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

# configuration of the grid for the frame
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)
frame1.grid_rowconfigure(2, weight=1)
frame1.grid_rowconfigure(3, weight=1)

# 7-day forecast layout
forecast_frame = tk.Frame(frame1)
forecast_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="sew")
forecast_frame.grid_columnconfigure(tuple(range(7)),weight=1)

# placeholder path for the weather icons
icon_paths = [
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\cloudy.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\mixed.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\raining.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\showering.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\snowing.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\storm.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\sunny.png",
    "C:\\Users\\mhmts\\PycharmProjects\\weather forecast & broadcast\\warm-cloudy.png"
]

# 7-day forecast layout
for i in range(7):
    day_frame = tk.Frame(forecast_frame, relief="ridge", bd=1)
    day_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")


    # load weather icons
    img = Image.open(icon_paths[i])
    img = img.resize((50,50), Image.LANCZOS)
    icon_img = ImageTk.PhotoImage(img)

    # placeholder for weather icon
    icon_label = tk.Label(day_frame, image=icon_img)
    icon_label.image = icon_img
    icon_label.pack()

    # placeholder for Day
    day_label = tk.Label(day_frame, text=f"Day {i+1}", font=("Helvetica", 10))
    day_label.pack(pady=5)

    # placeholder for temperature
    temp_label = tk.Label(day_frame, text=f"{20+i}°C", font=("Helvetica", 12))
    temp_label.pack(side=tk.BOTTOM, pady=5)


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

update_time()

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)



root.mainloop()