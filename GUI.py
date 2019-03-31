from tkinter import *
import func
global info


def rtnkey(event=None):
    func.get_pm25(e.get())


root = Tk()
root.title('pm2.5 for the city')
description1 = Label(root, text='Please input the name of the city below and then click REQUEST button')
description1.pack()

e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)
entry.pack()
entry.bind('<Return>', rtnkey)

root.mainloop()

