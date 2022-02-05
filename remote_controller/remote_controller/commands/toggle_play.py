from evdev import InputDevice

from remote_controller.commands.command import Command
from vlc_controller.series_player import SeriesPlayer


class TogglePlay(Command):
    IR_DATA_TO_COMMAND_DATA = {
        21: "TOGGLE_PLAY",
    }

    def execute(self, ir_data: int, device: InputDevice, player: SeriesPlayer):
        player.toggle_play()
