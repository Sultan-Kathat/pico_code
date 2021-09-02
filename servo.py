from machine import PWM, Pin
import utime

PWM_width = 0

# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(15))

# Set the PWM frequency to 1Khz.
pwm.freq(50)



while True:

    pwm.duty_u16(1000)
    utime.sleep(3)
    pwm.duty_u16(4200) # max 6502
    utime.sleep(1)
    pwm.duty_u16(7500) # min 3251
    utime.sleep(1)