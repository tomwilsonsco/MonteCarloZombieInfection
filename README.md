The aim is to show how a zombie apocalypse can be modelled using a random walk simulation to capture the speed and movement of zombies and human victims. 
A mathematical model was developed by Munz et al (2009) to simulate a zombie outbreak over time. 
This was later implemented in Python by Campo (2011) and considered the following factors:
1.	the number of susceptible victims
2.	the number of zombies
3.	the number of people "killed"
4.	the population birth rate
5.	the chance of a natural death
6.	the chance the "zombie disease" is transmitted (an alive person becomes a zombie)
7.	the chance a dead person is resurrected into a zombie
8.	the chance a zombie is destroyed

For this assignment, code was developed in Python to include a random walk in addition to the above factors, allowing distances between infected and non-infected populations to be modelled. Simulating the geographic spread of an outbreak is often considered in modelling spread of infectious diseases.  Random Walks are used in scientific modelling, for example in ecology to simulate the movement of an animal (Fagan and Calabrese 2014) and in chemistry for modelling chemical gas diffusion (Le Claire, 1958).

This report will describe code developed and simulation results in three separate sections as more complexity is added to the simulation:
1.	The basic random walk developed to simulate the speed and movement of zombies and its impact on the infection rate of a population.
2.	Modelling the spread between geographically separate populations with only one population centre initially being susceptible to rising dead.
3.	Including the movement of humans in response to zombie movement in the model.

References
Munz, P., Hudea, I., Imad, J. and Smith, R.J., 2009. When zombies attack!: mathematical modelling of an outbreak of zombie infection. Infectious disease modelling research progress, 4, pp.133-150.
Campo, C, 2011. "Modelling a Zombie Apocalypse", accessed online at http://scipy-cookbook.readthedocs.io/items/Zombie_Apocalypse_ODEINT.html  May 2018.
