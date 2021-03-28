import evdev
from gpiozero import LED

white=LED(17)

device = evdev.InputDevice('/dev/input/event4')
print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        print(event.code)
        if event.code==115:
            white.on()
        else:
            white.off()
