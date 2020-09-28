import tkinter as tk

win = tk.Tk()

win.title('Calculator')  # title
"""win.resizable(False, False)  # (x, y)
# make it unresizable"""

tk.Label(win, text="First label").pack()
# text on the GUI
tk.Button(win, text="HI!").pack()

label2 = tk.Label(win, text="hi, my name is george")
label2.pack()

win.mainloop()
# start the GUI/run it/show it on the screen
