from machine import UART, Pin, PWM

# Initialize UART
uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# Create a PWM object on Pin 0
pwm = PWM(Pin(0))

def set_pwm_signal(duty_cycle):
    pwm.freq(50)  # Set frequency to 50Hz
    pwm.duty_u16(duty_cycle)  # Set duty cycle

def transmit_signal(duty_cycle):
    uart1.write(str(duty_cycle))

def receive_and_calculate_difference(duty_cycle):
    measured_value = int(uart1.read())
    difference = duty_cycle - measured_value
    # Display the difference
    print("Difference:", difference)

# User sets the PWM duty cycle
duty_cycle = 32768  # 50% duty cycle for demonstration
set_pwm_signal(duty_cycle)
transmit_signal(duty_cycle)
receive_and_calculate_difference(duty_cycle)
