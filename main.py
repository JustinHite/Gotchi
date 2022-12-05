# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from VirtPet import VirtPet
import configure
import os

def main ():
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
    
            
        
    
if __name__ == "__main__":
    main()