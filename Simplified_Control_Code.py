# Import necessary modules and classes for GPIO pins, PWM, UART, and timing functions
from machine import Pin, PWM, UART
from time import sleep


# Initialize UART communication at a baud rate of 9600
uart = UART(0, 9600)

# # Define motor pins for the right, left, and lift motors
right_motor = [Pin(11, Pin.OUT), Pin(12, Pin.OUT)]
left_motor = [Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
lift_motor = [Pin(16, Pin.OUT), Pin(17, Pin.OUT)]

# Motor PWMs
motor_ena = PWM(Pin(10))
motor_enb = PWM(Pin(13))
motor_enc = PWM(Pin(10))

# Set motor PWM frequencies to 1500 Hz
motor_ena.freq(1500)
motor_enb.freq(1500)
motor_enc.freq(1500)

# Function to control motor speed and direction
def motor_control(pins, speed, direction):
    motor_ena.duty_u16(speed * 680)
    motor_enb.duty_u16(speed * 680)
    
    # Loop through motor pins and set direction
    for pin in pins:
        if direction:
            pin.high()  # spin forward
        else:
            pin.low()   # spin backward

# Function to control movement with motor actions and delays
def move(duration, *args):
    motor_control(*args) # Start motors
    sleep(duration) 
    motor_control([m for m in args[0]], 0, True)  # Stop the motors

while True:
    # Movement sequences for various directions and actions
    move(1, right_motor, 0, True) # Move right for 1 second
    move(3, right_motor, 1, False) # Move left for 3 seconds


    move(1, lift_motor, 0, True) # Move left for 1 second
    move(3, lift_motor, 1, False) # Move right for 3 seconds

    move(3, [right_motor[0], lift_motor[1]], 0, True)
    move(1, [right_motor[0], lift_motor[1]], 0, True)
    move(1, right_motor + lift_motor, 0, True)

    move(3, [right_motor[1], lift_motor[0]], 0, True)
    move(1, [right_motor[1], lift_motor[0]], 0, True)
    move(1, right_motor + lift_motor, 0, True)
    
    move(0.74, lift_motor, 0, True) # Move lift down for 0.74 seconds
    move(1, lift_motor, 0, True) # Move lift up for 1 second

    move(0.74, lift_motor, 1, False)
    move(1, lift_motor, 1, False)
