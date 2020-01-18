import pygame

class Graviti():
    def __init__(self, strenght):
        self.strenght = strenght

    def calculate(self,dTime, obj):
        obj.move[1] += obj.mass * self.strenght * dTime