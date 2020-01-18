import pygame # 1.9.6
from Helpers.Collitions import Collitions 
from Helpers.SimplePlayer import Player
from Helpers.SimplePlatform import Platform 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

FPS = 30
HEIGHT = 400 
WIDTH = 400

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Simple Exsample")
 

collitions = Collitions()

# Legger til Agents som kan kolidere med statiske elementer
player = Player()
collitions.addAgent(player)

# Legger til statiske elemepter som kan kolidere med Agents
platform = Platform(500,50, 0, 300)
collitions.addStatic(platform)
platform2 = Platform(200, 25, 100, 220)
collitions.addStatic(platform2)


clock = pygame.time.Clock()
done = False
# -------- Main Program Loop -----------
while done != True:
    # delta time
    dTime = clock.get_time()/1000


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    # --- Game logic should go here
    player.update()
    collitions.calculate(dTime)
    
 
    
 
    # --- Drawing code should go here
    screen.fill(WHITE)
  
    platform.draw(screen, BLACK)
    platform2.draw(screen, BLACK)
    player.draw(screen, BLACK)


    pygame.display.flip()
    clock.tick(FPS)

# Close the window and quit.
pygame.quit()