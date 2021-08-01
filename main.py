import tkinter as tk
from pygame import mixer  
import psycopg2
import os
import os.path

# variables for main window size (pixels)

HEIGHT = '800'
WIDTH = '1200'

# image paths

MAIN_ICON = os.path.join('/','home', 'vladimir','Documents','programming','mp3player','pictures', 'main_icon3.png')

# colors 

ROYAL_BLUE = '#3366ff'
WHITE = '#ffffff'

# main window options

root = tk.Tk()
root.title('MP3 player by vladimirferko')
root.geometry('{}x{}'.format(WIDTH, HEIGHT))
root.configure(bg = WHITE)
root.resizable(0,0)

img = tk.PhotoImage(file= MAIN_ICON)
root.tk.call('wm', 'iconphoto', root._w, img)

# login / register interface
class LoginWindow:
    def __init__(self, master):
        self.main_frame = tk.Frame(master)
        self.main_frame.pack()



# main window class

class MainWindow(LoginWindow):
    def __init__(self, master):
        super().__init__(master)
        

        




win = MainWindow(root)

root.mainloop()

