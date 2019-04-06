# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:09:33 2018

Tom Wilson (170006714)
Part of Data Science MSc 
AC52050 Programming Languages for Data Science

THIS CODE IS JUST FOR VISUALISATIONS SEE ZOMBIE MASTER FOR DATASETS REQUIRED FIRST

"""

import matplotlib.pyplot as plt

results_arr = np.array(results)
                                              
#plot changes in totals over time           
plt.figure()
plt.plot(results_arr[0], results_arr[1], label='Living humans')
plt.plot(results_arr[0], results_arr[3], label='Zombies')
plt.plot(results_arr[0], results_arr[2], label='Dead humans')
plt.plot(results_arr[0], results_arr[4], label='Destroyed zombies')
plt.xlabel('Hours from outbreak')
plt.ylabel('Population')
plt.title('Figure 2.2.1 \nZombie infection simulation with random walk of zombies')
plt.legend(loc=0)  


#plot locations from location dict
xlocs = [i[0][0] for i in population_locs.values()]
ylocs = [i[0][1] for i in population_locs.values()]      
plt.figure()
plt.scatter(xlocs, ylocs)

xlocs = [i[0][0] for i in p1.values()]
ylocs = [i[0][1] for i in p1.values()]  
xlocs2 = [i[0][0] for i in p2.values()]
ylocs2 = [i[0][1] for i in p2.values()]     
plt.figure()
plt.scatter(xlocs, ylocs)
plt.scatter(xlocs2, ylocs2, color = [1,0,0])
    
####Plot zombie walk
    
zombie_walk1_x = [i[0] for i in population_locs[482]]
zombie_walk1_y = [i[1] for i in population_locs[482]]

zombie_walk2_x = [i[0] for i in population_locs[5]]
zombie_walk2_y = [i[1] for i in population_locs[5]]


plt.figure()
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.5, pad = 0.1)
plt.text(zombie_walk1_x[0], zombie_walk1_y[0], 'start', color = [0,0,1],bbox=bbox_props)
plt.text(zombie_walk1_x[-1], zombie_walk1_y[-1], 'end', color = [0,0,1],bbox=bbox_props)
plt.text(zombie_walk2_x[0], zombie_walk2_y[0], 'start', color = [1,0,0],bbox=bbox_props)
plt.text(zombie_walk2_x[-1], zombie_walk2_y[-1], 'end', color = [1,0,0],bbox=bbox_props)
plt.plot(zombie_walk1_x, zombie_walk1_y, lw = 0.5, label = 'zombie walk 1')
plt.plot(zombie_walk2_x, zombie_walk2_y, lw = 0.5, color = [1,0,0], label = 'zombie walk 2')
plt.xlabel('X coord')
plt.ylabel('Y coord')
plt.title('Figure 2.2.1 \nRandom walk of two zombies on 100X100 grid')
plt.legend(loc=0)  

##Plot separate pops and zombie crossing between

xlocs = [i[0][0] for i in population_locs.values()]
ylocs = [i[0][1] for i in population_locs.values()]      
plt.figure()
      
zombie_walk1_x = [i[0] for i in population_locs[44]]
zombie_walk1_y = [i[1] for i in population_locs[44]]

plt.figure()
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.5, pad = 0.1)
plt.text(zombie_walk1_x[0], zombie_walk1_y[0], 'start', color = [0,0,1],bbox=bbox_props)
plt.text(zombie_walk1_x[-1], zombie_walk1_y[-1], 'end', color = [0,0,1],bbox=bbox_props)
plt.text(1, -2,'Population A')
plt.text(300, 400,'Population B')
plt.plot(zombie_walk1_x, zombie_walk1_y, lw = 0.5, label = 'Zombie reaching Pop B')
plt.scatter(xlocs, ylocs, color = [0,1,0], s=[0.7])
plt.xlabel('X coord')
plt.ylabel('Y coord')
plt.title('Figure 2.3.1 \nInitial location of individuals in populations A and B\n and random walk of zombie travelling between them')
plt.legend(loc=0) 

##Plot human fleeing zombies

human_walk1_x = [i[0] for i in population_locs[420]]
human_walk1_y = [i[1] for i in population_locs[420]]

human_walk2_x = [i[0] for i in population_locs[424]]
human_walk2_y = [i[1] for i in population_locs[424]]

plt.figure()
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.5, pad = 0.1)
plt.text(human_walk1_x[0], human_walk1_y[0], 'start', color = [0,0,1],bbox=bbox_props)
plt.text(human_walk1_x[-1], human_walk1_y[-1], 'end', color = [0,0,1],bbox=bbox_props)
plt.text(human_walk2_x[0], human_walk2_y[0], 'start', color = [0,0,0],bbox=bbox_props)
plt.text(human_walk2_x[-1], human_walk2_y[-1], 'end', color = [0,0,0],bbox=bbox_props)
xlocs = [i[-1][0] for i in population_locs.values()]
ylocs = [i[-1][1] for i in population_locs.values()] 
axes = plt.gca()
axes.set_xlim([-1000,300])
axes.set_ylim([0,650])
plt.scatter(xlocs, ylocs, color = [1,0,0], s=[0.9])
plt.plot(human_walk1_x, human_walk1_y, lw = 0.5, label = 'Human walk 1')
plt.plot(human_walk2_x, human_walk2_y, lw = 0.5, label = 'Human walk 2', color = [0,0,0])
plt.xlabel('X coord')
plt.ylabel('Y coord')
plt.title('Figure 2.6.1 Deliberate Walk of Humans Away from Zombies')
plt.legend(loc=0) 