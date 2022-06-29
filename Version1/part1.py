from tkinter import *
from random import *

login_wallpapers = ["Password-Generator\Assets\login_wallpapers\cave_edited_2.png",r"Password-Generator\Assets\login_wallpapers\tower_edited.png"]
class Login(Tk):
    def setup(self):
        self.title('Password Manager')
        self.configure(background='black')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        geometry = "500x500+" + str(int(screen_width/2 - 250)) + "+" + str(int(screen_height/2 - 250))
        self.geometry(geometry)
        self.backGroundImage=PhotoImage(file=choice(login_wallpapers))
        self.login_wallpaper = Label(self,image=self.backGroundImage)
        self.login_wallpaper.place(x=-2,y=-2)
        self.username_entry = Entry(self,width=20,font=('Times New Roman',15))
        self.username_entry.place(x=150,y=185)
        self.password_entry = Entry(self,width=20,font=('Times New Roman',15),show="*")
        self.password_entry.place(x=150,y=295)
        self.enter_button = Button(self,text="Enter",width=10,height=2,font=('Times New Roman',15),command=self.login)
        self.enter_button.place(x=150,y=400)
        self.bind("<Escape>", lambda event: self.destroy())
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username.lower() == "admin" and password == "password":
            print("access granted")
        else:
            print("access denied")
if __name__ =="__main__":
    login_page = Login()
    login_page.setup()
    
while True:
    login_page.update()
