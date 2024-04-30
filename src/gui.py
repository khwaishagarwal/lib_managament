import tkinter as tk
from tkinter import ttk #To provide better integrated widgets
from tkinter import messagebox
import mysql.connector
#IGNORE ALL PRINT FUNCTIONS THEY ARE FOR DEBUGGING PURPOSES ONLY

class Window:
    #TODO: fix button commands to accept functions with args
    #DONE, I think
    def __init__(self, con, database, table): #initialiser
        self.cursor = con.cursor() #SQL stuff
        self.con = con
        self.database = database
        self.table = table

        #Front end stuff -->
        self.root = tk.Tk() #Root window
        print(f"DBG: Window initialised: {self} with arg: {con}")
        self.root.title("SQL")
        self.root.geometry("600x850")
        self.root.resizable = False
        self.setup()
        self.root.mainloop()

    def setup(self):
        #Supposed to create the widgets and pack them
        print(f"DBG: Setup called")
        #Element query -->
        self.label1 = ttk.Label(self.root, text="Lookup Entry:")
        self.lookupCode = tk.Entry(self.root)
        self.lookupEntry = tk.Entry(self.root)
        self.searchCode = tk.Button(self.root, text="Code", command=self.query_code)
        self.search = ttk.Button(self.root, text="Name", command=self.query)
        #Add row -->
        self.label2 = ttk.Label(self.root, text="Add Entry:")
        
        self.book_name = ttk.Label(self.root, text="Book Name:")
        self.bname_entry = tk.Entry(self.root)
        
        self.book_code = ttk.Label(self.root, text="Code Number:")
        self.bcode_entry = tk.Entry(self.root)

        self.book_author = ttk.Label(self.root, text="Author:")
        self.bauthor_entry = tk.Entry(self.root)

        self.book_available = ttk.Label(self.root, text="Available: ")
        self.bavail_entry = tk.Entry(self.root)
        
        self.book_submit = tk.Button(self.root, text="Submit", command=self.submit)
		
        self.label1.grid(padx=10, pady=10)
        self.lookupEntry.grid(padx=10, pady=10)
        self.lookupCode.grid(padx=10, pady=10)
        self.search.grid(padx=10, pady=10)
        self.searchCode.grid(padx=10, pady=10)
        self.label2.grid(padx=10, pady=10)
        self.book_name.grid(padx=10, pady=10)
        self.bname_entry.grid(padx=10, pady=10)
        self.book_code.grid(padx=10, pady=10)
        self.bcode_entry.grid(padx=10, pady=10)
        self.book_author.grid(padx=10, pady=10)
        self.bauthor_entry.grid(padx=10, pady=10)
        self.book_available.grid(padx=10, pady=10)
        self.bavail_entry.grid(padx=10, pady=10)
        self.book_submit.grid(padx=10, pady=10)
        #DB stats -->
        self.stat_label = ttk.Label(self.root, text="Show Status:")
        self.stat_but = tk.Button(self.root, text="Show", command=self.stats)
        self.stat_label.grid(padx=10, pady=10, row=0, column=1)
        self.stat_but.grid(padx=10, pady=10, row=1, column=1)
        #Entry remove
        self.label3 = ttk.Label(self.root, text="Remove Entry:")
        self.remove = ttk.Label(self.root, text="Enter Code:")
        self.remove_entry = tk.Entry(self.root)
        self.remove_but = tk.Button(self.root, text="Remove", command=self.delete)
        self.label3.grid(padx=10, pady=10, column=1, row=3)
        self.remove.grid(padx=10, pady=10, column=1, row=4)
        self.remove_entry.grid(padx=10, pady=10, column=1, row=5)
        self.remove_but.grid(padx=10, pady=10, column=1, row=6)

        self.label4 = ttk.Label(self.root, text="Toggle availability:")
        self.toggle = ttk.Label(self.root, text="Enter Code:")
        self.toggle_entry = tk.Entry(self.root)
        self.toggle_but = tk.Button(self.root, text="Toggle", command=self.toggle_av)
        self.label4.grid(padx=10, pady=10, column=1, row=8)
        self.toggle.grid(padx=10, pady=10, column=1, row=9)
        self.toggle_entry.grid(padx=10, pady=10, column=1, row=10)
        self.toggle_but.grid(padx=10, pady=10, column=1, row=11)

        self.setup_db()

    def setup_db(self):
        print(f"DBG: Setup DB called with args: {self.table}")
        try:
            self.cursor.execute(f"USE {self.database}")
        except:
            print("DBG: Required DB does not exist")
            messagebox.showerror("Fatal", "Required Database does not exist")
            self.root.quit()

        self.cursor.execute("SHOW TABLES")
        if self.table in self.cursor.fetchone():
            print(f"DBG: Found table {self.table}")
        else:
            messagebox.showerror("Fatal", f"Couldnt find table {self.table}")
            self.root.quit()

    def query(self): #default only temporary till TODO:8 is done
        #DONE more or less
        print("DBG: query called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupEntry.get()
        print(f"DBG: Value returned from self.lookupEntry: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox
        #DONE
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE name = \"{self.lookupEntry.get()}\"")
        temp = self.cursor.fetchone()
        print(f"DBG: temp = {temp}")
        try:
            msg = f" Name: {temp[0]}\n Code: {temp[1]}\n Author: {temp[2]}\n Available: {bool(temp[3])}\n"
        except:
            msg = "Not found"
        messagebox.showinfo("Search", msg)

    def query_code(self):
        print("DBG: query_code called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupCode.get()
        print(f"DBG: Value returned from self.lookupCode: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox
        #DONE
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE code = {temp};")
        temp = self.cursor.fetchone()
        print(f"DBG: temp = {temp}")
        try:
            msg = f" Name: {temp[0]}\n Code: {temp[1]}\n Author: {temp[2]}\n Available: {bool(temp[3])}\n"
        except:
            msg = "Not found"
        messagebox.showinfo("Search", msg)

    def submit(self):
        #Supposed to verify input fields and create a new entry
        #in the database
        print(f"DBG: submit called")

        name = self.bname_entry.get()
        code = self.bcode_entry.get()
        author = self.bauthor_entry.get()
        available = self.bavail_entry.get()

        print(f"DBG: Value returned from self.bname_entry: {name}, self.bcode_entry: {code}, self.bauthor_entry: {author}, self.bavail_entry: {available}")

        #TODO: Make it verify and submit the entries
        #DONE
        try:
            int(code)
        except:
            print("DBG: Invalid values entered in self.bcode_entry")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the code box")
            return 0
        try:
            bool(available)
        except:
            print("DBG: Invalid values entered in self.bavail_entry")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the available box(0/1)")
            return 0
        if name.isspace() or author.isspace():
            print("DBG: Boxes cannot be empty")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the boxes")
            return 0
        else:
            try:
                s = f"INSERT INTO {self.table} VALUES (\"{name}\", {code}, \"{author}\", {available});" 
                self.cursor.execute(s)
                self.con.commit()
                messagebox.showinfo("Successful", "Row Successfully added into the table")
            except:
                print("DBG: Couldn't add row to DB")
                messagebox.showerror("Error", "Couldn't insert row into the database")
                return 0

    def stats(self):
        print(f"DBG: stats called with args table: {self.table}")
        try:
            self.cursor.execute(f"SELECT * FROM {self.table}")
            temp = self.cursor.fetchall()
            #Counting available books
            available_books = 0
            for i in temp:
                if i[3] == 1:
                    available_books += 1

            messagebox.showinfo("Status", f"No. of books: {len(temp)}\nBooks Available: {available_books}")
        except:
            print("DBG: Error while trying to communicate with server")
            messagebox.showerror("Error", "Couldnt communicate with the server")
            return 0

    def delete(self):
        print("DBG: remove called")
        temp = self.remove_entry.get()
        print(f"DBG: Value returned from self.remove_entry: {self.remove_entry.get()}")
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE code = {self.remove_entry.get()};")
        temp = self.cursor.fetchone()
        print(f"DBG: temp = {temp}")
        try:
            msg = f" Name: {temp[0]}\n Code: {temp[1]}\n Author: {temp[2]}\n Available: {bool(temp[3])}\n"
            ques = messagebox.askyesno("Confirm", f"{msg}\nReally remove this book?")
            try:
                if ques:
                    print("DBG: Returned True")
                    cmd = f"DELETE FROM {self.table} WHERE code = {self.remove_entry.get()};"
                    print(cmd)
                    self.cursor.execute(cmd)
                    self.con.commit()
                    return 0
                else:
                    print("DBG: Returned false")
                    return 0
            except:
                messagebox.showerror("Error", "Couldn't delete entry")
                return 0
        except:
            msg = "Not found"
            messagebox.showinfo("Search", msg)

    def toggle_av(self):
        print("DBG: toggle_av called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        code = self.toggle_entry.get()
        print(f"DBG: Value returned from self.toggle_entry: {code}")

        self.cursor.execute(f"SELECT * FROM {self.table} WHERE code = {code};")
        temp = self.cursor.fetchone()
        print(f"DBG: temp = {temp}")
        try:
            msg = f" Name: {temp[0]}\n Code: {temp[1]}\n Author: {temp[2]}\n Available: {bool(temp[3])}\n"
            try:
                ques = messagebox.askyesno("Confirm", f"{msg}\nReally toggle the availability?")
                if ques:
                    self.cursor.execute(f"DELETE FROM {self.table} WHERE code = {code};")
                    self.con.commit()
                    if bool(temp[3]):
                        self.cursor.execute(f"INSERT INTO {self.table} VALUES (\"{temp[0]}\", {temp[1]}, \"{temp[2]}\", 0);")
                        self.con.commit()
                        messagebox.showinfo("Successful", "Book is unavailable now")
                    else:
                        self.cursor.execute(f"INSERT INTO {self.table} VALUES (\"{temp[0]}\", {temp[1]}, \"{temp[2]}\", 1);")
                        self.con.commit()
                        messagebox.showinfo("Successful", "Book is available now")

            except:
                print(f"DBG: Errored out") 
                messagebox.showerror("Error", "Couldnt toggle")
        except:
            msg = "Not found"
            messagebox.showinfo("Search", msg)