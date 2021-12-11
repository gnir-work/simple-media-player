from remote_control.commands.command import Command
from remote_control.ir_reciever import get_single_remote_key
from vlc_controller.series_player import SeriesPlayer
from evdev import InputDevice


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

    @classmethod
    def execute(cls, ir_data: int, device: InputDevice, player: SeriesPlayer):
        episode_number = cls.IR_DATA_TO_COMMAND_DATA[ir_data]
        next_ir_data = get_single_remote_key(device, timeout=cls.EPISODE_CHANGE_TIMEOUT)
        while next_ir_data:
            if cls.can(next_ir_data):
                episode_number += cls.IR_DATA_TO_COMMAND_DATA[ir_data]
            next_ir_data = get_single_remote_key(
                device, timeout=cls.EPISODE_CHANGE_TIMEOUT
            )
        player.play_episode(int(episode_number))
