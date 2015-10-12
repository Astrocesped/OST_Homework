#!/usr/local/bin/python3
#
# GUI Layout Practice
# gui_layout.py
#
# 2015 July 12th
#
""" Practice tkinter layouts. """

from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(0, weight=1)
        f1 = Frame(self, bg="orange")
        f1.grid(row=0, column=0, columnspan=2, sticky=ALL)
        Label(f1, text="Frame 1", bg="orange", fg="white").pack(padx=80,
                                                                pady=50,
                                                                fill=BOTH,
                                                                expand=True)
        
        self.rowconfigure(1, weight=1)
        f2 = Frame(self, bg="red")
        f2.grid(row=1, column=0, columnspan=2, sticky=ALL)
        Label(f2, text="Frame 2", bg="red", fg="white").pack(padx=80,
                                                                pady=50,
                                                                fill=BOTH,
                                                                expand=True)
        
        f3 = Frame(self, bg="pink")
        f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        Label(f3, text="Frame 3", bg="pink", fg="red").pack(padx=120,
                                                                fill=BOTH,
                                                                expand=True)
        
        # Create row of five buttons
        self.rowconfigure(2)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=2, column=c,
                                                             sticky=W+E)
            
root = Tk()
app = Application(master=root)
app.mainloop()
