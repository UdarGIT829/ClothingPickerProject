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
import colors

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

        for F in (HomeFrame, ClosetFrame, OutfitFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomeFrame")
    
    def initialize(self):
        pass

    def show_frame(self, name):
        frame = self.frames[name]
        frame.initialize()
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
        titleText = tk.Label(titleContainer, text="Home Page", font=controller.titleFont)
        titleText.pack(anchor=tk.N, side = tk.TOP, pady = 15)
        menubox = tk.Canvas(self)
        menubox.place(anchor = tk.NE, relx=0.14, rely = 0.25)
        tk.Label(menubox, text="Main Menu", font=controller.titleFont).pack(anchor=tk.N, side=tk.TOP, pady=30)
        closetButton = tk.Button(menubox, text="Browse Closet", font=controller.bodyFont, command=lambda: controller.show_frame("ClosetFrame"))
        closetButton.pack(anchor=tk.N, side = tk.TOP, pady = 5)
        tk.Button(menubox, text="Match Outfits", font=controller.bodyFont, command=lambda: controller.show_frame("OutfitFrame")).pack(anchor=tk.N, side = tk.TOP, pady = 5)

        exitButton = tk.Button(menubox, text="Exit", font=controller.bodyFont, command=self.quit)
        exitButton.pack(anchor=tk.N, side = tk.TOP, pady = 5)
    
    def initialize(self):
        pass
        

# closetFrame - Inherits from tkinter frame
# Closet Browser page. This frame displays what is currently in the closet and what is in the laundry list. You can do your laundry here as well.
# Programmers: Vijay
# Date: 5/01/2020

class ClosetFrame(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.closet = Closet()
        self.closet.load()
        self.tops = self.closet.tops
        self.bottoms = self.closet.bottoms
        self.shoes = self.closet.shoes

        titleCanvas = tk.Canvas(self)
        titleCanvas.pack(anchor=tk.NE, expand=True, fill="x")
        titleText = tk.Label(titleCanvas, text="Your Closet", font=controller.titleFont)
        titleText.pack(anchor=tk.N, side = tk.TOP, pady = 15)

        BackButton = tk.Button(titleCanvas, text="Back", font=controller.bodyFont, command=lambda: controller.show_frame("HomeFrame"))
        BackButton.pack(anchor=tk.NE, side = tk.LEFT, padx = 15)

        topsListCanvas= tk.Canvas(self)
        topsListCanvas.place(anchor=tk.CENTER, relx=0.25, rely=0.35)
        bottomsListCanvas= tk.Canvas(self)
        bottomsListCanvas.place(anchor=tk.CENTER, relx=0.5, rely=0.35)
        shoesListCanvas= tk.Canvas(self)
        shoesListCanvas.place(anchor=tk.CENTER, relx=0.75, rely=0.35)

        topsSb = tk.Scrollbar(topsListCanvas)
        topsSb.pack(side=tk.RIGHT, fill="y", pady=(30,0))
        bottomsSb = tk.Scrollbar(bottomsListCanvas)
        bottomsSb.pack(side=tk.RIGHT, fill="y", pady=(30,0))
        shoesSb = tk.Scrollbar(shoesListCanvas)
        shoesSb.pack(side=tk.RIGHT, fill="y", pady=(30,0))

        self.topsList = tk.Listbox(topsListCanvas, font=controller.bodyFont, yscrollcommand=topsSb.set, width=30)
        self.bottomsList = tk.Listbox(bottomsListCanvas, font=controller.bodyFont, yscrollcommand=bottomsSb.set, width=30)
        self.shoesList = tk.Listbox(shoesListCanvas, font=controller.bodyFont, yscrollcommand=shoesSb.set, width=30)

        topsSb.config(command=self.topsList.yview)
        bottomsSb.config(command=self.bottomsList.yview)
        shoesSb.config(command=self.shoesList.yview)

        tk.Label(topsListCanvas, text="Tops", font=controller.titleFont).pack(anchor=tk.N, side=tk.TOP)
        tk.Label(bottomsListCanvas, text="Bottoms", font=controller.titleFont).pack(anchor=tk.N, side=tk.TOP)
        tk.Label(shoesListCanvas, text="Shoes", font=controller.titleFont).pack(anchor=tk.N, side=tk.TOP)

        self.topsList.pack(anchor=tk.N, side=tk.TOP, pady="5")
        self.bottomsList.pack(anchor=tk.N, side=tk.TOP, pady="5")
        self.shoesList.pack(anchor=tk.N, side=tk.TOP, pady="5")
        self.initialize()

    def initialize(self):
        self.topsList.delete(0, tk.END)
        self.bottomsList.delete(0,tk.END)
        self.shoesList.delete(0,tk.END)
        for top in self.tops:
            tempStr = str(""+top.getName()+", "+str(top.getStatus()))
            self.topsList.insert(tk.END, tempStr)
        for bottom in self.bottoms:
            tempStr = str(""+bottom.getName()+", "+str(bottom.getStatus()))
            self.bottomsList.insert(tk.END, tempStr)
        for shoe in self.shoes:
            tempStr = str(""+shoe.getName()+", "+str(shoe.getStatus()))
            self.shoesList.insert(tk.END, tempStr)
        
# OutfitFrame - Inherits from tkinter frame
# Outfit Browser. This frame displays possible matching outfits from the garmets in the closet. 
# Programmers: Vijay
# Date: 5/04/2020

class OutfitFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.closet = Closet()
        self.closet.load()
        self.tops = self.closet.tops
        self.bottoms = self.closet.bottoms
        self.shoes = self.closet.shoes

        self.colordict = dict()
        self.outfits = list()

        tk.Label(self, text="Calculated Outfits", font=controller.titleFont, justify=tk.CENTER).place(anchor=tk.N, relx=0.5, rely=0.01)
        
        BackButton = tk.Button(self, text="Back", font=controller.bodyFont, command=lambda: controller.show_frame("HomeFrame"))
        BackButton.place(anchor=tk.NE,relx=0.07, rely=0.04)

        mainSb = tk.Scrollbar(self)
        mainSb.pack(side=tk.RIGHT, fill="y", padx=(0, 345), pady=243)
        self.lbox = tk.Listbox(self, font=controller.bodyFont, yscrollcommand=mainSb.set, width=50, justify=tk.CENTER, selectmode=tk.SINGLE)
        self.lbox.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        mainSb.config(command=self.lbox.yview)
        tk.Button(self, text="Outfit Info", font=controller.bodyFont, command=lambda: self.Selected()).place(anchor=tk.NE,relx=0.9, rely=0.9)
    
    def Selected(self):
        if all(self.lbox.curselection()) or not self.outfits:
            tk.messagebox.showerror("Error", "No Outfit Selected")
            return
    
    def StrToTuple(self, myStr):
        tup = tuple()
        for token in myStr.split(","):
            tup = tup+(int(token),)
        return tup
    
    def GetBottomThatMatches(self, listOfColors):
        listOfBottoms = list()
        for col in listOfColors:
            for bottom in self.bottoms:
                bottomCol = bottom.colors[0].replace(',', '')
                if str(bottomCol) == str(col):
                    listOfBottoms.append(bottom)
        return listOfBottoms
    
    def initialize(self):
        self.lbox.delete(0, tk.END)
        self.outfits = list()
        print("Cleared List")
        self.colordict = colors.initializeColors()
        for shirt in self.tops:
            sColor= shirt.colors[0]
            sColor = tuple(self.StrToTuple(sColor))
            Bottoms = self.GetBottomThatMatches(self.colordict[sColor])
            if Bottoms:
                for bottom in Bottoms:
                    self.outfits.append(str(shirt.getName()) + " AND " +str(bottom.getName()) + " AND Converse White Shoes")
        if not self.outfits:
            self.lbox.insert(tk.END, "No Outfits Found")
            print("FOUND NONE")
        
        for outfit in self.outfits:
            self.lbox.insert(tk.END, outfit)
        



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