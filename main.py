import tkinter as tk
from pygame import mixer  
import psycopg2
import os
import os.path
import time
import sys

# variables for main window size (pixels)

HEIGHT = 800
WIDTH = 1200

# image paths

MAIN_ICON = os.path.join('/','home', 'vladimir','Documents','programming','mp3player','pictures', 'main_icon3.png')

# colors 

SAILOR_BLUE = '#296C92'
MINT_GREEN = '#CFFFE5'
WHITE = '#FFFFFF'

# main window options

root = tk.Tk()
root.title('MP3 player by vladimirferko')
root.geometry('{}x{}'.format(WIDTH, HEIGHT))
root.resizable(0,0)

img = tk.PhotoImage(file= MAIN_ICON)
root.tk.call('wm', 'iconphoto', root._w, img)

# login / register interface class

class LoginWindow:
    def __init__(self, master):
        self.main_frame = tk.Frame(master, width = WIDTH, height = HEIGHT, bg = SAILOR_BLUE)
        self.main_frame.pack()

        # bottom frame and its labels, there are clock and contact of this app

        self.bottom_frame = tk.Frame(self.main_frame, width = WIDTH, height = HEIGHT / 10, bg = MINT_GREEN)
        self.bottom_frame.place(x = 0, y = HEIGHT - (HEIGHT / 10))

        self.clock = tk.Label(self.bottom_frame, text = 'ou ye', font = ('Calibri', 15),bg = SAILOR_BLUE, fg = MINT_GREEN)
        self.clock.place(x = WIDTH - (WIDTH / 5), y = (HEIGHT / 10) / 3)
        self.get_time()

        self.contact_label = tk.Label(self.bottom_frame, bg = SAILOR_BLUE, fg = MINT_GREEN ,text = '  Contact me at vladoferko3@gmail.com  \n  or at +421 944 954 513  ')
        self.contact_label.place(x = 15, y = (HEIGHT / 10) / 3)

        self.login_frame = tk.Frame(self.main_frame, width = WIDTH / 3, height = HEIGHT / 1.5, bg = MINT_GREEN)
        self.login_frame.place(x = WIDTH / 2 - (WIDTH / 3) / 2, y = (HEIGHT - (HEIGHT / 1.5)) / 2)

    
    # function which gives me a time

    def get_time(self):
        self.timeVar = time.strftime('%H:%M:%S')
        self.clock.config(text = '  ' + self.timeVar + '                    ')
        self.clock.after(500, self.get_time)



# main window class

class MainWindow(LoginWindow):
    def __init__(self, master):
        super().__init__(master)

    
        

        




win = MainWindow(root)

root.mainloop()

