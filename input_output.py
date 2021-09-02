from machine import Pin
import utime

# Assign pin number and their functions to variable
button = Pin(2, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)


name = input('what is your name ?')
print('Name: ', name)

while True:    
    if button.value() == 0:
        print('button pressed')
        led.toggle()
        while button.value() == 0:
            pass
    utime.sleep_ms(20)            
