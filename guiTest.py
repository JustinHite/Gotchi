# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:50:06 2022

@author: hitejad
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class splashDialog():
    def __init__(self, master):
        self.splash = ttk.Frame(master, padding=10)
        self.splash.grid()
        #welcome Label
        self.welcomeLabel = ttk.Label(self.splash, text = "Welcome to Gotchi!")
        self.welcomeLabel.grid(column = 0, row = 0)
        #New Game Button
        self.newGameButton = ttk.Button(self.splash, text = "New Game", command = self.startNewGame)
        self.newGameButton.grid(column = 0, row = 1)
        #Open Saved Game Button
        self.savedGame = ttk.Button(self.splash, text = "Open Saved Game", command = self.openSavedGame)
        self.savedGame.grid(column = 0, row = 2)
        
    def startNewGame(self):
        self.splash.destroy()
        self.newGameScreen = newGame()

    
    def openSavedGame(self):
        self.splash.destroy()
        self.savedGameScreen = openSavedGame()
    
        
class newGame():
    def __init__(self):
        self.new = ttk.Frame(padding=10)
        self.new.grid()
        #Name Entry
        self.nameEntry = ttk.Entry(self.new)
        self.nameEntry.grid(column = 0, row = 0)
        #Name Pet Button
        self.namePet = ttk.Button(self.new, text="Name My Pet", command=self.on_button)
        self.namePet.grid(column = 0, row = 1)
        #Launch New Game Button
        self.launchGame = ttk.Button(self.new, text="Launch New Game", command = self.launchGame)
        self.launchGame.grid(column = 0, row = 2)

    def on_button(self):
        print(self.nameEntry.get())
        
    def launchGame(self):
        self.new.destroy()
        self.gamePlay = gamePlay()

class openSavedGame(tk.Tk):
    def __init__(self):
        self.open = ttk.Frame(padding=10)
        self.open.grid()
        ttk.Label(self.open, text = "Placeholder").grid(column = 0, row = 0)
        self.launchGame = ttk.Button(self.open, text="Launch Game", command = self.launchGame)
        self.launchGame.grid(column = 0, row = 1)
        
    def launchGame(self):
        self.open.destroy()
        self.gamePlay = gamePlay()
        

        
class gamePlay(tk.Tk):
    def __init__(self):
        self.play = ttk.Frame(padding=10)
        self.play.grid()
        #Widget?
        self.playArea = tk.Canvas(self.play, height = 100, width = 100)
        self.playArea.grid(column=0, row=0)
        self.coord = 10, 10, 60, 60
        self.arc = self.playArea.create_arc(self.coord, start = 0, extent =359 , fill = "red")
        #Feed Pet
        self.feedPet = ttk.Button(self.play, text = "Feed")
        self.feedPet.grid(column=1, row=0)
        #Play
        self.playPet= ttk.Button(self.play, text = "Play")
        self.playPet.grid(column=1, row=1)
        #Clean
        self.cleanPet = ttk.Button(self.play, text = "Clean")
        self.cleanPet.grid(column=1, row=2)
    
        


def main():
    root = tk.Tk()
    window = splashDialog(root)
    root.mainloop()
    
main()