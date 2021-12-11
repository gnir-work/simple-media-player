from evdev import InputDevice
from pathlib import Path
from enum import Enum
import time
from series_player import SeriesPlayer

READ_INTERVAL = 0.01  # Seconds
LONG_PRESS_TIMEOUT = 0.15
READ_COMMAND_TIMEOUT = 0.85


class KeyType(Enum):
    NUMBER = "number"
    ACTION = "action"


class Key:
    def __init__(self, value: str, key_type: KeyType):
        self.value = value
        self.type = key_type

    def __repr__(self):
        return f"{self.type} - {self.value}"


remote_value_to_key = {
    22: Key("0", key_type=KeyType.NUMBER),
    12: Key("1", key_type=KeyType.NUMBER),
    24: Key("2", key_type=KeyType.NUMBER),
    94: Key("3", key_type=KeyType.NUMBER),
    8: Key("4", key_type=KeyType.NUMBER),
    28: Key("5", key_type=KeyType.NUMBER),
    90: Key("6", key_type=KeyType.NUMBER),
    66: Key("7", key_type=KeyType.NUMBER),
    82: Key("8", key_type=KeyType.NUMBER),
    74: Key("9", key_type=KeyType.NUMBER),
}


def read_one_with_timeout(device: InputDevice, timeout: float = 0):
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
        event = device.read_one()
        if event and event.value and event.value in remote_value_to_key:
            return remote_value_to_key[event.value]
        else:
            time.sleep(READ_INTERVAL)


def get_single_remove_command(device: InputDevice, timeout: float = 0):
    """

    :param device: [description]
    :type device: InputDevice
    """
    # import ipdb;ipdb.set_trace()
    value = read_one_with_timeout(device, timeout)
    if value:
        while read_one_with_timeout(device, LONG_PRESS_TIMEOUT):
            pass  # Clean long presses
        return value


def handle_next_command(device: InputDevice, timeout: float = READ_COMMAND_TIMEOUT):
    command = get_single_remove_command(device)
    

def get_remote_command(device: InputDevice, timeout: float = READ_COMMAND_TIMEOUT):
    command = [get_single_remove_command(device)]
    next_command = get_single_remove_command(device, timeout)
    while next_command:
        command.append(next_command)
        next_command = get_single_remove_command(device, timeout)
    return command


def main_loop(device: InputDevice, player: SeriesPlayer):
    while True:
        command = get_remote_command(device)
        episode_number = int(command[0].value)
        player.play_episode(episode_number)


if __name__ == "__main__":
    dev = InputDevice("/dev/input/event7")
    player = SeriesPlayer(Path("/home/pi/Code/simple-media-player/vlc_controller/tests/test_episodes"))
    main_loop(dev, player)
