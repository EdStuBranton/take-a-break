import time
import tkinter as tk
from tkinter import ttk
from PIL import Image

from playsound import playsound
import sys

picture = r'take_a_break_logo.png'

def convert_image_format(image):
    im = Image.open(image)
    im.save('take_a_break_logo.ico', format='ICO')

def destroy_window():
    root.destroy()
    
def set_time():
    t = 1500
    return countdown(t)

def countdown(t):
    minutes, seconds = divmod(t, 60)    
    time_label.configure(text='{:02d}:{:02d}'.format(minutes, seconds))
    if t > 0:
        time_label.after(1000, countdown, t-1)
    else:
        time_label.configure(text='take a break')
        playsound('cuteplop.wav')
    
def close_program():
    sys.exit()



root = tk.Tk()
root.wm_iconbitmap('take_a_break_logo.ico')
root.title('take a break')
root.geometry('500x200')
message_lbl = tk.Label(text='Take a break', width=15, background='#f2f2f2', font='courier 15 bold')
time_label = tk.Label(root, text='timer', background='#dfdede', font=('verdana', 30))
start_button = tk.Button(root, text='Start', bg='#cecece', command=set_time)
stop_button = tk.Button(root, bg='#bdbdbd', text='Stop')
restart_button = tk.Button(root, bg='#aba7a7', text='Restart', command=set_time)
quit_button = tk.Button(root, bg='#f2f2f2', text='Quit', command=close_program)


start_button.grid(column=0, row=2, sticky='nsew')
stop_button.grid(column=1, row=2, sticky='nsew')
restart_button.grid(column=2, row=2, sticky='nsew')
quit_button.grid(column=3, row=2, sticky='nsew')
message_lbl.grid(column=0, row=0, columnspan=4, sticky='nsew')
time_label.grid(column=0, row=1, columnspan=4, sticky='nsew')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=7)

root.mainloop()