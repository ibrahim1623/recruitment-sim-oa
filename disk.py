import numpy as np


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    g = 9.81
    # intial potential energy
    PE = mass * g * height
    # normal force that gets applied
    normal_force = mass * g * np.cos(np.radians(incline))
    # force applied by friction
    friction_force = friction * normal_force
    # calculate total work done
    work = friction_force * length
    # calculate net energy leftover
    net_energy = PE - work

    if net_energy <= 0:
        return 0
    else:
        np.sqrt(4 * net_energy / (3 * mass))
