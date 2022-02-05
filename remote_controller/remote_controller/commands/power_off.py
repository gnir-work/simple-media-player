from evdev import InputDevice

from remote_controller.commands.command import Command
from vlc_controller.series_player import SeriesPlayer


class PowerOff(Command):
    IR_DATA_TO_COMMAND_DATA = {
        69: "POWER_OFF",
    }

    def execute(self, ir_data: int, device: InputDevice, player: SeriesPlayer):
        player.stop()
