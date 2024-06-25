import tkinter as tk
from tkinter import ttk
 
window = tk.Tk()
window.title('title')
window.geometry('300x300')
 
string_var = tk.StringVar(value='hello')

label = ttk.Label(master= window,text='something',textvariable= string_var)
label.pack()

entry = ttk.Entry(master=window,textvariable= string_var)
entry.pack()
entry2 = ttk.Entry(master=window,textvariable= string_var)
entry2.pack()


window.mainloop()