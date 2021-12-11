from evdev import InputDevice
from pathlib import Path
import time
from vlc_controller.series_player import SeriesPlayer
from remote_controller.commands.change_episode import ChangeEpisode
from remote_controller.commands.toggle_play import TogglePlay
from remote_controller.commands.rewind_player import RewindPlayer
from remote_controller.ir_reciever import get_single_remote_key

COMMANDS = [ChangeEpisode, TogglePlay, RewindPlayer]


def main_loop(device: InputDevice, player: SeriesPlayer):
    while True:
        ir_data = get_single_remote_key(device)
        for command in COMMANDS:
            if command.can(ir_data):
                command.execute(ir_data, device, player)


if __name__ == "__main__":
    dev = InputDevice("/dev/input/event7")
    player = SeriesPlayer(
        Path("/home/pi/Code/simple-media-player/vlc_controller/tests/test_episodes")
    )
    main_loop(dev, player)
