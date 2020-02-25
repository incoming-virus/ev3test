from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase          
# Firstly you declare the ports your motors  and sensors are connected to 
# motor ports a to d while sensor ports s1 to s4

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

class machine:

    def __init__(self,wheel_diameter = 56, axle_track = 114):
        self.left_motor = Motor(Port.B) 
        self.right_motor = Motor(Port.A)
        self.obstacle_sensor = UltrasonicSensor(Port.S4)
        self.stop =Stop(stop_type.COAST)
        self.brake = Stop(stop_type.BRAKE)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter, axle_track)
        
    def drive():
        robot.drive(200, 0)
    def reverse(self):
        self.brake
        while self.obstacle_sensor().distance() < 300:
            
            brick.sound.file(SoundFile.backing_alert)
            
    def Motion(self):
        while True:
            if self.obstacle_sensor().distance() > 300:
                drive()
            else:
                reverse()
        
robot().Motion()       
            


