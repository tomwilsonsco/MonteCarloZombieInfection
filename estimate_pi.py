import random
import numpy as np

"""Square of 1 by 1 and circle of radius 0.5 inside it
area of this circle is pi*(0.5)^2 = pi/4
ratio of area of circle to area of square is (pi/4)/1 = pi/4

If use Monte Carlo simulation can est ratio of circle area to square area.
Can randomly place points inside square and they can fall inside or outside of circle
if run this n times and keep a count of whether within circle or just square:

pi / 4 approximately = count inside circle / total count
and therefore:

pi approximately = (count inside circle / total count) * 4
Code below does this, using np.linalg.norm to calc euclidean distance to circle centre
and therefore determine is point distance to centre less than or greater than circle radius"""

number_of_tests = 100000

inside_circle, outside_circle = 0, 0

for i in range(0, number_of_tests):
    rand_point = np.array([random.uniform(0, 1), random.uniform(0, 1)])
    point_dist = np.array([0.5, 0.5])
    dist = np.linalg.norm(rand_point - point_dist)
    if dist < 0.5:
        inside_circle += 1
    else:
        outside_circle += 1

pi_est = (inside_circle / (inside_circle + outside_circle)) * 4

print(pi_est)
