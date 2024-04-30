#SETS UP THE DATABASE AND TABLE
#ONLY FOR RUNNING ONE TIME
from tkinter import messagebox
import mysql.connector
import init

def main():
	win = init.login()
	temp = win.return_vals
	win.root.quit()

	con = temp[0]
	db = temp[1]
	table = temp[2]
		
	try:
		cur = con.cursor()
		cur.execute(f"CREATE DATABASE {db};")
		con.commit()
	except:
		messagebox.showerror("Fatal Error", "Couldnt create database")
		return 0
	try:
		cur.execute(f"USE {db};")
		cur.execute(f"CREATE TABLE {table}(name VARCHAR(255), code BIGINT, author VARCHAR(255), available BOOL);")
		con.commit()
	except:
		messagebox.showerror("Fatal Error", "Couldnt create table")
		return 0
	print(f"Database {db} and table {table} have been setup and are ready for use")

main()		
