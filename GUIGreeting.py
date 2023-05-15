'''
GUI Greeting
Pawelski
5/15/2023
Python II
'''

import tkinter as tk

def display_greeting():
    '''
    Displays a greeting with the user's named filled in.
    '''
    name = name_entry.get()
    if len(name) == 0:
        greeting_label.config(text="Enter your name!")
    else:
        greeting_label.config(text="Hello, " + name)

# Create the window
window = tk.Tk()
window.title("GUI Greeting")

# Create the widgets
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)
display_button = tk.Button(window, text="Display Greeting", command=display_greeting)
greeting_label = tk.Label(window)

# Pack the widgets
name_label.pack()
name_entry.pack()
display_button.pack()
greeting_label.pack()

window.mainloop()