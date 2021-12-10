from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event7')

for event in dev.read_loop():
    print(event)
