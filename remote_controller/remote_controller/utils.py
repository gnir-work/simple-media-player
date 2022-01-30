from remote_controller.consts import DEVICE_NAME
from evdev import list_devices, InputDevice

def get_gpio_device(device_name: str = DEVICE_NAME):
    for device in map(InputDevice, list_devices()):
        if device.name == device_name:
            return device
    raise Exception(f"No device with name {device_name} found!")
