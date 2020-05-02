#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tue Apr 28 16:50:42 2020

@authors: Bryan Toscano 'hyde'
          Vijay Duggirala 
          Viraat Udar
"""
## USE sudo apt-get install python3-tk ##
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as tkmessage

class mainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # Call Parent's Constructor
        self.bodyFont = tkfont.Font(family="Helvetica", size="14", weight="bold")
        self.titleFont = tkfont.Font(family="Helvetica", size="18", weight="bold")
        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


## main() Function implementation ##

def main():
    app = mainApplication()
    app.geometry("800x600")
    app.title("Clothing Picker Software")
    app.mainloop()

## Call main Function. Python does not do this by default ##
if __name__ == "__main__":
    main()