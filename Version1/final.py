import tkinter as tk
from tkinter import *
from random import *
import json
import math
from functools import partial

login_page = tk.Tk()
login_wallpapers = [r"Password-Generator\Assets\login_wallpapers\cave_edited.png",r"Password-Generator\Assets\login_wallpapers\tower_edited.png"]
headerBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\header_background.png")
tabBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\tab_background.png")
new_password_Background = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\new_password.png")
backGroundImage=PhotoImage(file=choice(login_wallpapers))

with open('Password-Generator\Version1\Password-Generator-Data.json', 'r') as f:
  data = json.load(f)
  
passwords = data[0]
accounts = data[1]
usernames = data[2]
password_labels = []
account_labels = []
username_labels = []
view_buttons = []
tabs = []
show_buttons = []
current_page = 1
total_pages = 0


def setup_manager():
    global manager
    manager = Toplevel(login_page)
    manager.title("Password Manager")
    manager.configure(background="#0e0118")
    manager.bind("<Escape>", lambda event: manager.destroy())
    screen_width = manager.winfo_screenwidth()
    screen_height = manager.winfo_screenheight()
    geometry = "700x500+" + str(int(screen_width/2 - 350)) + "+" + str(int(screen_height/2 - 250))
    manager.geometry(geometry)
    set_tabs()
    header = Label(manager,image=headerBackground, borderwidth=0)
    header.place(x=0,y=0)
    add_password = Button(manager,image=new_password_Background, width=50,height=50,borderwidth=0,command=new_password)
    add_password.place(y=37,x=640)
    next_button = Button(manager,text="→",font=("Arial", 20), background="#0e0118", foreground="#ffffff",command=next_page)
    next_button.place(y=440,x=650)
    previous_button = Button(manager,text="←",font=("Arial", 20), background="#0e0118", foreground="#ffffff",command=previous_page)
    previous_button.place(y=440,x=2)
    
        
