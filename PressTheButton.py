'''
Press the Button
Pawelski
5/15/2023
Python II
'''

import tkinter

def change_text():
    '''
    Changes the text of the button.
    '''
    press_button.config(text="I was pressed!")

# Create the window
window = tkinter.Tk()
window.title("Press the Button")

# Create the button
press_button = tkinter.Button(window, text="Press me!", command=change_text)
press_button.pack()

window.mainloop()