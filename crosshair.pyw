readme = open("readme.txt", "w")
readme.write("How To Use:\n\n1. press f2 to toggle program on/off (when run it will default to off)\n2. press f3 to "
             "make the crosshair bigger\n3. press f4 to make crosshair smaller\n4. to change the symbol of the "
             "crosshair open the program with a text editor and on line 22 change the symbol in the parenthesis\n5. "
             "in order for crosshair to show up in games make sure the game is set to borderless window, it will not "
             "work when fullscreen") 
readme.close()

import time
from tkinter import *
import os
try:
    import win32api
except:
    imports = open("imports.bat", "w")
    imports.write("@echo off\npip install pywin32")
    imports.close()
    os.system('imports.bat')
    os.remove('imports.bat')
    import win32api

character = "+"
size = 30
hotkey = False
overlay = Tk()
overlay.title("Crosshair")
overlay.attributes('-fullscreen', True)
overlay.wm_attributes('-transparentcolor', overlay['bg'])
overlay.attributes('-topmost', True)
label = Label(overlay, text="", fg="green", font=("Times New Roman", size))
label.place(relx=0.5, rely=0.5, anchor='center')

while True:

    overlay.update()

    hotkey_test = win32api.GetKeyState(0x71)
    if hotkey_test < 0:
        time.sleep(.2)
        label.destroy()
        label = Label(overlay, text=character, fg="green", font=("Times New Roman", size))
        label.place(relx=0.5, rely=0.5, anchor='center')
        hotkey = True

    while hotkey:

        overlay.update()

        hotkey_test = win32api.GetKeyState(0x71)
        if hotkey_test < 0:
            time.sleep(.2)
            label.destroy()
            label = Label(overlay, text="", fg="green", font=("Times New Roman", size))
            label.place(relx=0.5, rely=0.5, anchor='center')
            hotkey = False

        up = win32api.GetKeyState(0x72)
        if up < 0:
            size = size + 1
            label.destroy()
            label = Label(overlay, text=character, fg="green", font=("Times New Roman", size))
            label.place(relx=0.5, rely=0.5, anchor='center')

        down = win32api.GetKeyState(0x73)
        if down < 0:
            if size > 0:
                size = size - 1
                label.destroy()
                label = Label(overlay, text=character, fg="green", font=("Times New Roman", size))
                label.place(relx=0.5, rely=0.5, anchor='center')
