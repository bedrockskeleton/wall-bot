from buildhat import Motor, ColorSensor

class Follower:
    def __init__(self):
        self.left = Motor('A') # Left motor
        self.right = Motor('B') # Right motor
        self.wheels = [self.left, self.right] # Putting each motor in a list so it's easier to manipulate both
        [x.stop() for x in self.wheels] # Stopping both wheels
        
        speed = 25 # Default speed
        self.left.set_default_speed(-speed) # Left motor is reversed because it's attached backwards
        self.right.set_default_speed(speed)
        
        self.sensor = ColorSensor('C') # Color sensor
        self.color = 'black' # The color the robot looks for
        self.error = 'red' # This color stops the robot
        self.start = False
    
    def run(self):
        left = True
        self.start = True # Setting start variable to true
        while self.start:
            print(left, self.sensor.get_color()) # Showing the direction and color in console
            if self.sensor.get_color() == self.color: # If the bot sees the line, do nothing
                pass
            elif self.sensor.get_color() == self.error: # If the bot sees the border of the box, stop
                self.end()
            else: # If the bot sees anything else, turn the other direction
                self.turn(left)
                while self.sensor.get_color() != self.color: # Stall the program until it sees the line again
                    pass
                left = not left # Swap turning directions
            
    def turn(self, left):
        if left:
            self.left.stop()
            self.right.start()
            # Stops left motor and starts the right, turning the vehicle left
        else:
            self.right.stop()
            self.left.start()
            # Stops right motor and starts the left, turning the vehicle right

    
    def end(self):
        self.start = False
        [x.stop() for x in self.wheels] # Stops both motors
        
    def debug_color(self):
        while True:
            print(self.sensor.get_color())

bot = Follower()

bot.run()