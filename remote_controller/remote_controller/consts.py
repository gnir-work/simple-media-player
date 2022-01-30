from enum import Enum


class KeyType(Enum):
    NUMBER = "number"
    ACTION = "action"


class Key:
    def __init__(self, value: str, key_type: KeyType):
        self.value = value
        self.type = key_type

    def __repr__(self):
        return f"{self.type} - {self.value}"


DEVICE_NAME = "gpio_ir_recv"
REMOTE_VALUE_TO_KEY = {
    22: Key("0", key_type=KeyType.NUMBER),
    12: Key("1", key_type=KeyType.NUMBER),
    24: Key("2", key_type=KeyType.NUMBER),
    94: Key("3", key_type=KeyType.NUMBER),
    8: Key("4", key_type=KeyType.NUMBER),
    28: Key("5", key_type=KeyType.NUMBER),
    90: Key("6", key_type=KeyType.NUMBER),
    66: Key("7", key_type=KeyType.NUMBER),
    82: Key("8", key_type=KeyType.NUMBER),
    74: Key("9", key_type=KeyType.NUMBER),
}
