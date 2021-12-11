from remote_controller.commands.command import Command
from remote_controller.ir_reciever import get_single_remote_key
from vlc_controller.series_player import SeriesPlayer
from evdev import InputDevice


class PowerOff(Command):
    IR_DATA_TO_COMMAND_DATA = {
        69: "POWER_OFF",
    }

    @classmethod
    def execute(cls, ir_data: int, device: InputDevice, player: SeriesPlayer):
        player.stop()
