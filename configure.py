# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:16:27 2022

@author: hite3
"""

from VirtPet import VirtPet
import os

def configure(name, file, path):
    if os.path.exists(path):
        print("Game Installed")
    else:
        os.makedirs(path)
        
    if os.path.exists(file):
        print("Player Exists")
        '''if player exists then give options of files to read'''
        '''need to import json file and begin game'''
    else:
        pet = VirtPet(name)
        body = """"name":"{}",\n"age":"{}",\n"happiness":"{}",\n"hunger":"{}",\n"life":"{}"\n""".format(pet.name, pet.age, pet.happiness, pet.hunger, pet.life)
        with open(file, "w") as f:
            f.write("{\n"+body+"\n}")
        return(pet)