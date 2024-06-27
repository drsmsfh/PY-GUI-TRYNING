import tkinter as tk
import ttkbootstrap as ttk
import random

# Initialize the main window
window = tk.Tk()
window.title('Treeview Example')

# Data for populating the Treeview
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# Create the Treeview widget
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack()

# Insert random values into the Treeview
for i in range(100):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    table.insert(parent='', index=0, values=(first_name, last_name, f'{first_name+last_name}@email.com'))

# Function to print selected items
def item_select(event):
    for item in table.selection():
        print(table.item(item)['values'])

# Function to delete selected items
def delete_items(event):
    for item in table.selection():
        table.delete(item)

# Bind selection and delete events
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)
table.bind('<BackSpace>', delete_items)  # Bind Backspace key to delete items

# Run the main event loop
window.mainloop()
