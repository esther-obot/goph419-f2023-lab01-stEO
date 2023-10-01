"""Tests for GOPH 419 Lab Assignment #1."""
import numpy as np
from source.launch import launch_angle_range
# for question 2
def test_launch_angle_range():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02

    # expected results computed by hand
    expected_min_phi = 0.0467
    expected_max_phi = 0.3623

    # actual results computed using launch_an3 gle_range
    actual_phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
    actual_min_phi = actual_phi_range[0]
    actual_max_phi = actual_phi_range[1]

    # print expected and actual ranges
    print(f"Expected range: ({expected_min_phi:.4f}, {expected_max_phi:.4f})")
    print(f"Actual range: ({actual_min_phi:.4f}, {actual_max_phi:.4f})")

    # compare expected and actual results
    assert abs(expected_min_phi - actual_min_phi) < 1e-4
    assert abs(expected_max_phi - actual_max_phi) < 1e-4

test_launch_angle_range()






