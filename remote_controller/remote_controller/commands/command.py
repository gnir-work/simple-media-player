from abc import ABC, abstractclassmethod
from vlc_controller.series_player import SeriesPlayer
from evdev import InputDevice


class Command(ABC):
    IR_DATA_TO_COMMAND_DATA = {}

    @classmethod
    def can(cls, ir_data: int) -> bool:
        return ir_data in cls.IR_DATA_TO_COMMAND_DATA

    @abstractclassmethod
    def execute(cls, ir_data: int, device: InputDevice, player: SeriesPlayer):
        pass
