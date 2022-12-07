# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from VirtPet import VirtPet
import configure
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def openFile():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    print(filename)
    
   
def getName(entry):
        name = entry.get()   
        print(name)
        
def launchNewGame():       
    root = Tk()
    frm = ttk.Frame(root, padding = 10)
    frm.grid()
    entry1 = Entry(frm).grid(column=0, row=0)
    ttk.Button(frm, text = "Name my Pet", command = lambda: getName(entry1)).grid(column=0, row = 1)
    root.mainloop()
        
    
def testMain ():
    print("Welcome to the Virtual Pet Shop \n")
    startGame = False
    while startGame == False:
        selection = input("Would you like to 1) start a new game\n or\n 2) return to a previous pet? ")
        if selection == "1" or selection == "2":
            if selection == "1":
                name = input("What would you like to name your new pet? ")
                path = "C:\VirtPet\configs"
                file = path+"\\"+name+".txt"
                configure.configure(name, file, path)
                startGame = True
            else:
                print("Sorry - we aren't set up to continue a previous game yet. Check back tomorrow!")
        else:
            print("Sorry - Not a valid selection, please type in 1 or 2")
    
def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Welcome to Gotchi!").grid(column=0, row=0)
    ttk.Button(frm, text = "New Game", command = launchNewGame).grid(column = 0, row = 1)
    ttk.Button(frm, text = "Open Saved Game", command = openFile).grid(column = 0, row = 2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    root.mainloop()
          
        
    
if __name__ == "__main__":
    main()