from machine import ADC, Pin
import time

adc = ADC(26)

while True:
    adc_value = adc.read_u16()
    time.sleep(1)
    volt = adc_value*(3.3/65535)
    print('volt: ',volt)
    mv = volt*1000
    print('mv: ', mv)
    temp = mv/10 # as per LM35 datasheet LM35 produces 10mv/degree
    round(temp,2)
    print('temperature by LM35: ', temp)
    print('----------------------')
