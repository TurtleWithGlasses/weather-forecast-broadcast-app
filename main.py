import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime


root = tk.Tk()
root.title("Weather Forecast & News Broadcast")
root.geometry("800x600")


# frame for date, time, location, 7-dat forecast
frame1 = tk.Frame(root, width=600, height=200, relief="ridge", bd=2, background="white")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# frame for 24-hour temperature bars
frame2 = tk.Frame(root, width=600, height=300, relief="ridge", bd=2, background="white")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# frame for news headlines
frame3 = tk.Frame(root, width=250, height=600, relief="ridge", bd=2, background="white")
frame3.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

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

# frame 2 - hourly temperature bars
def create_temperature_bars(frame, temperatures):
    canvas = tk.Canvas(frame, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # calculate the maximum temperature for scaling the bars
    max_temp = max(temperatures)

    bar_width = 15
    spacing = 5

    for i, temp in enumerate(temperatures):
        # scale the height of the bar according to the temperature
        bar_height = (temp / max_temp) * 200
        x0 = i * (bar_width + spacing) + spacing
        y0 = 250 - bar_height
        x1 = x0 + bar_width
        y1= 250

        # draw the bar
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

        # label the bar with the temperature
        canvas.create_text(x0 + bar_width // 2, y0 - 10, text=f"{temp}°C", font=("Helvetica", 7))
        canvas.create_text(x0 + bar_width // 2, 260, text=f"{i}h", font=("Helvetiva", 7))

temperatures = [15, 17, 19, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 12, 14, 16, 18, 20, 22, 24, 23]

create_temperature_bars(frame2, temperatures)

root.mainloop()