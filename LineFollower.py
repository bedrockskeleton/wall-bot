from buildhat import Motor, ColorSensor
import time
import math
from math import pi
import numpy as np

class Wheel:
    def __init__(self, port, reverse = False):
        self.motor = Motor(port)
        if reverse:
            self.motor.reverse()
            
class Follower:
    def __init__(self):
        self.left = Wheel('A')
        self.right = Wheel('B')
        self.wheels = [self.left.motor, self.right.motor]
        [x.stop() for x in self.wheels]
        
        speed = 25
        self.left.motor.set_default_speed(-speed)
        self.right.motor.set_default_speed(speed)
        
        self.sensor = ColorSensor('C') # Color sensor
        self.color = 'black' # The color the robot looks for
        self.start = False
        
    def run(self):
        left = True
        self.start = True
        while self.start: # While robot is started
            print(left, self.sensor.get_color())
            if left: # Sweeps the robot left over the line
                if self.sensor.get_color() == self.color: # If the initial color is black, sweep until the robot leaves it
                    self.right.motor.start()
                    while self.sensor.get_color() == self.color:
                        pass
                    self.right.motor.stop()
                    left = False
                else:
                    self.right.motor.start()
                    while self.sensor.get_color() != self.color:
                        pass
                    self.right.motor.stop()                    
            else:
                if self.sensor.get_color() == self.color:
                    self.left.motor.start()
                    while self.sensor.get_color() == self.color:
                        pass
                    self.left.motor.stop()
                    left = True
                else:
                    self.left.motor.start()
                    while self.sensor.get_color() != self.color:
                        pass
                    self.right.motor.stop()
            
    def end(self):
        self.start = False
        [x.stop() for x in self.wheels]
        
    def debug_color(self):
        while True:
            print(self.sensor.get_color())

bot = Follower()

bot.end()