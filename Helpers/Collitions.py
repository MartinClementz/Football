class Collitions():
    def __init__(self):
        self.static = []
        self.agents = []
        self.collided = {}
        
    def addStatic(self, obj):
        self.static.append(obj)

    def addAgent(self, obj):
        self.agents.append(obj)

    def calculate(self, dTime):
        for agent in self.agents:
            for index in range(len(self.static)):
                c = agent.rect.colliderect(self.static[index])
                #index = agent.rect.collidelist(self.static)
                if c == True:
                    
                    # collided Bottom side of player
                    if agent.rect.bottom >= self.static[index].rect.top and agent.rect.bottom <= self.static[index].rect.bottom and agent.move[1] > 0:
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
                    elif agent.rect.top <= self.static[index].rect.bottom and agent.rect.top >= self.static[index].rect.top and agent.move[1] < 0:
                        agent.rect.top = self.static[index].rect.bottom
                        agent.move[1] = 0

                    self.collided[self.static[index].name] = agent.name
                    

                else:
                    self.collided[self.static[index].name] = None
                        
                    
                
