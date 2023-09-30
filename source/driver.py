

import numpy as np
import matplotlib.pyplot as plt
from launch.py import launch_angle_range

def main():
    # Define the range of alpha values
    alpha_values = np.linspace(0.01, 0.5, 100)

    # Define the tolerances for alpha and theta
    tol_alpha = 0.04
    tol_theta = 5

    # Create empty lists for the minimum and maximum launch angles
    min_angles = []
    max_angles = []

    # Iterate over the alpha values and compute the valid launch angles for each
    for alpha in alpha_values:
        valid_angles = launch_angle_range((200, 400), 2.0, alpha, tol_alpha, tol_theta)
        if len(valid_angles) > 0:
            min_angles.append(min(valid_angles))
            max_angles.append(max(valid_angles))
        else:
            min_angles.append(None)
            max_angles.append(None)

    # Plot the minimum and maximum launch angles as functions of alpha
    plt.plot(alpha_values, min_angles, label='Minimum angle')
    plt.plot(alpha_values, max_angles, label='Maximum angle')
    plt.xlabel('Alpha')
    plt.ylabel('Launch angle (degrees)')
    plt.legend()
    plt.savefig('figures/angle_vs_alpha.png')

    # Compute the maximum height as a function of alpha
    ve_v0 = 2.0
    g = 9.81
    max_heights = [(ve_v0**2 / (2*g)) * (np.sin(alpha)**2) for alpha in alpha_values]

    # Plot the maximum height as a function of alpha
    plt.figure()
    plt.plot(alpha_values, max_heights, label='Maximum height')
    plt.xlabel('Alpha')
    plt.ylabel('Maximum height (m)')
    plt.legend()
    plt.savefig('figures/height_vs_alpha.png')

if __name__ == '__main__':
    main()

