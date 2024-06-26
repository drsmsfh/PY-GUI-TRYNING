import tkinter as tk
import ttkbootstrap as ttk
 
window = tk.Tk()
window.title('title')

spin = ttk.Spinbox(master= window,from_=1,to=10)
spin.pack()
spin.bind("<<Increment>>",lambda event:print('up'))
spin.bind("<<Decrement>>",lambda event:print('dawn'))
window.mainloop()