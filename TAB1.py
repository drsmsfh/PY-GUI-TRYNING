import tkinter as tk
import ttkbootstrap as ttk  # Ensure ttkbootstrap is installed
import random

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')


# Menu setup
menu = tk.Menu(window)
file_menu = tk.Menu(menu,tearoff= False)
file_menu.add_command(label='open', command=lambda: print('file'))
menu.add_cascade(label="file", menu=file_menu)
# Attach the menu to the window


help_menu = tk.Menu(menu,tearoff= False)
help_menu.add_command(label = 'git help',command = lambda :print('you got help'))
menu.add_cascade(label = 'help', menu = help_menu)
help_var = tk.StringVar()
help_menu.add_checkbutton(label = 'check buton',onvalue='on',offvalue = 'off',variable = help_var)


menu_button = tk.Menubutton(window)
new_menu = tk.Menu(menu_button,tearoff=False)
new_menu.add_command(label = 'test',command = lambda:print('test'))
new_menu.add_cascade(label = 'pris',menu = new_menu)


but_var = tk.StringVar()
menu_button.add_checkbutton(label = 'check buton')
menu_button.config(menu=new_menu)
window.config(menu=menu)
window.mainloop()

