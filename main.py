import PySimpleGUI as sg

# Defining all elements of the GUI/Initializing the GUI
# ---------------------------------------------------------------------------------------------------------------------

starting_str: str = "0"
eval_string: str = "0"
# major varibles: eval_string, starting_str
# use of eval_string: the string that holds the equations and gets evaluated
# use of starting_str: string shown on screen; string that is added to eval string along with an operator

C: bool = False
AC: bool = True
# determines which state the clear button is in

clear_button = sg.Button("AC", size=(3, 1.5), font="Helvetica", button_color=("white", "DarkGrey"), key="")
# define what the clear button is
layout = [
    [sg.Text(starting_str, size=(9, 1), font=("Helvetica", 50), key="_STRSHOWN_")],  # Text Row

    [clear_button,  # Row 1
     sg.Button("+/-", size=(3, 1.5), font="Helvetica", button_color=("white", "DarkGrey")),
     sg.Button("%", size=(3, 1.5), font="Helvetica", button_color=("white", "DarkGrey")),
     sg.Button(u"\N{DIVISION SIGN}", size=(3, 1.5), font="Helvetica", button_color=("white", "orange"))],

    [sg.Button("7", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),  # Row 2
     sg.Button("8", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("9", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button(chr(215), size=(3, 1.5), font="Helvetica", button_color=("white", "orange"))],

    [sg.Button("4", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),  # Row 3
     sg.Button("5", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("6", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("-", size=(3, 1.5), font="Helvetica", button_color=("white", "orange"))],

    [sg.Button("1", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),  # Row 4
     sg.Button("2", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("3", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("+", size=(3, 1.5), font="Helvetica", button_color=("white", "orange"))],

    [sg.Button("0", size=(12, 1.5), font="Helvetica", button_color=("white", "Grey")),  # Row 5
     sg.Button(".", size=(3, 1.5), font="Helvetica", button_color=("white", "Grey")),
     sg.Button("=", size=(3, 1.5), font="Helvetica", button_color=("white", "orange"))]
]
sg.theme("DarkGrey5")
window = sg.Window("Calculator", layout=layout)

# Main Logic & Loops in the GUI
# ---------------------------------------------------------------------------------------------------------------------

while True:
    event, value = window.read()
    # start the GUI and read values given from it

    if event == sg.WIN_CLOSED:
        break  # prevent the code from running errors infinitely

    # number/digit button logic
    if len(starting_str) < 9:  # digit limit
        if starting_str == "0":
            if event in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                starting_str = event  # replace the unneeded 0
                clear_button.Update("C")
                AC = False
                C = True
        else:
            if event in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                starting_str += event  # concatenate the number to starting_str
            elif event == "+/-":
                if starting_str[0] == "-":
                    starting_str = starting_str[1:]
                else:
                    starting_str = "-" + starting_str
        window["_STRSHOWN_"].update(starting_str)  # update the text shown on the screen

    # clear button logic
    if C:
        if event == "":
            C = False
            AC = True
            starting_str = "0"
            window["_STRSHOWN_"].update(starting_str)  # update the text shown on the screen
            clear_button.Update("AC")
    elif AC:
        if event == "":
            AC = False
            C = True
            eval_string = "0"
            starting_str = "0"
            window["_STRSHOWN_"].update(starting_str)  # update the text shown on the screen

    # In Development
    # ------------------------------------------------------------------------------------
    if len(starting_str) < 9:
        if event == ".":
            if starting_str == "0":
                starting_str = "0."
            else:
                starting_str = starting_str + "."
            window["_STRSHOWN_"].update(starting_str)

    if event == "%":
        if starting_str[-1] in ("+", "-", "*", "/"):
            starting_str = starting_str[0:len(starting_str) - 1]
        eval_string += f"({starting_str})"
        if eval_string[0] == "0":
            eval_string = eval_string[1:]
        starting_str = str(eval(eval_string)/100)[:9]
        window["_STRSHOWN_"].update(starting_str)
        print(str(eval(eval_string)/100)[:9])
        eval_string = "0"
    # ------------------------------------------------------------------------------------

    # operation button logic
    if event == "=":
        if starting_str[-1] in ("+", "-", "*", "/"):
            starting_str = starting_str[0:len(starting_str) - 1]
        eval_string += f"({starting_str})"
        if eval_string[0] == "0":
            eval_string = eval_string[1:]
        starting_str = "0"
        try:
            window["_STRSHOWN_"].update(str(eval(eval_string))[:9])  # show the answer on the screen
        except ZeroDivisionError:
            window["_STRSHOWN_"].update("Error")
        eval_string = "0"  # prevent the "EqualSignGlitch" where you can't do any equations after solving 1 equations
        clear_button.Update("AC")
        AC = True
        C = False
    elif event in ("+", "-", chr(215), u"\N{DIVISION SIGN}"):
        dupl = False
        if eval_string == "0":
            eval_string = eval_string.replace("0", "")
        if event in ("+", "-"):
            eval_string += f"({starting_str}){event}"
        elif event == chr(215):
            eval_string += f"({starting_str})*"
        elif event == u"\N{DIVISION SIGN}":
            eval_string += f"({starting_str})/"
        starting_str = "0"
        AC = True
        C = False

# Cleaning up and closing everything
# ---------------------------------------------------------------------------------------------------------------------

window.close()
# safely close the window and prevent errors
quit()
# make sure that the program closes
#