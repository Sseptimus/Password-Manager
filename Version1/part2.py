from tkinter import *
from pynput import mouse
import json
from time import sleep

with open('Password-Generator\Version1\Password-Generator-Data.json', 'r') as f:
  data = json.load(f)
  
passwords = data[0]
accounts = data[1]
usernames = data[2]
password_labels = []
account_labels = []
username_labels = []
tabs = []
positions = []
positions_account = []
positions_password = []

def on_scroll(x,y,dx,dy):
    if focus_check:
        if positions[len(positions)-1][1]+dy*10 >= 400 and positions[0][1]+dy*10 <= 125:
            for i in tabs:
                tabs[tabs.index(i)].place(y=positions[tabs.index(i)][1]+dy*5)
                positions[tabs.index(i)][1] += dy*5
            for i in accounts:
                account_labels[accounts.index(i)].place(y=positions_account[accounts.index(i)][1]+dy*5)
                positions_account[accounts.index(i)][1] += dy*5
        elif positions[len(positions)-1][1]+dy*10 > 400:
            for i in tabs:
                tabs[tabs.index(i)].place(y=125+tabs.index(i)*100)
                positions[tabs.index(i)][1] = 125+tabs.index(i)*100
            for i in accounts:
                account_labels[accounts.index(i)].place(y=155+accounts.index(i)*100)
                positions_account[accounts.index(i)][1] = 155+accounts.index(i)*100
        else:
            for i in tabs:
                if len(tabs) < 4:
                    tabs[tabs.index(i)].place(y=100+tabs.index(i)*100)
                    positions[tabs.index(i)][1] = 100+tabs.index(i)*100
                else:
                    tabs[tabs.index(i)].place(y=100+tabs.index(i)*100-(len(tabs)-4)*100)
                    positions[tabs.index(i)][1] = 100+tabs.index(i)*100-(len(tabs)-4)*100
            for i in accounts:
                if len(tabs) < 4:
                    account_labels[accounts.index(i)].place(y=130+accounts.index(i)*100)
                    positions_account[accounts.index(i)][1] = 130+accounts.index(i)*100
                else:
                    account_labels[accounts.index(i)].place(y=130+accounts.index(i)*100-(len(tabs)-4)*100)
                    positions_account[accounts.index(i)][1] = 130+accounts.index(i)*100-(len(tabs)-4)*100
            for i in passwords:
                if len(tabs) < 4:
                    password_labels[passwords.index(i)].place(y=155+passwords.index(i)*100)
                    positions_password[passwords.index(i)][1] = 155+passwords.index(i)*100
        # sleep(0.00001) 
            


listener = mouse.Listener(on_scroll=on_scroll)
listener.start()
class Page(Tk):
    def setup(self):
        global focus_check,tabBackground,pages
        pages = self
        self.title("Password Manager")
        self.configure(background="#0e0118")
        self.bind("<Escape>", lambda event: self.destroy())
        focus_check = BooleanVar()
        self.bind('<FocusIn>', lambda _: focus_check.set(True))
        self.bind('<FocusOut>', lambda _: focus_check.set(False))
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        geometry = "700x500+" + str(int(screen_width/2 - 350)) + "+" + str(int(screen_height/2 - 250))
        self.geometry(geometry)
        self.headerBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\header_background.png")
        tabBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\tab_background.png")
        self.set_tabs(True)
        self.header = Label(self,image=self.headerBackground, borderwidth=0)
        self.header.place(x=0,y=0)
        self.newBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\new_password.png")
        self.add_password = Button(self,image=self.newBackground, width=50,height=50,borderwidth=0,command=self.new_password)
        self.add_password.place(y=37,x=530)
            
    def new_password(self):
        global generate_button, manual_button, account_input, username_input, password_input, new_window
        new_window = Toplevel(self)
        new_window.grab_set()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
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
        generate_button = Button(new_window, text="Generate Password", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        generate_button.place(x=25,y=275)
        manual_button = Button(new_window, text="Manual Entry", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command=lambda: Page.manuel_entry(Page))
        manual_button.place(x=225,y=275)
        
        
    def manuel_entry(self):
        global password_input
        generate_button.place_forget()
        manual_button.place_forget()
        password_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        password_input.place(x=25,y=275)
        done_button = Button(new_window, text="Add password", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command= lambda: Page.new_password_entry())
        done_button.place(x=25,y=325)

    def set_tabs(a,b):
        print(len(passwords))
        if b:
            for i in passwords:
                tabs.append(Label(pages, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
                tabs[passwords.index(i)].place(x=0,y=125+passwords.index(i)*100)
                positions.append([0,125+passwords.index(i)*100])
            for i in accounts:
                account_labels.append(Label(pages, text=i,font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                account_labels[accounts.index(i)].place(x=20,y=155+accounts.index(i)*100)
                positions_account.append([20,155+accounts.index(i)*100])
            for i in passwords:
                password_labels.append(Label(pages, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                
                if len(i) > 6:
                    password_labels[-1].config(text="******")
                    password_labels[-1].place(x=550-36,y=155+passwords.index(i)*100)
                    positions_password.append([550-36,155+passwords.index(i)*100])
                else:
                    password_labels[-1].place(x=550-len(i)*5,y=155+passwords.index(i)*100)
                    positions_password.append([550-len(i)*5,155+passwords.index(i)*100])
        if not b:
            for i in passwords:
                tabs[passwords.index(i)].place(x=0,y=125+passwords.index(i)*100)
                positions[passwords.index(i)][1] = 125+passwords.index(i)*100
                positions[passwords.index(i)][0] = 0
                password_labels.append(Label(pages, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                if len(i) > 6:
                    password_labels[-1].config(text="******")
                    password_labels[-1].place(x=550-36,y=155+passwords.index(i)*100)
                    positions_password.append([550-36,155+passwords.index(i)*100])
                else:
                    password_labels[-1].place(x=550-len(i)*5,y=155+passwords.index(i)*100)
                    positions_password.append([550-len(i)*5,155+passwords.index(i)*100])
        
        
    def new_password_entry():
        passwords.append(password_input.get())
        accounts.append(account_input.get())
        usernames.append(username_input.get())
        tabs.append(Label(pages, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
        tabs[-1].place(x=0,y=125+(len(passwords)-1)*100)
        positions.append([0,125+(len(passwords)-1)*100])
        account_labels.append(Label(pages, text=account_input.get(),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
        account_labels[-1].place(x=20,y=155+(len(passwords)-1)*100)
        positions_account.append([20,155+(len(passwords)-1)*100])
        pages.set_tabs(False)
        new_window.destroy()
        
if __name__ == "__main__":
    page = Page()
    page.setup()
    page.mainloop()
    listener.join()
    