import time
from evdev import InputDevice, InputEvent
from typing import Union
from logbook import Logger

READ_INTERVAL = 0.01  # Seconds
LONG_PRESS_TIMEOUT = 0.15
READ_COMMAND_TIMEOUT = 0.85

logger = Logger("IR_utils")


def read_one_with_timeout(device: InputDevice, timeout: float = 0) -> Union[int, None]:
    """
    Reads the next event from the give device.
    In case a timeout was specified will return None after the timeout.

    :param device: [description]
    :type device: InputDevice
    :param timeout: [description], defaults to 0
    :type timeout: int, optional
    """
    timeout_time = time.time() + timeout
    while not timeout or timeout_time > time.time():
        event: InputEvent = device.read_one()
        if event and event.value:
            value: int = event.value
            return value
        else:
            time.sleep(READ_INTERVAL)
    return None


def get_single_remote_key(device: InputDevice, timeout: float = 0) -> Union[int, None]:
    """

    :param device: [description]
    :type device: InputDevice
    """
    value = read_one_with_timeout(device, timeout)
    if value:
        while read_one_with_timeout(device, LONG_PRESS_TIMEOUT):
            pass  # Clean long presses
        return value
    return None
