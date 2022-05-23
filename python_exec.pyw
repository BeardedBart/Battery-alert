import psutil
import time
from tkinter import *
from PIL import ImageTk, Image
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1) # pozwala na wyostrzenie tekstu

tk = Tk()
tk.title('Battery checker')
tk.geometry('350x200')
tk.config(bg = '#453534')


def convertTime(sec):
    mins, sec = divmod(sec, 60) 
    hrs, mins = divmod(mins, 60)
    return '%d:%02d:%02d' % (hrs, mins, sec)


def show_warning():
    global top_warn
    if top_warn:
        time.sleep(5)
        top_warn.destroy()
    else:
        top_warn = Toplevel()
        warn = Label(top_warn, text = 'LOW BATTERY LEVEL', font = ('Calibri', 60), fg = 'red', bg = '#453534')
        warn.pack()
    
    
def show_threat():
    global top_threat
    if top_threat:
        time.sleep(5)
        top_threat.destroy() # to spowoduje, że jeżeli aplikacja została wyświetlona, to warunek ją zamknie
    else:
        top_threat = Toplevel()
        warn = Label(top_threat, text = '15%!!! PLUG IN PSU!!!', font = ('Calibri', 60), fg = 'red', bg = '#453534')
        warn.pack()


def show_procent():
    battery = psutil.sensors_battery() # zmienna musi być zawsze zdefiniowana wewnątrz funkcji, inaczej się wszystko jebie
    procent = battery.percent
    
    procent_ent.config(text = f'{procent}%')
    procent_ent.after(1000, show_procent)

    if procent <= 20: show_warning()
    if procent == 15: show_threat()


def show_state():
    battery = psutil.sensors_battery()
    state = battery.power_plugged
    
    status_ent.config(text = f'{state}')
    status_ent.after(1000, show_state)


def show_left():
    battery = psutil.sensors_battery()
    bat_left = convertTime(battery.secsleft)
    
    time_ent.config(text = f'{bat_left} h')
    time_ent.after(1000, show_left)

# def logic_1s():
#     bat = psutil.sensors_battery()
#     procent = bat.percent
#     isPowered = bat.power_plugged
        
#     if not isPowered and procent <= 95: print('Working!')
#     if not isPowered and procent == 15: show_threat()
#     tk.after(1000, logic_1s)


if __name__ == '__main__':
    # while True:
    #     procent, isPowered, bat_left = battery_info()
    #     print(f'Pozostało {procent}%, starczy na: {bat_left}')
        
    #     # dorób funkcję wykorzystującą parametr isPowered
        
    #     if procent <= 25: show_warning()
        
    #     elif procent <= 15: show_threat()
        
    #     time.sleep(15)

    # Ukazuje poziom naładowania baterii w procentach
    
    top_warn = None
    
    lbl = Label(tk, text = 'Pozostało procent: ', font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    lbl.grid(row = 0, column = 0, padx = 5, pady = 25)
    
    procent_ent = Label(tk, text = '', font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    procent_ent.grid(row = 0, column = 1)
    show_procent()
    
    status_lbl = Label(tk, text = 'Podłączony: ', font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    status_lbl.grid(row = 1, column = 0)

    status_ent = Label(tk, text = '' ,font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    status_ent.grid(row = 1, column = 1)
    show_state()
    
    time_lbl = Label(tk, text = 'Pozostało: ', font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    time_lbl.grid(row = 2, column = 0, pady = 25)
    
    time_ent = Label(tk, text = '', font = ('Calibri', 12), fg = '#f2c821', bg = '#453534')
    time_ent.grid(row = 2, column = 1)
    show_left()

    tk.attributes('-topmost', True) # sprawia, że aplikacja jest zawsze widoczna 
    
    tk.mainloop()
