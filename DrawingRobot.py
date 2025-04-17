from buildhat import Motor
import time
import math
from math import pi
import numpy as np

class Pulley: # Pulley class deals with the motors directly
    def __init__(self, port, rot_direction=False):
        self.port = port
        self.motor = Motor(port)
        self.length = 0
        self.maxLength = 60 # Maximum length that the pulley can extend to
        if rot_direction:
            self.rot_direction = -1
        else:
            self.rot_direction = 1
        self.pDiameter = 0.94 # Diameter of pulley in inches
        
    def extend(self, distance): # Converts distance to motor rotations
        rotations = distance / (pi * self.pDiameter)
        self.motor.run_for_rotations(self.rot_direction * rotations)
        self.length += distance
    
    def calibrate(self, distance):
        # Retracts pulley by the maximum distance, then extends it to the given distance
        self.extend(-self.maxLength)
        self.extend(distance)
        self.length = distance

class WallBot: # WallBot class coordinates the two pulleys
    def __init__(self):
        self.left = Pulley('A', True)
        self.right = Pulley('B')
        self.pulleys = [self.left, self.right]
        self.wallWidth = 38
        self.pulleySeparation = 4.15
        [pul.calibrate(36) for pul in self.pulleys] # Calibrate both pulleys to 36 inches (3 feet)

    def calibrate(self, distance): # Dual-calibration function
        [pul.calibrate(distance) for pul in self.pulleys]

    def extend(self, distance): # Extends both pulleys together
        [pul.extend(distance) for pul in self.pulleys]

    def getCoords(self): # Use math to return the X/Y coordinates of the wallbot
        pass

    def moveTo(self, x, y): # Converts X/Y coordinates to lengths for the pulleys
        # Bottom points of the self.pulleySeparation base
        xLeft = x - self.pulleySeparation / 2
        xRight = x + self.pulleySeparation / 2

        # Left Pulley: from top-left (0, 0) to robot left
        newLeft = np.sqrt(xLeft**2 + y**2)
        self.left.extend(self.left.length - newLeft)

        # Right Pulley: from top-right (self.wallWidth, 0) to robot right
        newRight = np.sqrt((self.wallWidth - xRight)**2 + y**2)
        self.right.extend(self.right.length - newRight)

wallbot = WallBot()