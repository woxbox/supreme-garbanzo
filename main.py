
#testing:
from robot import Robot
import time

r = Robot()
print(r)
print(r.cameras)
sBoard = r.servo_board
cam0 = r.cameras[0]
cam1 = r.cameras[1]
s0 = sBoard.servos[0]
s1 = sBoard.servos[1]
s0.position = -1
s1.position = -1

while True:

    c0markers = cam0.see()
    c1markers = cam1.see()

    if c0markers != [] and prevTwitch == False:
        s0.position = 0.5
        time.sleep(0.5)
        s0.position = -0.5
        prevTwitch = True

    elif c1markers != [] and prevTwitch == False:
        s1.position = 0.5
        time.sleep(0.5)
        s1.position = -0.5
        prevTwitch = True


    else:
        prevTwitch = False