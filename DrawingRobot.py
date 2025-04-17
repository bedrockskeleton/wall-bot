from buildhat import Motor
import time
import math
from math import pi

class Pulley:
    def __init__(self, port, rot_direction=False):
        self.port = port
        self.motor = Motor(port)
        if rot_direction:
            self.rot_direction = -1
        else:
            self.rot_direction = 1
        self.pDiameter = 0.94 # Diameter of pulley in inches
        
    def extend(self, distance):
        rotations = distance / (pi * self.pDiameter)
        self.motor.run_for_rotations(self.rot_direction * rotations)    
    
    def calibrate(self, distance):
        # Retracts pulleys until they stop, then extends them to the given distance
        self.motor.run_for_seconds(10, -50 * self.rot_direction)
        self.extend(distance)
        

pLeft = Pulley('A', True)
pRight = Pulley('B')

pSeparation = 4.34 # Distance between the two pulley points in inches

pLeft.calibrate(6)
pRight.calibrate(6)