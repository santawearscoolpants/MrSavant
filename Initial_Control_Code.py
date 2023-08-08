from machine import Pin, PWM, UART
from time import sleep

uart = UART(0,9600)

m1a = Pin(11, Pin.OUT) #right motor
m1b = Pin(12, Pin.OUT) #right motor
m2a = Pin(14, Pin.OUT) #left motor
m2b = Pin(15, Pin.OUT) #left motor

m3a = Pin(16, Pin.OUT) #lift motor
m3b = Pin(17, Pin.OUT) #lift motor

ena = PWM(Pin(10)) #enables speed control of motor
enb = PWM(Pin(13))
enc = PWM(Pin(10))

ena.freq(1500) 
enb.freq(1500)
enc.freq(1500)



def move_left(speed,duration=0):
    ena.duty_u16(speed * 680)
    enb.duty_u16(speed * 680)
    
    print("Moving left")
    m1a.high() #spin forward
    m1b.low()
    m2a.low() #spin forward
    m2b.high()
    
    print("Moved left")
    sleep(duration)
    
def move_forward(speed,duration=0):
    ena.duty_u16(speed * 680)
    enb.duty_u16(speed * 680)
    
    print("Moving forward!")
    m1a.low() #spin forward
    m1b.high()
    m2a.low() #spin forward
    m2b.high()
    
    print("Moved forward")
    sleep(duration)
    
def move_backward(speed,duration=0):
    ena.duty_u16(speed * 680)
    enb.duty_u16(speed * 680)
    
    print("Moving Backward!")
    m1a.high() #spin forward
    m1b.low()
    m2a.high() #spin forward
    m2b.low()
    
    print("Moved Backward")
    sleep(duration)
    
def move_right(speed,duration=0):
    ena.duty_u16(speed * 680)
    enb.duty_u16(speed * 680)
    
    print("Moving right!")
    m1a.low() #spin backward
    m1b.high()
    m2a.high() #spin backward
    m2b.low()
    
    print("Moved Right")
    sleep(duration)
    
def stop(duration=0):
    ena.duty_u16(0)
    enb.duty_u16(0)
    
    print("Stoping")
    m1a.low() #spin backward
    m1b.low()
    m2a.low() #spin backward
    m2b.low()
    
    print("Stopped")
    sleep(duration)
    
def move_down(speed,duration=0):
    enc.duty_u16(speed * 680)
    
    print("Lift down!")
    m3a.high() #spin forward
    m3b.low()
    
    print("Down")
    sleep(duration)
    
def move_up(speed,duration=0):
    enc.duty_u16(speed * 680)
    
    print("Lift Up!")
    m3a.low() #spin forward
    m3b.high()
    
    print("Up!")
    sleep(duration)
    
def stop_lift(duration=0):
    enc.duty_u16(0)
    
    print("Lift stop!")
    m3a.low() #spin forward
    m3b.low()
    
    print("Stopped!")
    sleep(duration)
    

while True:
    move_forward(90)
    sleep(1)
    stop()
    sleep(3)

    move_backward(90)
    sleep(1)
    stop()
    sleep(3)


"""

while True:
    move_left(90)
    sleep(3)
    stop()
    sleep(1)

    move_right(90)
    sleep(3)
    stop()
    sleep(1)
    
    move_down(90)
    sleep(0.74)
    stop_lift()
    sleep(1)

    move_up(90)
    sleep(0.74)
    stop_lift()
    sleep(1)

"""


        


