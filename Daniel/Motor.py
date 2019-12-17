"""Mr. Murray's test for using adafruit_motorkit with a stepper motor
Keep and eye on temperatures! Disconnect battery when not in use

Made with the help of this adafruit doc:
https://cdn-learn.adafruit.com/downloads/pdf/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi.pdf

For this you'll need to install the following package from thonny:
adafruit-circuitpython-motorkit


Connecting wires from the stepper:
Connect coloured stepper motor wires to blue input screw slots:
SLOT1 BLACK WIRE, SLOT2 GREEN WIRE,(skip the third pin:GND), SLOT4 BLUE WIRE, SLOT5 RED WIRE
"""

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from time import sleep
kit = MotorKit()


"""
You have access to the following options:

direction , which should be one of the following constant values:
stepper.FORWARD (default)
stepper.BACKWARD

style , which should be one of the values:

stepper.SINGLE (default) for a full step rotation to a position where one single coil is powered
stepper.DOUBLE for a full step rotation to position where two coils are powered providing more torque
stepper.MICROSTEP for a microstep rotation to a position where two coils are partially active

release() which releases all the coils so the motor can free spin, and also won't use any power
"""

#moves the motor forward a number of steps
"""for i in range(1000):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
sleep(1)"""


"""#moves the motor forward a number of baby steps with percision
for i in range(400):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
sleep(1)"""


#moves the motor forward a number of steps with lots of power (and heat!!)
"""for i in range(400):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
sleep(1)"""


#moves the motor backwards a number of steps with lots of power (and heat!!)
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
sleep(3)

#powers down the motor (stops it getting too hot)
kit.stepper1.release()
