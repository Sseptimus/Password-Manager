import tkinter as tk
from tkinter import *
from random import randint
manager = tk.Tk()
accounts = ["Facebook", "Twitter", "Instagram", "Snapchat", "LinkedIn"]
usernames = ["nick", "joe", "jane", "jim", "joe"]
passwords = ["password", "password", "password", "password", "password"]
def popup(location):  # opens a popup window with the info chosen

    info_window = Toplevel(manager)
    info_window.grab_set()
    info_window.focus_set()
    screen_width = manager.winfo_screenwidth()
    screen_height = manager.winfo_screenheight()
    info_window.configure(background="#0e0118")
    geometry = "400x370+" + \
        str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
    info_window.geometry(geometry)
    info_window.title("View Information")
    account_title = Label(info_window, text="Account:", font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    account_title.place(x=25, y=25)
    account_info = Label(info_window, text=accounts[location], font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    account_info.place(x=25, y=65)
    username_title = Label(info_window, text="Username:", font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    username_title.place(x=25, y=115)
    username_info = Label(info_window, text=usernames[location], font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    username_info.place(x=25, y=155)
    password_title = Label(info_window, text="Password:", font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    password_title.place(x=25, y=205)
    password_info = Label(info_window, text=passwords[location], font=(
        "Arial", 20), fg="#ffffff", background="#0e0118")
    password_info.place(x=25, y=245)

popup(randint(0,len(accounts)-1))

while True:
    manager.update()