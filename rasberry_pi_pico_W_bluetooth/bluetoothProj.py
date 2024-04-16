# Import necessary modules
from machine import Pin 
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)
led_one = Pin(17, Pin.OUT)
led_two = Pin(16, Pin.OUT)

# Initialize the LED state to 0 (off)
led_state = 0

# Function to toggle the LED state
def toggle_led():
    global led_state
    led.value(not led_state)
    led_state = 1 - led_state

# Callback function to handle received data
def on_rx(data):
    print("Data received: ", data)
    if data == b'toggle\r\n':
        toggle_led()
    elif data == b'ledone\r\n':
        led_one.toggle()
    elif data == b'ledtwo\r\n':
        led_two.toggle()

# Function to check BLE connection and set callback
def check_ble_connection():
    if sp.is_connected():
        sp.on_write(on_rx)

# Main function
def main():
    while True:
        check_ble_connection()
