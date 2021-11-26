from pathlib import Path
from typing import List
from os import readlink, listdir

from tests.consts import CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER


def _get_current_open_files() -> List[Path]:
    open_files = []
    for file_descriptor_name in listdir(CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER):
        try:
            open_files.append(
                Path(readlink(Path(CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER) / file_descriptor_name))
            )
        except FileNotFoundError:
            pass # Some files open and close all the time
    return open_files


def check_if_file_was_open(file_name: str) -> bool:
    return any(map(lambda open_file: file_name in open_file.as_posix(), _get_current_open_files()))
