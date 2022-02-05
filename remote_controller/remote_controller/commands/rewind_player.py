from evdev import InputDevice

from remote_controller.commands.command import Command
from vlc_controller.series_player import SeriesPlayer


class RewindPlayer(Command):
    IR_DATA_TO_COMMAND_DATA = {7: -0.02, 9: 0.02}

    def execute(self, ir_data: int, device: InputDevice, player: SeriesPlayer):
        player.rewind_player(self.IR_DATA_TO_COMMAND_DATA[ir_data])