def new_password():
    global generate_button, manual_button, account_input, username_input, password_input, new_window
    new_window = Toplevel(manager)
    new_window.grab_set()
    new_window.focus_set()
    screen_width = manager.winfo_screenwidth()
    screen_height = manager.winfo_screenheight()
    geometry = "400x370+" + str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
    new_window.geometry(geometry)
    new_window.title("New Password")
    new_window.configure(background="#0e0118")
    account_name = Label(new_window, text="Account Name:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    account_name.place(x=25,y=25)
    account_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    account_input.place(x=25,y=75)
    username_name = Label(new_window, text="Username:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    username_name.place(x=25,y=125)
    username_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    username_input.place(x=25,y=175)
    password_name = Label(new_window, text="Password:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    password_name.place(x=25,y=225)
    password_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    password_input.place(x=25,y=275)
    done_button = Button(new_window, text="Add password", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command= lambda: new_password_entry())
    done_button.place(x=25,y=325)

    
def next_page():
    global current_page, total_pages
    if current_page == total_pages:
        return
    current_page += 1
    for i in password_labels:
        
        if password_labels.index(i) >= current_page*3-3 and password_labels.index(i) <= current_page*3-1:
            i.place(x=490-36,y=155+(password_labels.index(i)-((current_page-1)*3))*100)
        else:
            i.place(x=1000,y=1000)
    for i in account_labels:
        if account_labels.index(i) >= current_page*3-3 and account_labels.index(i) <= current_page*3-1:
            i.place(x=20,y=155+(account_labels.index(i)-((current_page-1)*3))*100)
        else:
            i.place(x=1000)
    for i in view_buttons:
        if  view_buttons.index(i) >= current_page*3-3 and view_buttons.index(i) <= current_page*3-1:
            i.place(x=540,y=155+(view_buttons.index(i)-((current_page-1)*3))*100)
        else:
            i.place(x=1000)
                            
            
def previous_page():
    global current_page, total_pages
    if current_page == 1:
        return
    current_page -= 1
    for i in password_labels:
        if password_labels.index(i) >= current_page*3-3 and password_labels.index(i) <= current_page*3-1:
            i.place(x=490-36,y=155+(password_labels.index(i)-((current_page-1)*3))*100)
        else:
            i.place(x=1000)
    for i in account_labels:
        if account_labels.index(i) >= current_page*3-3 and account_labels.index(i) <= current_page*3-1:
            i.place(x=20,y=155+(account_labels.index(i)-((current_page-1)*3))*100)
        else:
            i.place(x=1000)
            
            
def manuel_entry():
    global password_input,current_page
    generate_button.place_forget()
    manual_button.place_forget()
    password_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
    password_input.place(x=25,y=275)
    done_button = Button(new_window, text="Add password", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command= new_password_entry)
    done_button.place(x=25,y=325)
    current_page = 1
    for i in password_labels:
        i.place_forget()
    for i in account_labels:
        i.place_forget()
    set_tabs()
    
def set_tabs():
    global total_pages
    total_pages = math.ceil(len(passwords)/3)
    for i in passwords:
        
        if passwords.index(i) < 3:
            tabs.append(Label(manager, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
            tabs[passwords.index(i)].place(x=0,y=125+passwords.index(i)*100)
            account_labels.append(Label(manager, text=accounts[passwords.index(i)],font=("Arial", 20),fg="#ffffff", background="#0e0118"))
            account_labels[passwords.index(i)].place(x=20,y=155+passwords.index(i)*100)
            password_labels.append(Label(manager, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
            view_buttons.append(Button(manager, command= partial(popup,passwords.index(i)),text = "View Password", font=("Arial", 15),background="#0e0118", foreground="#ffffff"))
            view_buttons[passwords.index(i)].place(x=540,y=155+passwords.index(i)*100)
            if len(i) > 6:
                password_labels[-1].config(text="******")
                password_labels[-1].place(x=490-36,y=155+passwords.index(i)*100)
            else:
                password_labels[-1].place(x=490-len(i)*5,y=155+passwords.index(i)*100)
        else: 
            tabs.append(Label(manager, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
            tabs[passwords.index(i)].place(x=700*(total_pages-1),y=125+(passwords.index(i)-(total_pages*3))*100)
            account_labels.append(Label(manager, text=accounts[passwords.index(i)],font=("Arial", 20),fg="#ffffff", background="#0e0118"))
            account_labels[passwords.index(i)].place(x=700*(total_pages-1)+20,y=155+(passwords.index(i)-(total_pages*3))*100)
            password_labels.append(Label(manager, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
            view_buttons.append(Button(manager,command= partial(popup,passwords.index(i)),text = "View Password", font=("Arial", 15),background="#0e0118", foreground="#ffffff"))
            view_buttons[passwords.index(i)].place(x=540,y=155+(passwords.index(i)-(total_pages*3))*100)
            if len(i) > 6:
                password_labels[-1].config(text="******")
                password_labels[-1].place(x=490-36+700*(total_pages-1),y=155+(passwords.index(i)-(total_pages*3))*100)
            else:
                password_labels[-1].place(x=490-len(i)*5+700*(total_pages-1),y=155+(passwords.index(i)-(total_pages*3))*100)

    
def new_password_entry():
    passwords.append(password_input.get())
    accounts.append(account_input.get())
    usernames.append(username_input.get())
    data[0] = passwords
    data[1] = accounts
    data[2] = usernames
    with open('Password-Generator\Version1\Password-Generator-Data.json', 'w') as outfile:
        json.dump(data, outfile)
    tabs.append(Label(manager,width=700,height=100, image = tabBackground,borderwidth=0))
    account_labels.append(Label(manager, text=account_input.get(),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
    if len(password_input.get()) > 6:
        password_labels.append(Label(manager, text="******",font=("Arial", 20),fg="#ffffff", background="#0e0118"))
    else:
        password_labels.append(Label(manager, text=len(password_input.get())*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
    new_window.destroy()

def popup(location):
    
    info_window = Toplevel(manager)
    info_window.grab_set()
    info_window.focus_set()
    screen_width = manager.winfo_screenwidth()
    screen_height = manager.winfo_screenheight()
    info_window.configure(background="#0e0118")
    geometry = "400x370+" + str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
    info_window.geometry(geometry)
    info_window.title("View Information")
    account_title = Label(info_window, text="Account:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
    account_title.place(x=25,y=25)
    account_info = Label(info_window, text=accounts[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
    account_info.place(x=25,y=65)
    username_title = Label(info_window, text="Username:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
    username_title.place(x=25,y=115)
    username_info = Label(info_window, text=usernames[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
    username_info.place(x=25,y=155)
    password_title = Label(info_window, text="Password:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
    password_title.place(x=25,y=205)
    password_info = Label(info_window, text=passwords[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
    password_info.place(x=25,y=245)
    
def login():
    global password_entry, username_entry
    login_page.title('Password Manager')
    login_page.configure(background='black')
    screen_width = login_page.winfo_screenwidth()
    screen_height = login_page.winfo_screenheight()
    geometry = "500x500+" + str(int(screen_width/2 - 250)) + "+" + str(int(screen_height/2 - 250))
    login_page.geometry(geometry)
    login_wallpaper = Label(login_page,image=backGroundImage)
    login_wallpaper.place(x=-2,y=-2)
    username_label = Label(login_page,text="Username:",bg='black',fg='white',font=('Arial',20))
    username_label.place(x=150,y=140)
    username_entry = Entry(login_page,width=20,font=('Arial',15))
    username_entry.place(x=150,y=185)
    password_label = Label(login_page,text="Password:",bg='black',fg='white',font=('Arial',20))
    password_label.place(x=150,y=250)
    password_entry = Entry(login_page,width=20,font=('Arial',15),show="*")
    password_entry.place(x=150,y=295)
    enter_button = Button(login_page,text="Enter",font=("Arial", 15), background="#0e0118", foreground="#ffffff",command=login_check)
    enter_button.place(x=150,y=330)
    login_page.bind("<Escape>", lambda event: login_page.destroy())

def login_check():
    username = username_entry.get()
    password = password_entry.get()
    if username.lower() == "admin" and password == "password":
        login_page.withdraw()
        setup_manager()

    else:
        
        login_page.messagebox.showerror(title="Error",message="Incorrect Username or Password")
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        
if __name__ == "__main__":
    login()
    login_page.mainloop()