import tkinter as tk
from tkinter import messagebox
import sqlite3

def login():
    username = ent_username.get()
    password = ent_password.get()
    db_address = 's11/db.sqlite3'
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    result = cursor.execute(
        'select * from user where username=? and password=?',
        (username,password)).fetchone()
    connection.commit()
    connection.close()
    if result is None:
        messagebox.showerror("faild","username or password is wrong")
    else:
        messagebox.showinfo("success","welcome")

    print(result)

window = tk.Tk()

lbl_usename = tk.Label(master=window,text='username')
lbl_password = tk.Label(master=window,text='password')
ent_username = tk.Entry(master=window)
ent_password = tk.Entry(master=window)
btn_login=tk.Button(master=window,text='login',command=login)
lbl_usename.pack()
ent_username.pack(fill=tk.X)
lbl_password.pack()
ent_password.pack(fill=tk.X)
btn_login.pack()

window.mainloop()