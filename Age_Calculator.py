import datetime
import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
window.geometry("500x400")
window.title(" Age Calculator App ")

name = tk.Label(text="Name")
name.grid(column=0, row=1)
year = tk.Label(text="Year")
year.grid(column=0, row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Day")
date.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)

monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        if today.month < self.birthdate.month | ((today.month == self.birthdate.month) & (today.day < self.birthdate.day)):
            return age-1
        else:
            return age


def getInput():
    name = nameEntry.get()
    man = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    textArea = tk.Text(master=window, height=6, width=35)
    textArea.grid(column=1, row=6)

    answer = " Hey, {man}!. You are {age} years old! ".format(man=name, age=man.age())
    textArea.insert(tk.END, answer)


image = Image.open('app_image.jpg')
image.thumbnail((350, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)


button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)

window.mainloop()