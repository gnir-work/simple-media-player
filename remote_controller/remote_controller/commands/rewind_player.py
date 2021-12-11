from remote_controller.commands.command import Command
from remote_controller.ir_reciever import get_single_remote_key
from vlc_controller.series_player import SeriesPlayer
from evdev import InputDevice


class RewindPlayer(Command):
    IR_DATA_TO_COMMAND_DATA = {
        7: -0.02,
        9: 0.02
    }

    @classmethod
    def execute(cls, ir_data: int, device: InputDevice, player: SeriesPlayer):
        player.rewind_player(cls.IR_DATA_TO_COMMAND_DATA[ir_data])
