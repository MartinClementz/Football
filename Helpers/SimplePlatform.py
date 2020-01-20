import pygame
class Platform():
    def __init__(self, width, height, x, y, name):
        ## trenger disse vaeriablene skrevet                  
        ## på akkruatt dene måten hvis den skal ha tyngdekraft 
        self.move = [0, 0]
        self.mass = 20
        self.name = name
        ########

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    ## Denne funksjonen trengs hvis platform skal bevege seg
    def Update(self):
        self.rect.move_ip(self.move[0], self.move[1])


    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
