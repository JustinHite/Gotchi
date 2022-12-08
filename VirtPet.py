# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:03:06 2022

@author: hite3
"""

class VirtPet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.happiness = 0
        self.hunger = 0
        self.size = 1
        self.life = 100
        
    def play(self, happiness):
        self.happiness = self.happiness + 5
        return self.happiness
    
    def eat(self, hunger):
        self.hunger = self.hunger + 5
        return self.hunger
    
    def _sadness(self, happiness):
        self.happiness = self.happiness - 1
        return self.happiness
        
    def _hunger(self, hunger):
        self.hunger = self.hunger - 1
        return self.hunger
        
    def _health(self, life, happiness, hunger):
        if self.happiness < 10:
            self.life = self.life - 1
        elif self.happiness > 20:
            self.life = self.life + 1
        
        if self.hunger < 10:
            self.life = self.life - 1
        elif self.hunger > 20:
            self.life = self.life + 1
        
    def _age(self, age):
        self.age = self.age + 1
        return self.age
    
    def _deathCheck(self, age, life):
        death = False
        if self.age > 25:
            death = True
        elif self.life < 1:
            death = True
        return death

            
            
    
    
            
        
        
        
    
        
    
    