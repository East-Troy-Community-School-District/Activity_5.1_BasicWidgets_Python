'''
GUI Rectangle Area
Pawelski
5/15/2023
Python II
'''

import tkinter

def calculate_area():
    '''
    Calculates the area of a rectangle.
    '''
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    result_label.config(text="Area = " + str(area))

# Create the window
window = tkinter.Tk()
window.title("Square Area Calculator")

# Create length widgets
length_frame = tkinter.Frame(window)
length_label = tkinter.Label(length_frame, text="Length:")
length_entry = tkinter.Entry(length_frame)
length_label.pack(side=tkinter.LEFT, padx=2, pady=2)
length_entry.pack(side=tkinter.LEFT, padx=2, pady=2)
length_frame.pack()

# Create width widgets
width_frame = tkinter.Frame(window)
width_label = tkinter.Label(width_frame, text="Width:")
width_entry = tkinter.Entry(width_frame)
width_label.pack(side=tkinter.LEFT, padx=2, pady=2)
width_entry.pack(side=tkinter.LEFT, padx=2, pady=2)
width_frame.pack()

# Create calculate button
calculate_button = tkinter.Button(window, text="Calculate Area", command=calculate_area)
calculate_button.pack(padx=2, pady=2)

# Create result label
result_label = tkinter.Label(window, text="Area = ")
result_label.pack(padx=2, pady=2)

window.mainloop()