#!/usr/local/bin/python3
#
# GUI Events and Dialogs Practice
# gui_events.py
#
# 2015 July 14th
#
""" Practice tkinter Events and Dialogs. """

from tkinter import *
from tkinter.filedialog import LoadFileDialog

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(0, weight=1)
        f1 = Frame(self, bg="orange", name="frame 1")
        f1.grid(row=0, column=0, columnspan=2, sticky=ALL)
        Label(f1, text="Frame 1", bg="orange",).pack(padx=150, pady=50,
                                                     fill=BOTH, expand=True)
        
        self.rowconfigure(1, weight=1)
        f2 = Frame(self, bg="red", name="frame 2")
        f2.grid(row=1, column=0, columnspan=2, sticky=ALL)
        Label(f2, bg="red", text="Frame 2").pack(padx=150, pady=50,
                                                 fill=BOTH, expand=True)
        
        # Frame 3 contains an Entry and Text widgets
        f3 = Frame(self)
        f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)

        self.file_name_entry = Entry(f3, width=60)
        self.file_name_entry.pack(side=TOP, padx=20, pady=5, fill= BOTH)
        
        self.file_content_text = Text(f3, width=80, height=10)
        self.file_content_text.pack(side=TOP, padx=20, pady=10,
                                    fill= BOTH, expand=True)
        
        # Create row of five buttons, fifth one with Open File Dialog
        for c, color in enumerate(("Red", "Blue", "Green", "Black")):
            self.columnconfigure(c, weight=1)
            
            # Create a button for each color, after modifying the column.
            # Insert special lambda command function to pass a color argument
            Button(self, command=lambda c=color: self.text_color(c),
                   text=color).grid(row=2, column=c, sticky=W+E)
        
        self.columnconfigure(4, weight=1)
        Button(self, text="Open",
               command=self.open_file_dialog).grid(row=2, column=4,
                                                   sticky=W+E)
            
        # Connect events to widgets
        f1.bind("<Button-1>", self.print_mouse_info)
        f2.bind("<Button-1>", self.print_mouse_info)
    
    def open_file_dialog(self):
        d = LoadFileDialog(self)
        fname = d.go()
        if fname is not None:
            # Clear both fields before inserting corresponding data
            self.file_name_entry.delete(0, END)
            self.file_content_text.delete("1.0", END)
            
            # Insert name of the file inside the Frame 3's Entry
            self.file_name_entry.insert(INSERT, fname)
            
            # Retrieve the file's content through context manager
            with open(fname) as f:
                # Insert content into the Text field
                self.file_content_text.insert(INSERT, f.read())
            
    def print_mouse_info(self, event):
        """ Callback function that prints the location of a mouse click. """
        
        print("The widget {0} was clicked at "
              "X = {1} Y = [2]".format(event.widget, event.x, event.y))
        
    def text_color(self, color):
        """ Changes the foreground color of file_content_text.
        :param color: String containing name of color to change text to. """
        
        self.file_content_text.config(fg=color.lower())
        
root = Tk()
app = Application(master=root)
app.mainloop()
