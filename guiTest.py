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
        self.Splashroot = super().__init__()
        self.splash = ttk.Frame(self.Splashroot, padding=10)
        self.splash.grid()
        ttk.Label(self.splash, text = "Welcome to Gotchi!").grid(column = 0, row = 0)
        ttk.Button(self.splash, text = "New Game", command = self.startNewGame).grid(column = 0, row = 1)
        ttk.Button(self.splash, text = "Open Saved Game", command = self.openSavedGame).grid(column = 0, row = 2)
        
    def startNewGame(self):
        self.newGameScreen = newGame()
        self.newGameScreen.mainloop()
    
    def openSavedGame(self):
        self.openSavedGame = openSavedGame()
        self.openSavedGame.mainloop()
    
        
class newGame(tk.Tk):
    def __init__(self):
        self.Newroot = super().__init__()
        self.new = ttk.Frame(self.Newroot, padding=10)
        self.new.grid()
        ttk.Entry(self.new).grid(column = 0, row = 0)
        ttk.Button(self.new, text="Name My Pet", command=self.on_button).grid(column = 0, row = 1)
        ttk.Button(self.new, text="Launch New Game").grid(column = 0, row = 2)

    def on_button(self):
        print(self.entry.get())

class openSavedGame(tk.Tk):
    def __init__(self):
        self.Openroot = super().__init__()
        self.open = ttk.Frame(self.Openroot, padding=10)
        self.open.grid()
        ttk.Label(self.open, text = "Placeholder").grid(column = 0, row = 0)
        

        
class gamePlay(tk.Tk):
    def __init__(self):
        print("Play a game")

app = splashDialog()
app.mainloop()
        