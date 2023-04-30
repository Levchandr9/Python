import random
import time
from tkinter import *


def bros():
    x = random.choice(['icons\\b.png', 'icons\\b2.png', 'icons\\b3.png',
                       'icons\\b4.png', 'icons\\b5.png', 'icons\\b6.png'])
    return x
def img(event):
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=bros())
        b2 = PhotoImage(file=bros())
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.1)

root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Сделай бросок')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icons\iconka.png'))
font = PhotoImage(file='icons\holst.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
# Button(root, text="Бросок", command=img).pack()
root.bind('<1>', img)
img('event')
root.mainloop()
