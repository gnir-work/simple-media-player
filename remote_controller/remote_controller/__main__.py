import sys
from pathlib import Path

from evdev import InputDevice
from logbook import Logger, StreamHandler

from remote_controller.commands.change_episode import ChangeEpisode
from remote_controller.commands.power_off import PowerOff
from remote_controller.commands.rewind_player import RewindPlayer
from remote_controller.commands.toggle_play import TogglePlay
from remote_controller.ir_reciever import get_single_remote_key
from remote_controller.utils import get_gpio_device
from vlc_controller.series_player import SeriesPlayer

logger = Logger('IR_MAIN')
COMMANDS = [ChangeEpisode, TogglePlay, RewindPlayer, PowerOff]


def loop(device: InputDevice, player: SeriesPlayer):
    while True:
        logger.info("Waiting for next IR command")
        ir_data = get_single_remote_key(device)
        logger.info(f"Got {ir_data} from IR remote")
        for command in COMMANDS:
            command = command()
            if command.can(ir_data):
                command.execute(ir_data, device, player)


def setup_loggers():
    StreamHandler(sys.stdout).push_application()


def main():
    setup_loggers()
    logger.info("Started main IR loop...")
    device = get_gpio_device()
    logger.info(f"Found IR device {device.name}")
    player = SeriesPlayer(
        Path("/home/pi/Code/simple-media-player/vlc_controller/tests/test_episodes")
    )
    loop(device, player)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception()
        raise
