import tkinter as tk
from datetime import datetime

def update_clock():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  clock_label.config(text=current_time)
  clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Arial", 80),bg="white",fg="black")
clock_label.pack(padx=50,pady=50)

update_clock()
root.mainloop()
