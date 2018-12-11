# Minecraft controlling Lego Motor.

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from mcpi.minecraft import Minecraft
from mcpi import block

Speed = 0


from time import sleep

def move_forward(selected_value):
        Speed = float(selected_value)
        print(Speed)
        robot.forward(0.3)
        sleep(1)
        robot.forward(Speed)

def move_backward(selected_value):
        Speed = float(selected_value)
        print(Speed)
        robot.backward(0.3)
        sleep(1)
        robot.backward(Speed)
        
def you_chose_forward(selected_value):
    if selected_value == "0.15":
        move_forward(selected_value)
    elif selected_value == "0.16":
        move_forward(selected_value)

    elif selected_value == "0.17":
        move_forward(selected_value) 
    elif selected_value == "0.18":
        move_forward(selected_value)
        

    elif selected_value == "0.19":
        move_forward(selected_value)

def you_chose_backward(selected_value):
    if selected_value == "0.15":
        move_backward(selected_value)

    elif selected_value == "0.16":
        move_backward(selected_value)
    elif selected_value == "0.17":
        move_backward(selected_value)
    elif selected_value == "0.18":
        move_backward(selected_value)
    elif selected_value == "0.19":
        move_backward(selected_value)
    

robot = CamJamKitRobot()

def Stop():
    robot.stop()



mc = Minecraft.create()





while True:
  events=mc.events.pollBlockHits()
  for e in events:
    pos=e.pos
    Block=mc.getBlock(pos.x,pos.y,pos.z)
    if Block == 46:
      mc.postToChat("Blocks Controlling Blocks...FWD")
      move_forward(0.19)
    if Block == 20:
      mc.postToChat("Blocks Controlling Blocks...Stop")
      Stop()
    
        
     

    

