import tkinter as tk
from time import strftime

def time():
    string = strftime('%I:%M:%S  %p')
    label.config(text = string)
    label.after(1000, time)

root = tk.Tk()
root.title("Beautiful Digital Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='gray', foreground='white')
label.pack(anchor = 'center')

time()
root.mainloop()