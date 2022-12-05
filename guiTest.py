# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:50:06 2022

@author: hitejad
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class splashDialog(tk.Tk):
    def __init__(self):
        self.root = tk.Tk.__init__(self)
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.ttk.Label(self.frm, text="Welcome to Gotchi!").grid(column=0, row=0)
        self.ttk.Button(self.frm, text = "New Game", command = self.launchNewGame).grid(column = 0, row = 1)
        self.ttk.Button(self.frm, text = "Open Saved Game", command = self.openFile).grid(column = 0, row = 2)
        self.ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=0, row=3)
        
    def launchNewGame(self):
        print("launch New game")
        
    def openFile(self):
        print("open file")
    
        
class newGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Name My Pet", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())

class openSavedGame(tk.Tk):
    def __init__(self):
        print("Open saved game")

        
class gamePlay(tk.Tk):
    def __init__(self):
        print("Play a game")

app = splashDialog()
app.mainloop()
        