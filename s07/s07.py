import __main__
import tkinter as tk
from tkinter import Tk
from pathlib import Path


# scope
# built in
# global
# non local
# local

# x = 0


# def bt1_command():
#     # print(f"btn1 was fired!")
#     global x
#     x += 1
#     l1.config(text=f"{x}")


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

def save_data(data):
    path = Path(__main__.__file__)
    # print(path.parent)
    data_path = path.parent.joinpath("data")
    data_path.mkdir(mode=0o777, exist_ok=True)
    data_path = data_path.joinpath("data.txt")
    f = open(data_path, "a")
    f.write(str(data))
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


# numbers = [1,5,10]
# names = ["mohammad","ali","reza"]

# for name,number in zip(names,numbers):
#     print(name,number)
# # mohammad 1
# # ali 5
# # reza 10

# for i,number in enumerate(numbers):
#     print(name,number,sep="")
# 0 1
# 1 5
# 2 10

# 2       1           0
# 4       5           2
# 10**2   10**1       10**0

# 10      decimal
# 1010    binary

# 3   2   1   0
# 1   0   1   0
# 2^3 2^2 2^1 2^0
# 8   4   2   1
# 8 + 0 + 2 + 0 = 10

# 973
# 2^9 2^8 2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
# 1   1   1   1   0   0   1   1   0   1

# 973//8 = 121
# 973%8 = 5

# 121//8 = 15
# 121%8 = 1

# 15//8 = 1
# 15%8 = 7

# 1715


# 0123456789 10 11 12 13 14 15
#             a  b  c d  e  f
# a2f
# 15*16^0 + 2*16^1 + 10*16^2 = 2607


# 0o777

# 8^0*7+8^1*7+8^2*7
# 511
# root group  user
# rwx 
# 111  111    111