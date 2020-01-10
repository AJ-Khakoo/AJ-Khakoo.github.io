
import random
#Step 1: creating the agents.
class Agent():
#Step 2: Initialisation of the agents within the code and output space (environment).
    def __init__(self,environment,agents) :
        self.environment = environment
        self.agents = agents
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.store = 0
        
#Step 3: Rreturning the string representation of agents 
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y) + ",store=" + str(self.store)

#Step 4: Making the agents move, uses a random number generator to decide direction in x or y independently.
    def move(self):
        if random.random()<0.5:
          self.x=self.x+1
        else:
           self.x=self.x-1
        if random.random()<0.5:
            self.y=self.y+1
        else:
            self.y=self.y-1
#Step 5: Simply stopping the agents from teleporting between x and y limits.
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.x>99:
            self.x=99
        if self.y>99:
            self.y=99
            
#Step 6: Defining 'eating' parameters, limiting each agent to 'eating' 10 units. 
    def eat(self):
        if self.environment[self.y][self.x]>10:
            self.environment[self.y][self.x] -=10
            self.store +=10

#Step 7: Defining sharing parameters, if agents come within the predetermined 'neighbourhood' distance they will split there 'food' in half.  
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
           

#Step 8: Definig the distance between agents, this facilitates the 'share_with_neighbours' function initialisation.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    
