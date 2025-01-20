from gpiozero import LED, Button
from signal import pause

# Define pins
LedPin = 17  # GPIO17
BtnPin = 12  # GPIO12

# Initialize GPIO devices
led = LED(LedPin)
button = Button(BtnPin, pull_up=True)

# Callback function for button events
def my_callback():
    if button.is_pressed:
        led.off()
        print("LED OFF...")
    else:
        led.on()
        print("...LED ON")

# Setup button event
button.when_pressed = my_callback
button.when_released = my_callback

print("Press the button to toggle the LED state...")

# Keep the script running
try:
    pause()
except KeyboardInterrupt:
    print("\nExiting...")
