from evdev import InputDevice
from pathlib import Path
import time
from vlc_controller.series_player import SeriesPlayer
from remote_control.commands.change_episode import ChangeEpisode
from remote_control.ir_reciever import get_single_remote_key

COMMANDS = [ChangeEpisode]

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
