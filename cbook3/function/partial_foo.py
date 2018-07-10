from functools import partial
# import _tkinter
import tkinter

root = tkinter.Tk()

MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='Quit', bg='red', command=root.quit)

b1.pack()
b2.pack()
qb.pack(fill=tkinter.X, expand=True)
root.title('Miclefeng')
root.mainloop()