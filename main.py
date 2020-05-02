# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tue Apr 28 16:50:42 2020

@authors: Bryan Toscano
          Vijay Duggirala
          Viraat Udar
"""
# USE sudo apt-get install python3-tk
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox as tkmessage
from closet import Closet
from garment import Garment

# MainApplication class - Inherits from main tkinter object
# Main Application window that contains all the other classes(also windows) as variables and performs operations on them.
# Programmers: Vijay
# Date: 5/01/2020

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # Call Parent's Constructor
        self.bodyFont = tkfont.Font(family="Helvetica", size="14", weight="bold")
        self.titleFont = tkfont.Font(family="Helvetica", size="18", weight="bold")
        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (HomeFrame, ClosetFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomeFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

# HomeFrame - Inherits from tkinter frame
# Home page. This simply displays some welcome messages and menus for navigating to other frames. 
# Programmers: Vijay
# Date: 5/01/2020

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        titleContainer = tk.Canvas(self)
        titleContainer.pack(side="top")
        titleText = tk.Label(titleContainer, text="Main Menu", font=controller.titleFont)
        titleText.pack(anchor=tk.N, side = tk.TOP, pady = 15)
        menubox = tk.Canvas(self)
        menubox.pack(anchor = tk.NE, side=tk.LEFT)
        closetButton = tk.Button(menubox, text="Browse Closet", font=controller.bodyFont, command=lambda: controller.show_frame("ClosetFrame"))
        closetButton.pack(anchor=tk.N, side = tk.TOP, padx = 15)
        

# closetFrame - Inherits from tkinter frame
# Closet Browser page. This frame displays what is currently in the closet and what is in the laundry list. You can do your laundry here as well.
# Programmers: Vijay
# Date: 5/01/2020

class ClosetFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        closet = Closet()
        closet.load()
        tops = list(closet.tops)
        bottoms = closet.bottoms
        shoes = closet.shoes
        titleCanvas = tk.Canvas(self)
        titleCanvas.pack(anchor=tk.NE, expand=True, fill="x")
        titleText = tk.Label(titleCanvas, text="Your Closet", font=controller.titleFont)
        titleText.pack(anchor=tk.N, side = tk.TOP, pady = 15)
        BackButton = tk.Button(titleCanvas, text="Back", font=controller.bodyFont, command=lambda: controller.show_frame("HomeFrame"))
        BackButton.pack(anchor=tk.NE, side = tk.LEFT, padx = 15)
        topsbox = tk.Scrollbar(self)
        topsbox.pack(anchor=tk.CENTER, side=tk.TOP, fill="both")
        topsList = tk.Listbox(topsbox)
        topsList.pack()
        for top in tops:
            topStr = str(""+Garment(top).name+", "+str(not Garment(top).isDirty()))
            topsList.insert(tk.END, topStr)
        topsList.config(yscrollcommand=topsbox.set)
        topsbox.config(command=topsList.yview)




# Main function
# Main function simply creates an instance of the application class and shows it to user. 
# Programmers: Vijay
# Date: 5/01/2020

def main():
    app = MainApplication()
    app.geometry("1280x720")
    app.title("Clothing Picker Software")
    app.mainloop()

# Call main Function. Python does not do this by default
if __name__ == "__main__":
    main()