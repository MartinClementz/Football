class Collitions():
    def __init__(self):
        self.static = []
        self.agents = []
        self.collided = {}
        
    # alle statiske objekter som spiller kan kolidere med
    # disse kan ikke kolidere med hverandre
    def addStatic(self, obj):
        self.static.append(obj)

    # alle dynamiske elementer som kan kolidere med statiske elementer
    # disse kan ikke kolidere med hverandre
    def addAgent(self, obj):
        self.agents.append(obj)

    # Regner ut kolisjoner mellom objekter
    def calculate(self, dTime):
        for agent in self.agents:
            for index in range(len(self.static)):
                c = agent.rect.colliderect(self.static[index])

                if c == True:
                    
                    # collided Bottom side of player
                    if agent.rect.bottom >= self.static[index].rect.top and agent.rect.bottom <= self.static[index].rect.bottom + agent.move[1] and agent.move[1] > 0:
                        agent.rect.bottom = self.static[index].rect.top + 2
                        agent.move[1] = 0
                        
                        try:
                            agent.jump = False
                        except:
                            pass

                    # collided right side of player
                    elif agent.rect.right >= self.static[index].rect.left and agent.rect.right <= self.static[index].rect.left + agent.speed:
                        agent.rect.right = self.static[index].rect.left
                        agent.rect.move_ip(-1, 0)

                    # collided left  side of player
                    elif agent.rect.left <= self.static[index].rect.right and agent.rect.left >= self.static[index].rect.right - agent.speed:
                        agent.rect.left = self.static[index].rect.right
                        agent.rect.move_ip(1, 0)
                        
                    # collided top side of player
                    elif agent.rect.top <= self.static[index].rect.bottom and agent.rect.top >= self.static[index].rect.top + agent.move[1] and agent.move[1] < 0:
                        agent.rect.top = self.static[index].rect.bottom
                        agent.move[1] = 0

                    ########### Viktig ############
                    # Lager dictionary med alle objekter som har kolidert. Nå vises
                    # navnet til objektene som har kolidert. Dette er kun for det 
                    # visuellle, slik at det er lett å se hva som har kolidert. Men det 
                    # gitt mere mening å legge til selve objektene, ved å fjerne .name
                    # fra begge objektene. Dette vil gi mye mere fleksiblitet
                    self.collided[self.static[index].name] = agent.name
                    

                else:
                    # Ingen ting har kolidert med dette objektet
                    self.collided[self.static[index].name] = None
                        
                    
                
