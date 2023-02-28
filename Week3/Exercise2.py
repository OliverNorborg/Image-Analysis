
"""Exercise 2 - week 3 Cameras and Lenses"""

import math
import numpy as np

#Exercise 1) 
#Explain how to calculate the angle when the opposite and adjasent 
#side is given 

#it is calculated using tangent. Tangent of angle equals the opposite side 
# divided by the adjasent side. In order to get the angle you take the 
# arc tangent. 

#Exercise 2) 
def camera_b_distance(f,g):
    """
    camera_b_distance returns the distance (b) where the CCD should be placed 
    when the object distance (g) and the focal length (f) are given
    
    Parameters
    ----------
    f : INT
        Focal length (mm).
    g : INT
        Object Distance (m).

    Returns
    -------
    b : INT 
        distance where CCD should be placed (meter)
    """
    #We first convert focal length into meters
    f = f*0.001
    
    b = -(g*f)/(f-g)
    return b


focal_length = 15
object_distance = [0.1,1,5,15]
for i in range(len(object_distance)):
    print(camera_b_distance(focal_length, object_distance[i]))
    
#We can see that as the objects distance increases the distance to CCD
# gravitate towards the focal length


# Exercise 3)






















