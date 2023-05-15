'''
Positioning Buttons
Pawelski
5/15/2023
Python II
'''

import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Positioning Buttons")

# Create buttons
button1 = tk.Button(window, text="Button 1")
button2 = tk.Button(window, text="Button 2")
button3 = tk.Button(window, text="Button 3")
button4 = tk.Button(window, text="Button 4")
button1.pack(side=tk.TOP, padx=2, pady=2)
button2.pack(side=tk.TOP, padx=2, pady=2)
button3.pack(side=tk.TOP, padx=2, pady=2)
button4.pack(side=tk.TOP, padx=2, pady=2)

window.mainloop()