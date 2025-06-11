# Your job is to return the volume of a cup when given the diameter of the top, 
# the diameter of the bottom and the height.
# You know that there is a steady gradient from the top to the bottom.
# Inputs will be in range 1 <= dTop, dBotton, height <= 10_000.
# You do not need to do any rounding. Your answer will be checked with tolerance of 0.01.
# =======================================================================================
import math


def cup_volume(d1, d2, height):
    """
    Calculate the volume of a cup given the diameters of the top and bottom and the height.
    
    Parameters:
    d1 (float): Diameter of the top of the cup.
    d2 (float): Diameter of the bottom of the cup.
    height (float): Height of the cup.
    
    Returns:
    float: Volume of the cup.
    """
    r1 = d1 / 2
    r2 = d2 / 2
    
    volume = (1/3) * math.pi * height * (r1**2 + r1*r2 + r2**2)
    
    return volume
