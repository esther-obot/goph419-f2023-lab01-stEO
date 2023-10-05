import numpy as np
import matplotlib.pyplot as plt

from launch import (launch_angle_range, min_altitude_ratio,  max_altitude_ratio,  min_velocity_ratio,  max_velocity_ratio )


#Question 3
def main():
    # Define the range of alpha values to plot

    ve_v0= 2.0 
    alpha_min=min_altitude_ratio(ve_v0)
    alpha_max= max_altitude_ratio(ve_v0)
    alpha_values = np.linspace(alpha_min,alpha_max,50)

    # Define the tolerance for maximum altitude
    tol_alpha = 0.04
    

    # Compute the minimum and maximum launch angles at each alpha value using launch_angle_range
    min_angles = np.zeros_like(alpha_values)
    max_angles = np.zeros_like(alpha_values)
    for k in range (len(alpha_values)):
        alpha=alpha_values[k]
        angles_min,angles_max = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles[k]=angles_min
        max_angles[k]=angles_max



    # Plot the minimum and maximum launch angles as functions of alpha
    plt.plot(alpha_values, np.rad2deg(min_angles), label='Minimum angle')
    plt.plot(alpha_values, np.rad2deg(max_angles), label='Maximum angle')
    plt.xlabel('Maximum Altitude Ratio (alpha)')
    plt.ylabel('Launch Angle (degrees)')
    plt.legend()
    plt.savefig('../figure/launch_angles_alpha.png')
    plt.show()

if __name__ == '__main__':
    main()
 
 #question4
def main():
    # Define the range of ve_v0 values to plot
    alpha = 0.25
    ve_v0_min=min_velocity_ratio(alpha)
    ve_v0_max= max_velocity_ratio(alpha)
    ve_v0_values = np.linspace(ve_v0_min,ve_v0_max,50)
    
    ve_v0_values = np.linspace(ve_v0_min,ve_v0_max)

    # Define the tolerance for maximum altitude
    tol_alpha = 0.04

    # Create empty lists for the minimum and maximum launch angles
    min_angles = np.zeros_like(ve_v0_values)
    max_angles = np.zeros_like(ve_v0_values)

    # Iterate over the ve_v0 values and compute the valid launch angles for each
    for k in range (len(ve_v0_values)):
        ve_v0=ve_v0_values[k]
        angles_min,angles_max = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles[k]=angles_min
        max_angles[k]=angles_max

    # Plot the minimum and maximum launch angles as functions of ve_v0
    plt.plot(ve_v0_values, np.rad2deg(min_angles), label='Minimum angle')
    plt.plot(ve_v0_values, np.rad2deg(max_angles), label='Maximum angle')
    plt.xlabel('Velocity Ratio (ve_v0)')
    plt.ylabel('Launch Angle (degrees)')
    plt.legend()
    plt.savefig('../figure/launch_angles_vev0.png')
    plt.show()

if __name__ == '__main__':
    main()

