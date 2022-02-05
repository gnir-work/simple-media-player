import sys
import click
from pathlib import Path

from evdev import InputDevice
from logbook import Logger, StreamHandler, FileHandler

from remote_controller.commands.change_episode import ChangeEpisode
from remote_controller.commands.power_off import PowerOff
from remote_controller.commands.rewind_player import RewindPlayer
from remote_controller.commands.toggle_play import TogglePlay
from remote_controller.ir_reciever import get_single_remote_key
from remote_controller.utils import get_gpio_device
from vlc_controller.series_player import SeriesPlayer

logger = Logger("IR_MAIN")
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


def setup_loggers(log_file: str):
    StreamHandler(sys.stdout).push_application()
    if log_file:
        FileHandler(log_file).push_application()


@click.command()
@click.option(
    "-d",
    "--media-directory",
    required=True,
    help="The absolute path to the folder with the media to be played",
)
@click.option("-l", "--log-file", default=None, help="The file to output the logs to")
def main(media_directory: str, log_file: str):
    setup_loggers(log_file)
    logger.info("Started main IR loop...")
    device = get_gpio_device()
    logger.info(f"Found IR device {device.name}")
    player = SeriesPlayer(Path(media_directory))
    loop(device, player)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception()
        raise
