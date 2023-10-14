from machine import UART, Pin, ADC

# Initialize UART
uart2 = UART(1, baudrate=9600, tx=Pin(9), rx=Pin(8))

# Initialize ADC on pin 26
adc = ADC(Pin(26))

def read_analog_value():
    # Convert ADC reading to duty cycle
    return adc.read_u16()

def listen_and_measure():
    desired_value = int(uart2.read())
    measured_value = read_analog_value()
    uart2.write(str(measured_value))

# Continuously listen for data from Pico 1
while True:
    listen_and_measure()
