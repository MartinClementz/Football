import pygame

class Player():
    def __init__(self):
        ## trenger disse vaeriablene skrevet                  
        ## på akkruatt dene måten hvis den skal ha tyngdekraft 
        self.name = "Player"
        self.mass = 40       
        self.move = [0, 0]   # Bevegelses vektor
        #####

        self.jump = False    # Hopper spillern nå?
        self.speed = 6       # Spiller'ns fart
        self.jumpHeight = 23 # Hoppekraft 

        self.height = 60
        self.width = 50
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # Bruker input sim beveger spiller'n
    def movement(self):
        keys = pygame.key.get_pressed() 

        # Hoppe
        if keys[pygame.K_w]:
            if self.jump == False:  
                self.move[1] = -(self.jumpHeight)
                self.jump = True

        # Begege seg venstre
        if keys[pygame.K_a]:
            self.move[0] = -self.speed
       
       # Begege seg høyre
        if keys[pygame.K_d]:
            self.move[0] = self.speed
        
        # Ingen bevegelse på x aksen 
        if keys[pygame.K_d] != True and keys[pygame.K_a] != True:
            self.move[0] = 0
            
    # Oppdaterer posisjonen til spiller'n
    def update(self):
        self.movement()
        self.rect.move_ip(self.move[0], self.move[1])

    # Tegner spiller
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
