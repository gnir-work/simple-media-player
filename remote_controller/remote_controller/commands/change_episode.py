from evdev import InputDevice

from remote_controller.commands.command import Command
from remote_controller.ir_reciever import get_single_remote_key
from vlc_controller.series_player import SeriesPlayer
from logbook import Logger

logger = Logger("Change Episode Command")


class ChangeEpisode(Command):
    EPISODE_CHANGE_TIMEOUT = 1
    IR_DATA_TO_COMMAND_DATA = {
        22: "0",
        12: "1",
        24: "2",
        94: "3",
        8: "4",
        28: "5",
        90: "6",
        66: "7",
        82: "8",
        74: "9",
    }

    def execute(self, ir_data: int, device: InputDevice, player: SeriesPlayer):
        episode_number = self.IR_DATA_TO_COMMAND_DATA[ir_data]
        next_ir_data = get_single_remote_key(
            device, timeout=self.EPISODE_CHANGE_TIMEOUT
        )
        logger.info(f"Initial episode number: {episode_number}")
        while next_ir_data:
            logger.info(f"Got {next_ir_data} from IR")
            if self.can(next_ir_data):
                episode_number += self.IR_DATA_TO_COMMAND_DATA[next_ir_data]
                logger.info(f"Current episode number {episode_number}")
            next_ir_data = get_single_remote_key(
                device, timeout=self.EPISODE_CHANGE_TIMEOUT
            )
        player.play_episode(int(episode_number))
