import numpy as np
import matplotlib.pyplot as plt
from launch import launch_angle_range

#Question 3
def main():
    # Define the range of alpha values to plot
    alpha_values = np.linspace(0.01, 0.99, 100)

    # Define the tolerance for maximum altitude
    tol_alpha = 0.04

    # Compute the minimum and maximum launch angles at each alpha value using launch_angle_range
    min_angles = []
    max_angles = []
    for alpha in alpha_values:
        angles = launch_angle_range(2.0, alpha, tol_alpha)
        min_angles.append(angles[0])
        max_angles.append(angles[1])

    # Plot the minimum and maximum launch angles as functions of alpha
    plt.plot(alpha_values, np.rad2deg(min_angles), label='Minimum angle')
    plt.plot(alpha_values, np.rad2deg(max_angles), label='Maximum angle')
    plt.xlabel('Maximum Altitude Ratio (alpha)')
    plt.ylabel('Launch Angle (degrees)')
    plt.legend()
    plt.savefig('figures/launch_angles_alpha.png')
    plt.show()

if __name__ == '__main__':
    main()
 
 #question4
def main():
    # Define the range of ve_v0 values to plot
    ve_v0_values = np.linspace(1.01, 2.5, 100)

    # Define the target maximum altitude ratio
    alpha = 0.25

    # Define the tolerance for maximum altitude
    tol_alpha = 0.04

    # Create empty lists for the minimum and maximum launch angles
    min_angles = []
    max_angles = []

    # Iterate over the ve_v0 values and compute the valid launch angles for each
    for ve_v0 in ve_v0_values:
        angles = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(angles[0])
        max_angles.append(angles[1])

    # Plot the minimum and maximum launch angles as functions of ve_v0
    plt.plot(ve_v0_values, np.rad2deg(min_angles), label='Minimum angle')
    plt.plot(ve_v0_values, np.rad2deg(max_angles), label='Maximum angle')
    plt.xlabel('Velocity Ratio (ve_v0)')
    plt.ylabel('Launch Angle (degrees)')
    plt.legend()
    plt.savefig('figures/launch_angles_vev0.png')
    plt.show()

if __name__ == '__main__':
    main()

