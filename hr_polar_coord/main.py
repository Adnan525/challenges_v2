# argand driagram to plot complex numbers in polar coordinates
import math

def get_polar_coord(z: str) -> tuple:
    try:
        c = complex(z)
        r = math.sqrt(c.real**2 + c.imag**2)
        theta = math.atan2(c.imag, c.real)
        return (round(r, 4), round(theta, 4))
    except ValueError:
        raise ValueError("Invalid complex number format")
    
if __name__ == "__main__":
    complex_number = input().strip()
    for element in get_polar_coord(complex_number):
        print(element)
        