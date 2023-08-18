import tkinter as tk
from tkinter import Tk
from tkinter import Label,Button
from tkinter import filedialog
from PIL import ImageTk, Image  

def btn1_command():
    print("btn1")
    path = filedialog.askopenfile()
    # path.write("data")
    print(path)

window = Tk()
image1 = Image.open("toy.png")
test = ImageTk.PhotoImage(image1)

# l1 = Label(master=window,image=test)
# l1.grid()
btn1 = Button(master=window,text="profile picture",command=btn1_command)
btn1.pack()
window.mainloop()