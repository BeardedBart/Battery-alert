# Simpler version of previous app
from tkinter import *
import psutil
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

def showPercent():
    batt = psutil.sensors_battery()
    procent = batt.percent
    
    if procent <= 20:
        lbl.config(text = f'{procent}%', fg = 'red')
    else:
        lbl.config(text = f'{procent}%')
        
    lbl.after(1000, showPercent)

win = Tk()
win.overrideredirect(1)

lbl = Label(win, text = '', font = ('Calibri', 20), fg = 'white')
lbl.pack()
showPercent()

win.attributes('-topmost', True)
win.wm_attributes('-transparentcolor', win['bg'])
# win.wm_attributes('-fullscreen', 'True')

win.mainloop()