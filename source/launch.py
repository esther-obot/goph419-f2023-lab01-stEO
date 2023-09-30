"""Functions for GOPH 419 Lab Assignment #1."""

import numpy as np
import math



def arcsin(x):
    """Compute the inverse sine of x on the range [-pi/2, pi/2].
    """
    n=0
    n_max=500
    eps_a=1
    eps_s=0.5e-5
    result=0
    while eps_a>eps_s and n<=n_max:
        upper_part=(2*x)**(2*n)
        lower_part=(n**2)*(math.fractori(2*n))/(math.fractori(n))**2
        term=0.5*upper_part/lower_part
        result +=term
        n +=1
        return np.sqrt(result)



def launch_angle(ve_v0, alpha):
    sin_theta = (1 + alpha) * (np.sqrt(1 - ((alpha / (1 + alpha)) * (ve_v0 ** 2))))
    launch_angle = arcsin(sin_theta)
    return launch_angle
       
   
def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Calculate the range of launch angles for a given
    velocity ratio, target altitude ratio, and tolerance.

    Returns the input values as well as the minimum and
    maximum launch angles.
    """
    min_alt=(1-tol_alpha)*alpha
    max_alt=(1+tol_alpha)*alpha
    min_phi= launch_angle(ve_v0,min_alt)
    max_phi= launch_angle(ve_v0,max_alt)

    # Return the input values and calculated angles as a tuple
    return min_phi,max_phi


def min_altitude_ratio(ve_v0):
    """Utility function for computing minimum possible peak altitude ratio
    for a given velocity ratio.
    """
    min_alt = ((ve_v0 ** 2)-2)/((1-(ve_v0 ** 2)))
    return min_altitude_ratio

def max_altitude_ratio(ve_v0):
    """Utility function for computing maximum possible peak altitude ratio
    for a given velocity ratio.
    """
    max_alt = 1/((ve_v0 ** 2)-1)
    return max_alt



def min_velocity_ratio(alpha):
    """Utility function for computing minimum possible velocity ratio
    for a given target peak altitude ratio.
    """
    min_vel=np.sqrt((2+alpha)/(1+alpha))
    return min_vel
   

def max_velocity_ratio(alpha):
    """Utility function for computing maximum possible velocity ratio
    for a given target peak altitude ratio.
    """
    max_vel = np.sqrt((1 + alpha) / alpha)
    return max_vel