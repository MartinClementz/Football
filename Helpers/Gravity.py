import pygame

class Graviti():
    def __init__(self, strength):
        self.strength = strength

    def calculate(self,dTime, obj):
        obj.move[1] += obj.mass * self.strength * dTime