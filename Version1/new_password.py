import tkinter as tk
from tkinter import *
import json

manager = tk.Tk()
passwords = ["password", "password2", "password3"]
usernames = ["username", "username2", "username3"]
accounts = ["account", "account2", "account3"]
tabs = []
with open('Password-Generator\Version1\Password-Generator-Data.json', 'r') as f:
    data = json.load(f)
    

def new_password(): 
    # Creates window for adding new password, does not return
    global generate_button, manual_button, account_input, username_input, password_input, new_window
    new_window = Toplevel(manager)
    new_window.grab_set()
    new_window.focus_set()
    screen_width = manager.winfo_screenwidth()
    screen_height = manager.winfo_screenheight()
    geometry = "400x370+" + \
        str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
    new_window.geometry(geometry)
    new_window.title("New Password")
    new_window.configure(background="#0e0118")
    account_name = Label(new_window, text="Account Name:", font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    account_name.place(x=25, y=25)
    account_input = Entry(new_window, width=30, font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    account_input.place(x=25, y=75)
    username_name = Label(new_window, text="Username:", font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    username_name.place(x=25, y=125)
    username_input = Entry(new_window, width=30, font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    username_input.place(x=25, y=175)
    password_name = Label(new_window, text="Password:", font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    password_name.place(x=25, y=225)
    password_input = Entry(new_window, width=30, font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff")
    password_input.place(x=25, y=275)
    done_button = Button(new_window, text="Add password", font=(
        "Arial", 15), background="#0e0118", foreground="#ffffff", command=lambda: new_password_entry())
    done_button.place(x=25, y=325)
    
def new_password_entry():
    # will be done in main file
    ...