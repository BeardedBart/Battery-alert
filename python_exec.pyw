import psutil
import time
from tkinter import *

# Things to add:
# None

def convertTime(sec):
    mins, sec = divmod(sec, 60) 
    hrs, mins = divmod(mins, 60)
    return '%d:%02d:%02d' % (hrs, mins, sec)

def battery_info():
    bat = psutil.sensors_battery()
    procent = bat.percent
    isPowered = bat.power_plugged
    bat_left = convertTime(bat.secsleft)
    return procent, isPowered, bat_left

def show_warning():
    tk = Tk()
    tk.iconbitmap('C:/Users/polsk/Desktop/programmer things/Python programs/Small projects/battery alert/Battery-alert-/noun-battery-alert-1601231.ico')
    warn = Label(tk, text = 'LOW BATTERY LEVEL', font = ('Calibri', 60), fg = 'red', bg = '#242323')
    warn.pack()
    tk.mainloop()
    
def show_startup_info():
    tk = Tk()
    tk.iconbitmap('C:/Users/polsk/Desktop/programmer things/Python programs/Small projects/battery alert/Battery-alert-/noun-battery-alert-1601231.ico')
    warn = Label(tk, text = 'Im running!', font = ('Calibri', 20), fg = '#505bb5', bg = '#242323')
    warn.pack()
    tk.after(3000, lambda: tk.destroy())
    tk.mainloop()
    
def show_threat():
    tk = Tk()
    tk.iconbitmap('C:/Users/polsk/Desktop/programmer things/Python programs/Small projects/battery alert/Battery-alert-/noun-battery-alert-1601231.ico')
    warn = Label(tk, text = '15%!!! PLUG IN PSU!!!', font = ('Calibri', 60), fg = 'red', bg = '#242323')
    warn.pack()
    tk.mainloop()

def main():
    show_startup_info()
    while True:
        procent, isPowered, bat_left = battery_info()
        print(f'Pozostało {procent}%, starczy na: {bat_left}')
        
        # dorób funkcję wykorzystującą parametr isPowered
        while isPowered is not True:
            if procent == 19: show_warning()
            elif procent <= 15: show_threat()
        
        time.sleep(15)
    

if __name__ == '__main__':
    main()