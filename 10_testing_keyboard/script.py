import keyboard

def on_press(event):
    print(f"Key {event.name} - Scan Code: {event.scan_code}")

keyboard.on_press(on_press)
keyboard.wait()  # Keeps the script running
