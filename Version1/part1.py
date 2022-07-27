import tkinter as tk
from tkinter import *
from random import *

login_wallpapers = [r"Password-Generator\Assets\login_wallpapers\cave_edited.png",r"Password-Generator\Assets\login_wallpapers\tower_edited.png"]
page=tk.Tk()
backGroundImage=PhotoImage(file=choice(login_wallpapers))
def login(login_page):
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
        print("access granted")
    else:
        print("access denied")
if __name__ =="__main__":
    login(page)
    page.mainloop()
    
    
