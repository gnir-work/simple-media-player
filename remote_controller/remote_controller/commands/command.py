from logging import Logger
from typing import Dict, Any

from evdev import InputDevice

from vlc_controller.series_player import SeriesPlayer


class Command:
    IR_DATA_TO_COMMAND_DATA: Dict[int, Any] = {}

    def __init__(self, logger=None):
        self.logger = logger or Logger("Command")

    def can(self, ir_data: int) -> bool:
        self.logger.info(f"Checking if {self.__class__.__name__} can execute on {ir_data}")
        return ir_data in self.IR_DATA_TO_COMMAND_DATA

    def execute(self, ir_data: int, device: InputDevice, player: SeriesPlayer):
        self.logger.info(f"Executing {self.__class__.__name__} on {ir_data}")
