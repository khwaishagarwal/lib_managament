import tkinter as tk
import mysql.connector
from tkinter import messagebox

#The initial login window responsible for getting credentials as well as
#instantiating the DB connection

class login:
    def __init__(self):
        print(f"Window initialised: {self}")
        self.root = tk.Tk()
        self.root.geometry("340x450")
        self.root.resizable = False
        self.root.title("Enter Creds")
        self.return_vals = [] #trying a solution for the error around #50
		
        self.uname = tk.Label(self.root, text="Username:")
        self.passw = tk.Label(self.root, text="Password:")
        self.uname_enter = tk.Entry(self.root)
        self.passw_enter = tk.Entry(self.root, show="*")
        self.submit = tk.Button(self.root, text="Submit", command=self.check)
        self.db = tk.Label(self.root, text="Database:")
        self.db_enter = tk.Entry(self.root)
        self.table = tk.Label(self.root, text="Table:")
        self.table_enter = tk.Entry(self.root)

        self.uname.grid(pady=10, padx=10)
        self.uname_enter.grid(pady=10, padx=35)
        self.passw.grid(pady=10, padx=10)
        self.passw_enter.grid(pady=10, padx=35)
        self.db.grid(pady=10, padx=10)
        self.db_enter.grid(pady=10, padx=35)
        self.table.grid(pady=10, padx=10)
        self.table_enter.grid(pady=10, padx=35)
        self.submit.grid(pady=10, padx=40)
        self.root.mainloop()

    def check(self):
        print(f"DBG: check() called")
        try:
            connector = mysql.connector.connect(host="127.0.0.1", user=self.uname_enter.get(), password=self.passw_enter.get())
            self.return_vals = [connector, self.db_enter.get(), self.table_enter.get()]
            self.root.quit()
            #IF SUCCESSFUL WILL SET
        except:
            print(f"DBG: Value from uname_enter: {self.uname_enter.get()}, passw_enter: HIDDEN FROM RELEASE VER, db_enter: {self.db_enter.get()}, table_enter: {self.table_enter.get()}")
            messagebox.showerror("Fatal", "Error. Either invalid creds, or MySQL daemon not running")
            self.root.quit()
            raise ValueError
            #IF UNSUCCESSFUL ERROR WILL BE RAISED
    # def close(self):
    #     print("DBG: close called")
    #     self.root.quit()
    #doesnt work for whatever reason
