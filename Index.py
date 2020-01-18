"""
python index.py
"""
#### Importerer pakker ####
import pygame # 1.9.6
from Helpers.Collitions import Collitions 
from Helpers.SimplePlayer import Player
from Helpers.SimplePlatform import Platform 
from Helpers.Gravity import Graviti 

#### Farger ####
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
Co = (255, 100, 100)

#### Pygame variabler ####
FPS = 30
HEIGHT = 400 
WIDTH = 400

#### Starter pygame ####
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pygame-2DPlatformer-Starter")
 
#### Starter kolisjoner ####
collitions = Collitions()
#### Lager tyngdekraft force:2 ####
gravity = Graviti(2)


#### Lager Spiller ####
player = Player()
#### Gir spiller kolisjon ####
collitions.addAgent(player)



#### Lager Platform 1 ####
platform = Platform(400,50, 0, 300, "Platform 1")
#### Gir platform kolisjon ####
collitions.addStatic(platform)

#### Lager Platform 2 ####
platform2 = Platform(200, 25, 100, 215, "Platform 2")
#### Gir platform kolisjon ####
collitions.addStatic(platform2)

#### Lager Platform 3 ####
platform3 = Platform(100, 50, 300, 150, "Platform 3")
#### Gir platform kolisjon ####
collitions.addStatic(platform3)


#### Lager klokke ####
clock = pygame.time.Clock()


#### GAME LOOP ####
done = False
while done != True:

    #### Delta tid, i sekunder ####
    dTime = clock.get_time()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #### OPPDATERER ####

    #### Spiller - med input ####
    player.update()
    #### Spiller - med tyngdekraft ####
    gravity.calculate(dTime, player)

    #### Kalkulerer alle kollisjoner #### 
    collitions.calculate(dTime)

    #### Hva har kolidert ####
    print(collitions.collided)


    #### TEGNER ####
    screen.fill(WHITE)
  
    #### Hvis spiller har kolidert med platform 2 ####
    if collitions.collided["Platform 3"] == "Player":
        platform3.draw(screen, GREEN)

    else:
        platform3.draw(screen, BLACK)


    player.draw(screen, Co)
    platform2.draw(screen, BLACK)
    platform.draw(screen, BLACK)
    

    pygame.display.flip()
    clock.tick(FPS)
# Close the window and quit.
pygame.quit()