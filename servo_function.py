from machine import PWM, Pin
import utime



# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(15))

# Set the PWM frequency to 1Khz.
pwm.freq(50)

min = 1000
max = 7500

def angle(angle): # angle value from 0 to 180
    global min, max
    if angle in range(0,181):
        inc_per_degree = (max-min)/180
        return(int(min+(angle*inc_per_degree)))
    else:
        print('Servo Error: Angle out of range!')
    
#print(angle(180))

while True:

    pwm.duty_u16(angle(0)) # Give angle value from 0 to 180
    utime.sleep(3)
    pwm.duty_u16(angle(90)) # max 6502
    utime.sleep(1)
    pwm.duty_u16(angle(180)) # min 3251
    utime.sleep(1)