from Raspi_MotorHAT import Raspi_MotorHAT
import time

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(3)

myMotor.setSpeed(150)


while (True):
	print ("Forward! ")
	myMotor.run(Raspi_MotorHAT.FORWARD)
	time.sleep(1)

	print ("Backward! ")
	myMotor.run(Raspi_MotorHAT.BACKWARD)
	time.sleep(1)

	print ("Release")
	myMotor.run(Raspi_MotorHAT.RELEASE)
	time.sleep(1)
