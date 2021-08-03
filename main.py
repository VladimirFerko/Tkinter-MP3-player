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
    login_x_value = (WIDTH / 3) / 10
    entry_width = 25
    def __init__(self, master):
        self.main_frame = tk.Frame(master, width = WIDTH, height = HEIGHT, bg = SAILOR_BLUE)
        self.main_frame.pack()

        self.intro_label = tk.Label(self.main_frame, text = 'Welcome to the MP3 player by vladimirferko', bg = SAILOR_BLUE, fg = MINT_GREEN, font = ('Calibri', 18))
        self.intro_label.place(x = WIDTH / 3.5, y = HEIGHT / 10)

        # bottom frame and its labels, there are clock and contact of this app

        self.bottom_frame = tk.Frame(self.main_frame, width = WIDTH, height = HEIGHT / 10, bg = MINT_GREEN)
        self.bottom_frame.place(x = 0, y = HEIGHT - (HEIGHT / 10))

        self.clock = tk.Label(self.bottom_frame, font = ('Calibri', 15),bg = SAILOR_BLUE, fg = MINT_GREEN)
        self.clock.place(x = WIDTH - (WIDTH / 5), y = (HEIGHT / 10) / 3)
        self.get_time()

        self.contact_label = tk.Label(self.bottom_frame, bg = SAILOR_BLUE, fg = MINT_GREEN ,text = '  Contact me at vladoferko3@gmail.com  \n  or at +421 944 954 513  ')
        self.contact_label.place(x = 15, y = (HEIGHT / 10) / 3)

        # login frame and its entry boxes and so on...

        self.login_frame = tk.Frame(self.main_frame, width = WIDTH / 3, height = HEIGHT / 3, bg = MINT_GREEN)
        self.username_label = tk.Label(self.login_frame, text = 'username : ', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.username_entry = tk.Entry(self.login_frame, width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')
        self.password_label = tk.Label(self.login_frame, text = 'password : ', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.password_entry = tk.Entry(self.login_frame, show = '*' ,width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')
        self.login_button = tk.Button(self.login_frame, text = 'Login', bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')
        self.register_button = tk.Button(self.login_frame, text = "I don't have an accout yet",  bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat', command = self.register_func)

        self.login_frame.place(x = WIDTH / 2 - (WIDTH / 3) / 2, y = (HEIGHT - (HEIGHT / 1.5)) / 2)

        self.login_widget_tuple = (self.username_label, self.username_entry, self.password_label, self.password_entry, self.register_button, self.login_button)
        self.login_entry_tuple = (self.username_entry, self.password_entry)




        for index, item in enumerate(self.login_widget_tuple):
            if index < 4:
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 2.5) / 10) + index * 25)
            else:
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 2.5) / 10) + index * 30)

        # widgets for registrating users

        self.register_frame = tk.Frame(self.main_frame, width = WIDTH / 3, height = HEIGHT / 2, bg = MINT_GREEN)

        self.register_email_label = tk.Label(self.register_frame, text = 'email :', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.register_email_entry = tk.Entry(self.register_frame, width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')

        self.register_name_label = tk.Label(self.register_frame, text = 'username : ', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.register_name_entry = tk.Entry(self.register_frame, width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')

        self.register_password1_label = tk.Label(self.register_frame, text = 'password : ', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.register_password1_entry = tk.Entry(self.register_frame, width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat', show = '*')

        self.register_password2_label = tk.Label(self.register_frame, text = 'repeat your password :', bg = MINT_GREEN, fg = SAILOR_BLUE, font = ('Calibri', 10))
        self.register_password2_entry = tk.Entry(self.register_frame, width = LoginWindow.entry_width, bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat', show = '*')

        self.register_exit_button = tk.Button(self.register_frame, text = 'exit', bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat', command = self.exit_registration_func)
        self.register_confirm_button = tk.Button(self.register_frame, text = 'Confirm registration', bg = SAILOR_BLUE, fg = MINT_GREEN, relief = 'flat')

        self.register_widget_tuple = (self.register_email_label, self.register_email_entry, self.register_name_label, self.register_name_entry, self.register_password1_label, self.register_password1_entry, self.register_password2_label, self.register_password2_entry, self.register_confirm_button, self.register_exit_button)
        self.register_entry_tuple = (self.register_name_entry, self.register_email_entry, self.register_password1_entry, self.register_password2_entry)

    # function which gives me a time

    def get_time(self):
        self.timeVar = time.strftime('%H:%M:%S')
        self.clock.config(text = '  ' + self.timeVar + '                    ')
        self.clock.after(500, self.get_time)

    # function for registrating new users

    def register_func(self):
        self.login_frame.place_forget()
        self.register_frame.place(x = WIDTH / 2 - (WIDTH / 3) / 2, y = (HEIGHT - (HEIGHT / 1.5)) / 2)


        for index, item in enumerate(self.register_widget_tuple):
            if index < 8:
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 2.5) / 10) + index * 25)
            else: 
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 6) / 10) + (index * 28) + 20)

        for item in self.login_entry_tuple:
            item.delete(0, 'end')

    # exit registration function

    def exit_registration_func(self):
        self.register_frame.place_forget()
        self.login_frame.place(x = WIDTH / 2 - (WIDTH / 3) / 2, y = (HEIGHT - (HEIGHT / 1.5)) / 2)
        for index, item in enumerate(self.login_widget_tuple):
            if index < 4:
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 2.5) / 10) + index * 25)
            else:
                item.place(x = LoginWindow.login_x_value , y = ((HEIGHT / 2.5) / 10) + index * 30)
        
        for item in self.register_entry_tuple:
            item.delete(0, 'end')

        



# main window class

class MainWindow(LoginWindow):
    def __init__(self, master):
        super().__init__(master)

    
        

        




login = LoginWindow(root)

root.mainloop()

    