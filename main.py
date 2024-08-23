import tkinter as tk

root = tk.Tk()
root.title("Weather Forecast & News Broadcast")
root.geometry("800x600")

# frame for date, time, location, 7-dat forecast
frame1 = tk.Frame(root, width=600, height=300, relief="ridge", bd=2, background="white")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# frame for 24-hour temperature bars
frame2 = tk.Frame(root, width=600, height=150, relief="ridge", bd=2, background="white")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# frame for news headlines
frame3 = tk.Frame(root, width=250, height=600, relief="ridge", bd=2, background="white")
frame3.grid(row=0, column=1, rowspan=2, padx=10, sticky="nsew")

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1, weight=1)



root.mainloop()