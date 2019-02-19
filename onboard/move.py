# Requires FTDI or XBee connection to hex

import serial
import time
from commands import *

ser = serial.Serial('/dev/ttyUSB0', 38400)

# Run given command for run_time number of seconds
def loop(command, run_time):
    start = time.time();
    while(time.time() - start < run_time):
        ser.write(command[0])
        ser.write(command[1])
        ser.write(command[2])
        ser.write(command[3])
        ser.write(command[4])
        ser.write(command[5])
        ser.write(command[6])
        ser.write(command[7])

# Initial stand
loop(still, 5)
loop(stand, 2)

loop(yaw_right, 2)
loop(yaw_left, 2)

# Finish
loop(still, 9)
