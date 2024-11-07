from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("400x500")

class arithmetic:
    def __init__(self,firstNum,secondNum):
        self.firstNum = firstNum
        self.secondNum = secondNum

    def add(self):
        addition = self.firstNum + self.secondNum
        messagebox.showinfo("add", addition)

    def sub(self):
        sub = self.firstNum - self.secondNum
        messagebox.showinfo("subraction", sub)

    def multi(self):
        mul = self.firstNum * self.secondNum
        messagebox.showinfo("Multiplication", mul)

    def divide(self):
        div = self.firstNum / self.secondNum
        messagebox.showinfo("Division", div)

    def moduless(self):
        mod = self.firstNum % self.secondNum
        messagebox.showinfo("Modules", mod)

    def powerof(self):
        power_of = (self.firstNum) ** (self.secondNum)

        messagebox.showinfo("Power of", power_of)

        print(power_of)
    def floordivision(self):
        floor = self.firstNum // self.secondNum
        messagebox.showinfo("floordivision", floor)




def add():
    firstnum = int(e1.get())
    secnum= int(e2.get())
    obj = arithmetic(firstnum,secnum)
    obj.add()

def sub():
    firstNum = int(e1.get())
    secondNum = int(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.sub()

def multi():
    firstNum = int(e1.get())
    secondNum = int(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.multi()


def divide():
    firstNum = float(e1.get())
    secondNum = float(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.divide()

def moduless():
    firstNum = int(e1.get())
    secondNum = int(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.sub()

def powerof():
    firstNum = int(e1.get())
    secondNum = int(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.powerof()

def floordivision():
    firstNum = int(e1.get())
    secondNum = int(e2.get())
    obj = arithmetic(firstNum, secondNum)
    obj.floordivision()


l1=Label(win, text="Enter a Numbers")
l1.grid(row=0, column=0)
e1 = Entry(win)
e1.grid(row=1, column=0)
e2 = Entry(win)
e2.grid(row=1, column=1)

b1=Button(win, text="Add(+)", command=add)
b1.grid(row=2, column=0)
b2 = Button(win, text="Sub(-)", command=sub)
b2.grid(row=2, column=1)
b3 = Button(win, text= "Multiple(*)", command=multi)
b3.grid(row=3, column=0)
b4 = Button(win, text= "Divide(/)", command=divide)
b4.grid(row=3, column=1)
b5 = Button(win, text= "modules(%)", command=moduless)
b5.grid(row=4, column=0)
b6 = Button(win, text= "Power(**)", command=powerof)
b6.grid(row=4, column=1)
b7 = Button(win, text= "Floor Division(//)", command=floordivision)
b7.grid(row=5, column=0)

win.mainloop()