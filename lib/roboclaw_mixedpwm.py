import time
from roboclaw_3 import Roboclaw

#Windows comport name
# rc = Roboclaw("COM8", 128)
#Linux comport name
rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
address = 0x80

rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)

while(1):
	rc.ForwardMixed(address, 32)
	time.sleep(2)
	rc.BackwardMixed(address, 32)
	time.sleep(2)
	rc.TurnRightMixed(address, 32)
	time.sleep(2)
	rc.TurnLeftMixed(address, 32)
	time.sleep(2)
	rc.ForwardMixed(address, 0)
	rc.TurnRightMixed(address, 32)
	time.sleep(2)
	rc.TurnLeftMixed(address, 32)
	time.sleep(2)
	rc.TurnRightMixed(address, 0)
	time.sleep(2)
