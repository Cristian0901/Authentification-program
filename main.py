import tkinter as tk

import functions as fn

class Program():
    def __init__(self, width:int = 1000, height:int = 500, title:str = "Program"):
        self.size = f"{width}x{height}"
        self.width = width
        self.height = height
        self.title = title
        
        #self.icon = "./program.xbm"
        
        self.win = tk.Tk()
        self.win.title(self.title)
        self.win.geometry(self.size)
        self.win.resizable(False, False)
        #self.win.iconbitmap(self.icon)
        #self.win.iconbitmap(self.icon)
        
        self.login()
        
    def login(self):
        #Clean and create the login page
        for i in self.win.winfo_children():
            i.destroy()
        self.fr_login = tk.Frame(self.win, width=300, height=300)
        self.fr_login.grid(row=0, column=0, sticky="SE")
        
        #Login page
        self.lb_login = tk.Label(self.fr_login, text='Login')
        self.lb_login.grid(row=0, column=0, columnspan=2)
        
        self.lb_name_login = tk.Label(self.fr_login, text='Name:')
        self.lb_name_login.grid(row=1, column=0)
        self.en_name_login = tk.Entry(self.fr_login)
        self.en_name_login.grid(row=1, column=1)
        
        self.lb_password_login = tk.Label(self.fr_login, text='Password:')
        self.lb_password_login.grid(row=2, column=0)
        self.en_password_login = tk.Entry(self.fr_login)
        self.en_password_login.grid(row=2, column=1)
        
        self.lb_error_login = tk.Label(self.fr_login, text="", fg="red")
        self.lb_error_login.grid(row=3, column=0, columnspan=2)
        
        self.btn_register = tk.Button(self.fr_login, text="Register", command=self.register)
        self.btn_register.grid(row=4, column=0)
        
        self.btn_home = tk.Button(self.fr_login, text="SingUp", command=self.fn_singup)#command=self.home)
        self.btn_home.grid(row=4, column=1)
    
    def register(self):
        #Clean and create the register page
        for i in self.win.winfo_children():
            i.destroy()
        self.fr_register = tk.Frame(self.win, width=300, height=300)
        self.fr_register.grid(row=0, column=0)
        
        #Register page
        self.lb_register = tk.Label(self.fr_register, text='Register')
        self.lb_register.grid(row=0, column=0, columnspan=2)
        
        self.lb_name_register = tk.Label(self.fr_register, text='Name:')
        self.lb_name_register.grid(row=1, column=0)
        self.en_name_register = tk.Entry(self.fr_register)
        self.en_name_register.grid(row=1, column=1)
        
        self.lb_password_register = tk.Label(self.fr_register, text='Password:')
        self.lb_password_register.grid(row=2, column=0)
        self.en_password_register = tk.Entry(self.fr_register)
        self.en_password_register.grid(row=2, column=1)
        
        self.lb_error_register = tk.Label(self.fr_register, text="", fg="red")
        self.lb_error_register.grid(row=3, column=0, columnspan=2)
        
        self.btn_register = tk.Button(self.fr_register, text="Register", command=self.fn_register)
        self.btn_register.grid(row=4, column=0)
        
        self.btn_home = tk.Button(self.fr_register, text="Login", command=self.login)
        self.btn_home.grid(row=4, column=1)
    
    def home(self):
        #Clean and create the home page
        for i in self.win.winfo_children():
            i.destroy()
            
        self.fr_home = tk.Frame(self.win, width=300, height=300)
        self.fr_home.grid(row=0, column=0)
        
        #Register page
        self.lb_home = tk.Label(self.fr_home, text='Home')
        self.lb_home.grid(row=0, column=0, columnspan=4)
        
        self.lb_name_home = tk.Label(self.fr_home, text=f"Name: {self.account[1]}")
        self.lb_name_home.grid(row=1, column=0, columnspan=2)
        
        self.lb_password_home = tk.Label(self.fr_home, text=f"Password: {self.account[2]}")
        self.lb_password_home.grid(row=1, column=2, columnspan=2)
        
        self.lb_description_home = tk.Label(self.fr_home, text=f"Description: {self.account[3]}")
        self.lb_description_home.grid(row=2, column=0, columnspan=4, rowspan=2)
        
        self.login_btn = tk.Button(self.fr_home, text="Go to Login", command=self.login)
        self.login_btn.grid(row=4, column=0, columnspan=4)
    
    def run(self):
        fn.connection_db()
        self.win.mainloop()
    
    def fn_singup(self):
        name = self.en_name_login.get()
        password = self.en_password_login.get()
        
        self.account = fn.select_db(name, password)
        #print(type(account))
        if (name == "") or (password == ""):
            self.lb_error_login.config(text="ERROR WITH THE AUTENTIFICATION!")
        else:
            if self.account == ():
                self.lb_error_login.config(text="ERROR WITH THE AUTENTIFICATION!")
            else:
                self.lb_error_login.config(text="")
                self.home()
    
    def fn_register(self):
        name = self.en_name_register.get()
        password = self.en_password_register.get()
        
        #print(name, password)
        #print(type(name))
        #print(type(password))
        
        #raise "Breake out!!"
        
        if (name == "") or (password == ""):
            self.lb_error_register.config(text="ERROR WITH THE AUTENTIFICATION!")
        else:
            self.account = fn.select_db(name, password)
            if self.account != ():
                self.lb_error_register.config(text="ACCOUNT ALREADY CREATED!")
            else:
                fn.insert_db(name, password)
                self.lb_error_register.config(text="ACCOUNT CREATED SUCCESSFULLY")

prog = Program()
prog.run()

fn.end_message()
