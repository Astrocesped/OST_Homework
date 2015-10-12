#!/usr/local/bin/python3
#
# GUI Entry adder
# gui_entry_adder.py
#
# 2015 July 11th
#
""" Creates a tkinter window that sums input. """

from tkinter import *
from math import fsum

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        top_frame = Frame(self)
        input_label1 = Label(top_frame, text="Number 1:")
        self.number_input1 = Entry(top_frame, width=15)
        separator_label = Label(top_frame, padx=10)
        input_label2 = Label(top_frame, text="Number 2:")
        self.number_input2 = Entry(top_frame, width=15)
        
        input_label1.pack(side=LEFT)
        self.number_input1.pack(side=LEFT)
        separator_label.pack(side=LEFT)
        self.number_input2.pack(side=RIGHT)
        input_label2.pack(side=RIGHT)
        top_frame.pack(expand=True, side=TOP)
        
        middle_frame = Frame(self)
        result_label = Label(middle_frame, text="Result:", pady=15)
        self.actualresult_label = Label(middle_frame, pady=15)
        result_label.pack(side=LEFT)
        self.actualresult_label.pack(side=RIGHT)
        middle_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        self.result_button = Button(bottom_frame, text="Add both numbers",
                                    command=self.sum_entries, padx=20)
        self.result_button.pack()
        bottom_frame.pack(side=TOP)
        
        self.pack(padx=10, pady=15)
        
    def sum_entries(self):
        """ Modifies the 'actualresult_label' with the result of the sum of
        both Entry fields.
        """
        self.actualresult_label.config(text=
                                       add_input(self.number_input1.get(),
                                                 self.number_input2.get()))

def add_input(*args):
    """ Adds the passed arguments.
    :param *args: List of positional parameters containing numbers
    :return: String containing the sum (or an ERROR warning)
    """

    try:
        converted_args = [float(number) for number in args]
    
    except ValueError:
        return "***ERROR***"
    
    # Return a math.fsum of the list of parameters
    return fsum(converted_args)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Input Adder")
    app = Window(master=root)
    app.mainloop()