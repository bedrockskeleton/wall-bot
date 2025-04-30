# Wall-Bot

# What is Raspberry Pi
The Raspberry Pi is a small, low-cost computer about the size of a credit card. It was created by the Raspberry Pi Foundation to help people, especially students, learn about computers and programming. Even though it’s tiny and affordable, it can do many things a regular computer can do, like browsing the internet, watching videos, playing games, and writing documents. It has a processor, memory (RAM), USB ports for keyboard and mouse, an HDMI port for connecting to a screen, and uses a microSD card for storage. People use Raspberry Pi for fun and creative projects like building robots, making smart home systems, setting up weather stations, or creating retro video game consoles. It supports simple programming languages like Python and Scratch, making it great for beginners. Because it’s cheap, easy to use, and very versatile, Raspberry Pi is popular among students, teachers, and tech hobbyists around the world.

![image](https://github.com/user-attachments/assets/32da7c9e-c094-47df-b7ef-89e8f2c31c7e)

# How Is Raspberry Pi Composed 
The Raspberry Pi is made up of many small parts that are all placed on a tiny green board. These parts work together to make it a working computer. The most important part is the processor, which is like the brain. It does all the thinking and runs the programs. It also has RAM, which is memory that helps it work faster and do more things at once.

The Raspberry Pi has USB ports where you can plug in a mouse, keyboard, or USB stick. It has an HDMI port, which lets you connect it to a monitor or TV so you can see what you're doing. Instead of a big hard drive, it uses a microSD card. This card holds the operating system and all your files, like pictures or documents.

It also has a power port where you plug in a charger to give it electricity. Most models have Wi-Fi and Bluetooth built in, so you can connect to the internet or other devices without wires. There is also a special row of metal pins called GPIO pins. These pins let you connect things like lights, buttons, and sensors, so you can build cool projects.

All these parts are put together on the board in a factory using special machines. Even though the Raspberry Pi is very small, it has everything you need to use it like a computer or to build fun and creative projects.
# The Wall-Bot to the Line Following-Bot
The Wall bot was the original plan of the project. The Wall bot was composed of two strings, two small angular motors, and the white board. The idea was to measure the length and the width of the white board and program the Wall Bot to draw on the white board. But unfortunately the idea had a lot of problems coming. We thought the battery was to hevavy for the Wall Bot to climb so we started moving it diffrent ways to balance the weight out. We first put the battery across the bottom of the robot, then when we hung it on the white board, and the top of the robot was away from the white board. So then we changed the weight of the battery and moved it to lay across the top to bottom of the robot. That ended up making the weight distribution worse. We finally figured it out by laying the battery across the top of the robot which then made it lay flat on the white board which would help the robot go up and down the white board. But that was not the main problem that we were actually going to face during this project. The main problem was going to be the angular motors. The motors were not strong enough to climb up the white board with or without the battery weight attached to the robot. 

So we decided to change or original idea of the Wall Bot to the Car Bot. The Car Bot is composed of two angular motors, two samll wheels, and a sensor camrea, The Car Bot has a camera at the bottom of the Raspberry pi near the wheels. The Car bot is suppose to detect the diffrent colors and move around when it identify the color.

# Wall Bot Code VS Line Following Bot Code

```
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
        self.motor.run_for_rotations(self.rot_direction * rotations, blocking=False)
        self.length += distance
    
    def calibrate(self, distance):
        # Retracts pulley by the maximum distance, then extends it to the given distance
        self.extend(-self.maxLength)
        self.extend(distance)
        self.length = distance
        
    def release(self, release):
        self.motor.release = release
  ```
We had to create a class called Pulley which rotated the motors and we had to make the turn of the motors into a distance integer so that we could get it to calibrate and release the same distance wit each motor. With the Line Following Bot we were able to make it simplier because it will move forward by the wheels turning left until it sees the black line and right until it sees the black line. So there was no math conversion that needed to be created when coding this so that it just uses a basic algorithm to move the robot.



