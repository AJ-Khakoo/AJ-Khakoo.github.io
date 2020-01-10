import random
import operator
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import Wolf


#creating environments
environment=[]
rowlist=["rowlist"]

with open('in.txt') as f:
    for row in f:
        parsed_line = str.split(row,",")
        rowlist=[]
        for coordinate in parsed_line:
            rowlist.append(float(coordinate))
        environment.append(rowlist)
        

#Agent Parameters
num_of_agents = 50
#num_of_iterations = 100
neighbourhood = 10
agents = []
#Wolf Parameters
num_of_wolf = 1
neighbourhood_wolf = 10
wolf = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
for j in range(num_of_wolf):
    agents.append(Wolf.wolf(environment, wolf))

carry_on = True	

#Agents Move, Eat and Share
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat ()
        agents[i].share_with_neighbours(neighbourhood)
        wolf[j].attack()
        wolf[j].wolf_move()
#Agent stopping condition, I.E wolf attack and kill function
def attack(self, neighbourhood_wolf):
    for agent in self.agents, self.wolf:
        attack = self.distance_between_wolf(agent)
    if attack <= neighbourhood:
        random.random <= 0
        agent, carry_on = False


    
   
#plotting agents
    for i in range(num_of_agents, num_of_wolf):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.scatter(wolf[j].wolfx, wolf[j].wolfy)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

#Changing the Stopping Parameters
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100)& (carry_on) :  
        yield a			# Returns control and waits next call.
        a = a + 1
        
#Animating The Agents

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#Running the Model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

    
    
# Creating General User Interface
root = tkinter.Tk()
root.wm_title("Model")
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
