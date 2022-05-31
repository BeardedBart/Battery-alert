# Simpler version of previous app
from tkinter import *
import psutil
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

def showPercent():
    batt = psutil.sensors_battery()
    procent = batt.percent
    state = batt.power_plugged
    
    if procent <= 20:
        lbl.config(text = f'{procent}%', fg = 'red')
    elif state == True:
        lbl.config(text = f'{procent}%', fg = 'green')
    else:
        lbl.config(text = f'{procent}%', fg = 'white')
        
    lbl.after(1000, showPercent)

win = Tk()
win.overrideredirect(1)

lbl = Label(win, text = '', font = ('Open 24 Display St', 20), fg = 'white')
lbl.pack()
showPercent()

win.attributes('-topmost', True)
win.wm_attributes('-transparentcolor', win['bg'])
# win.wm_attributes('-fullscreen', 'True')

win.mainloop()