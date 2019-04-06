# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:42:13 2018

Tom Wilson (170006714)
Part of Data Science MSc 
AC52050 Programming Languages for Data Science

"""
import random, numpy as np

# Simulation Options: 'basic', 'geographic separate', 'human movement', 'all complex'
#all complex can run for 20 mins +
run_type = 'human movement'

###########################################################################################
"""Define functions"""

def random_step(x,y):
    dx = random.choice([-1,0,1])
    dy = random.choice([-1,0,1])
    x += dx
    y += dy
    return (x,y)

def walk_subset(subset, d):
    for key, value in d.items():
        if key in subset:
            value.append(random_step(value[-1][0], value[-1][1])) 
            #value.pop(1) #to only keep most recent coordinate otherwise comment out
    return d

    
def compare_locations(lista, listb):
    listadict = dict((k, population_locs[k][-1]) for k in lista)
    listbdict = dict((k, population_locs[k][-1]) for k in listb)
    listacoords = [v for v in listadict.values()]
    listbcoords = [v for v in listbdict.values()]
    listaout = [key for key, value in listadict.items() if value in listbcoords]
    listbout = [key for key, value in listbdict.items() if value in listacoords]
    return listaout, listbout
    
    
def outcome_test(prob):
    return random.random() < prob

def switch_list_vals(val, removelist, addlist):
    removelist.remove(val)
    addlist.append(val)
    return removelist, addlist

def return_outcomes(input_list, prob):
    newl = []
    for i in input_list:
        if outcome_test(prob):
            input_list, newl = switch_list_vals(i, input_list, newl)
    return input_list, newl

def search_meetings(h, z, d, r):
    hmeet, zmeet = compare_locations(h, z)
    for hm in hmeet:
        for zm in zmeet:
            if hm in h and zm in z: #make sure not already changed state
                if outcome_test(A):
                    print("Human {} destroyed zombie {}!".format(hm, zm))
                    switch_list_vals(zm, z, r)
                else:
                    print("Zombie {} kills human {}!".format(zm, hm))
                    switch_list_vals(hm, h, d)
    return h, z, d, r

def add_current_counts(res, vals):
    for i in range(0,len(vals)):
        res[i].append(vals[i])
    return res

#For two  geographically separate populations
    
def search_meetings_sep(h, z, d, r, cityB):
    hmeet, zmeet = compare_locations(h, z)
    for hm in hmeet:
        for zm in zmeet:
            if hm in h and zm in z: #make sure not already changed state
                if outcome_test(A):
                    print("Human {} destroyed zombie {}!".format(hm, zm))
                    switch_list_vals(zm, z, r)
                else:
                    print("Zombie {} kills human {}!".format(zm, hm))
                    if not cityB and hm >= 500:
                        cityB = True
                        print('!!! Zombies have infected population B !!!')
                    switch_list_vals(hm, h, d)
    return h, z, d, r, cityB

# For human movement:

def compare_vals(v1, v2):
    if v1 < v2:
        return -1
    elif v1 > v2:
        return +1
    else:
        return random.randint(-1, 1)

#For human movement away from nearest zombie by Euclidean distance:
def move_humans(humans, zombies, population_locs):
    zombielocs = np.asarray([population_locs[i][-1] for i in zombies])
    for h in humans:
        coord = population_locs[h][-1]
        closest_zom = population_locs[zombies[np.argmin(np.sum((zombielocs - coord)**2, axis=1))]][-1]
        population_locs[h].append((coord[0] + compare_vals(coord[0],closest_zom[0]), coord[1] + compare_vals(coord[1], closest_zom[1])))
    return population_locs

###############################################################################################
"""Parameters and while loop for basic run of script"""

if run_type == 'basic':
   
    p = 500 #starting population
    
    d = 0.001 # probability of natural death
    G = 0.01 #probability of resurrection of zombie
    A = 0.2 #probability of human destroying zombie on encounter
    
    mt = 1000 # Optional Length of time over which the model is run 
    zs = 5#Number of zombie moves per time increment (read zombie speed)
    di = int(p/100) # 1% of initial population is dead
    
    # generate initial location dictionary for population on 100X100 grid
    population_locs = dict([(i, [(random.randint(0, 101), random.randint(0,101))]) for i in range(0,p)])
    
    #Create initial lists
    humans = [i for i in range(0,len(population_locs) - di)] #all pop but 1% initial dead are human
    dead = [i for i in population_locs if i not in humans] #dead is initial 1%
    zombies = [] #No initial zombies in population
    removed = [] #removed are zombies destroyed by humans
    
    results = [[],[],[],[],[]]
    
    """Run while loop for the simulation...."""
    t=0 #initialise t for while loop
    #while len(humans) > 0 and t < mt: #if only want to run for specified time period
    while len(humans) > 0: #or comment out above and run until all humans gone
        humans, new_died = return_outcomes(humans, d)
        dead += new_died
        dead, new_zombies = return_outcomes(dead, G)
        zombies += new_zombies
        # check if humans / zombies meet, and update lists, walk zombies and check again
        for s in range(0, zs + 1):
            # check if zombies in same location as humans
            humans, zombies, dead, removed = search_meetings(humans, zombies, dead, removed)
            # walk zombies
            population_locs = walk_subset(zombies, population_locs)
        
        results = add_current_counts(results, [t, len(humans), len(dead), len(zombies), len(removed)])
        t += 1   
    print("End result: Zombies {}, Humans {}, Dead {}, Destroyed {} in {} hours"
         .format(len(zombies), len(humans),len(dead), len(removed),(t)))
     
        
##################################################################################################
 
"""Parameters and while loop to model separate geographic populations"""

if run_type == 'geographic separate':
    p = 1000 #starting populations

    d = 0.001 # probability of natural death
    G = 0.01 #probability of resurrection of zombie
    A = 0.2 #probability of human destroying zombie on encounter
    
    mt = 1000 # Optional Length of time over which the model is run 
    zs = 10 #Number of zombie moves per time increment (read zombie speed)
    di = int(p/200) # 1% of Population A is dead
    
    # generate initial location dictionary for population A in range 100 by 100 on grid
    population_locs = dict([(i, [(random.randint(0, 101), random.randint(0,101))]) for i in range(0,p - 500)])
    
    # generate locations for population B in range 900, 1000:
    for i in range(500, p):
        population_locs[i] =[(random.randint(300, 401), random.randint(300,401))]
    
    
    #Create initial lists
    humans = [i for i in range(len(population_locs)-1, di -1, -1)] #all pop but 1% of population A are dead
    dead = [i for i in population_locs if i not in humans] #dead is initial 1% of population A
    zombies = [] #No initial zombies in population
    removed = [] #removed are zombies destroyed by humans
    
    results = [[],[],[],[],[]]
    
    """Run while loop for the simulation...."""
    t=0 #initialise t for while loop
    
    arrived_pop_B = False #record when zombies arrive at population B, initially false
    arrived_pop_B_time = None
    
    #while len(humans) > 0 and t < mt: #if only want to run for specified time period
    while len(humans) > 0: #or comment out above and run until all humans gone
        # Population in both locations can die at any time:
        humans, new_died = return_outcomes(humans, d)
        dead += new_died
        # Dead can only rise in Population B once zombies arrive and infect by random walk (ids 500+)
        if arrived_pop_B:
            dead, new_zombies = return_outcomes(dead, G)
            zombies += new_zombies
        else:
            popAdead = [i for i in dead if i < 500]
            popBdead = [i for i in dead if i >= 500]
            popAdead, new_zombies = return_outcomes(popAdead, G)
            zombies += new_zombies
            dead = popAdead + popBdead       
        # check if humans / zombies meet, and update lists, walk zombies and check again
        for s in range(0, zs + 1):
            # check if zombies in same location as humans
            humans, zombies, dead, removed, arrived_pop_B = \
            search_meetings_sep(humans, zombies, dead, removed, arrived_pop_B)
            # walk zombies
            population_locs = walk_subset(zombies, population_locs)
        
        results = add_current_counts(results, [t, len(humans), len(dead), len(zombies), len(removed)])
        if arrived_pop_B and arrived_pop_B_time is None:
            arrived_pop_B_time = t
        t += 1
    
    print("End result: Zombies {}, Humans {}, Dead {}, Destroyed {} in {} hours"
         .format(len(zombies), len(humans),len(dead), len(removed),(t)))
    
    print("Zombies rearched population B in {} hours".format(arrived_pop_B_time))
    
    print("{} zombies created in population B".format(len([z for z in zombies if z > 499])))

##############################################################################################
    
"""Parameters and while loop for human movement simulation"""

if run_type == 'human movement':

    p = 500 #starting population
    
    d = 0.001 # probability of natural death
    G = 0.01 #probability of resurrection of zombie
    A = 0.2 #probability of human destroying zombie on encounter
    
    mt = 2000 # Optional Length of time over which the model is run 
    zs = 5#Number of zombie moves per time increment (read zombie speed)
    di = int(p/100) # 1% of initial population is dead
    
    # generate initial location dictionary for population on 100X100 grid
    population_locs = dict([(i, [(random.randint(0, 101), random.randint(0,101))]) for i in range(0,p)])
    
    #Create initial lists
    humans = [i for i in range(0,len(population_locs) - di)] #all pop but 1% initial dead are human
    dead = [i for i in population_locs if i not in humans] #dead is initial 1%
    zombies = [] #No initial zombies in population
    removed = [] #removed are zombies destroyed by humans
    
    results = [[],[],[],[],[]]
    
    """Select whether humans allowed to move or not"""
    human_movement_allowed = True

    """Run while loop for the simulation...."""
    t=0 #initialise t for while loop
    
    #while len(humans) > 0 and t < mt: #if only want to run for specified time period  
    while len(humans) > 0: #or comment out above and run until all humans gone
        if human_movement_allowed and len(zombies) > 0:
            population_locs = move_humans(humans, zombies, population_locs)
        humans, new_died = return_outcomes(humans, d)
        dead += new_died
        dead, new_zombies = return_outcomes(dead, G)
        zombies += new_zombies
        # check if humans / zombies meet, and update lists, walk zombies and check again
        for s in range(0, zs + 1):
            # check if zombies in same location as humans
            humans, zombies, dead, removed = search_meetings(humans, zombies, dead, removed)
            # walk zombies
            population_locs = walk_subset(zombies, population_locs)
        
        results = add_current_counts(results, [t, len(humans), len(dead), len(zombies), len(removed)])
        t += 1
    
    print("End result: Zombies {}, Humans {}, Dead {}, Destroyed {} in {} hours"
         .format(len(zombies), len(humans),len(dead), len(removed),(t)))

#################################################################################################
"""Parameters and while loop to use both human movement and separate populations
but kill process if runs for more than 15000 time steps"""

"""Parameters and while loop to model separate geographic populations"""

if run_type == 'all complex':
    p = 1000 #starting populations

    d = 0.001 # probability of natural death
    G = 0.01 #probability of resurrection of zombie
    A = 0.2 #probability of human destroying zombie on encounter
    
    mt = 15000 # Optional Length of time over which the model is run 
    zs = 10 #Number of zombie moves per time increment (read zombie speed)
    di = int(p/200) # 1% of Population A is dead
    
    # generate initial location dictionary for population A in range 100 by 100 on grid
    population_locs = dict([(i, [(random.randint(0, 101), random.randint(0,101))]) for i in range(0,p - 500)])
    
    # generate locations for population B in range 900, 1000:
    for i in range(500, p):
        population_locs[i] =[(random.randint(300, 401), random.randint(300,401))]
    
    
    #Create initial lists
    humans = [i for i in range(len(population_locs)-1, di -1, -1)] #all pop but 1% of population A are dead
    dead = [i for i in population_locs if i not in humans] #dead is initial 1% of population A
    zombies = [] #No initial zombies in population
    removed = [] #removed are zombies destroyed by humans
    
    results = [[],[],[],[],[]]
    
    """Select whether humans allowed to move or not"""
    human_movement_allowed = True
    
    """Run while loop for the simulation...."""
    t=0 #initialise t for while loop
    
    arrived_pop_B = False #record when zombies arrive at population B, initially false
    arrived_pop_B_time = None
    
    while len(humans) > 0 and t < mt: #if only want to run for specified time period
    #while len(humans) > 0: #or comment out above and run until all humans gone
        # Population in both locations can die at any time:
        
        humans, new_died = return_outcomes(humans, d)
        dead += new_died
        # Dead can only rise in Population B once zombies arrive and infect by random walk (ids 500+)
        if arrived_pop_B:    
            dead, new_zombies = return_outcomes(dead, G)
            zombies += new_zombies
            if human_movement_allowed and len(zombies) > 0:
                population_locs = move_humans(humans, zombies, population_locs)
        else:
            popAdead = [i for i in dead if i < 500]
            popBdead = [i for i in dead if i >= 500]
            popAdead, new_zombies = return_outcomes(popAdead, G)
            zombies += new_zombies
            dead = popAdead + popBdead
            if human_movement_allowed and len(zombies) > 0:
                population_locs = move_humans([h for h in humans if h < 500], zombies, population_locs)
        # check if humans / zombies meet, and update lists, walk zombies and check again
        for s in range(0, zs + 1):
            # check if zombies in same location as humans
            humans, zombies, dead, removed, arrived_pop_B = \
            search_meetings_sep(humans, zombies, dead, removed, arrived_pop_B)
            # walk zombies
            population_locs = walk_subset(zombies, population_locs)
        
        results = add_current_counts(results, [t, len(humans), len(dead), len(zombies), len(removed)])
        if arrived_pop_B and arrived_pop_B_time is None:
            arrived_pop_B_time = t
        t += 1
    
    print("End result: Zombies {}, Humans {}, Dead {}, Destroyed {} in {} hours"
         .format(len(zombies), len(humans),len(dead), len(removed),(t)))
    
    print("Zombies rearched population B in {} hours".format(arrived_pop_B_time))
    
    print("{} zombies created in population B".format(len([z for z in zombies if z > 499])))