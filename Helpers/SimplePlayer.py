import pygame
class Player():
    def __init__(self):
        self.height = 75
        self.width = 50
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.jump = False # isJumping?
        self.mass = 40 # kg
        self.move = [0, 0] # movement Vector
        self.speed = 6 # player speed
        self.jumpHeight = 20 # jump force


    def movement(self):
        keys = pygame.key.get_pressed() 

        if keys[pygame.K_w]:
            if self.jump == False:  
                self.move[1] = -(self.jumpHeight)
                self.jump = True

        if keys[pygame.K_a]:
            self.move[0] = -self.speed
       
        if keys[pygame.K_d]:
            self.move[0] = self.speed
        
        if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
            self.move[0] = 0
            

    def update(self):
        self.movement()
        self.rect.move_ip(self.move[0], self.move[1])


    def draw(self, screen, BLACK):
        pygame.draw.rect(screen, BLACK, self.rect)
