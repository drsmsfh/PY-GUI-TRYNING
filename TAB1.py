import tkinter as tk
from tkinter import ttk  # Corrected the typo from tkk to ttk

def convert():
    # Get the input value and convert it to integer
    try:
        miles_input = int(entry_int.get())
        # Convert miles to kilometers
        klm_output = miles_input * 1.6
        # Set the output string variable to the result
        output_str.set(klm_output)
    except ValueError:
        # Handle invalid input
        output_str.set("Invalid input")

# Create a window
window = tk.Tk()
window.title('demo')
window.geometry('300x150')

# Create and pack the label
window_label = ttk.Label(master=window, text='miles to kms', font='Calibri 14 bold')
window_label.pack()

# Create and pack the input frame
input_frame = ttk.Frame(master=window)
# Instantiate IntVar for the entry field
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
# Create the button and set the command to the convert function
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left')
button.pack(side='left', padx=5)
input_frame.pack(pady=10)

# Instantiate StringVar for the output label
output_str = tk.StringVar()
output_label = ttk.Label(master=window, text='output', font='Calibri 10', textvariable=output_str)
output_label.pack()

# Run the Tkinter event loop
window.mainloop()


