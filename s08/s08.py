import csv
from pathlib import Path

import tkinter as tk
from tkinter import Tk
from tkinter import messagebox

labes = []
entries = []

def btn_submit_callback():
    person = {}
    person["id"] = entries[0].get()
    person["name"] = entries[1].get()
    person["age"] = entries[2].get()
    # print(person)
    if save_data(person):
        for e in entries:
            e.delete(0, tk.END)
            e.insert(0, "")
        messagebox.showinfo("save","data was saved successfully!")

def save_data(data:dict):
    path = Path(__file__)
    # print(path.parent)
    data_path = path.parent.joinpath("data")
    data_path.mkdir(mode=0o777, exist_ok=True)
    data_path = data_path.joinpath("data.csv")
    with open(data_path, "a") as f:
        w = csv.DictWriter(f,["id","name","age"])
        w.writerow(data)
    return True

def setup():
    frame = tk.Frame(
        master=main_window,
        relief=tk.RAISED,
        padx=30,
        pady=30,
        borderwidth=3)

    lable_text = ["id", "name", "age"]
    # labes = []
    # entries = []
    for i in range(3):
        labes.append(tk.Label(master=frame, text=lable_text[i]))
        entries.append(tk.Entry(master=frame))

    for i, l in enumerate(labes):
        l.grid(column=0, row=i)

    for i, e in enumerate(entries):
        e.grid(column=1, row=i)

    btn_submit = tk.Button(master=frame, text="submit",
                           command=btn_submit_callback)
    btn_submit.grid(column=0, row=3, columnspan=2)
    frame.pack()


main_window = Tk()
main_window.geometry("800x600")
setup()
main_window.mainloop()

