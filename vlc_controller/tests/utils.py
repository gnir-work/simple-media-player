from pathlib import Path
from typing import List
from os import readlink, listdir

from tests.consts import CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER


def _get_current_open_files() -> List[Path]:
    """
    Read the current processes open file descriptors and return them as a list of Path objects.
    This function is useful in order to test the player and make sure that it is opening the correct files.
    """
    open_files = []
    for file_descriptor_name in listdir(CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER):
        try:
            open_files.append(
                Path(
                    readlink(
                        Path(CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER)
                        / file_descriptor_name
                    )
                )
            )
        except FileNotFoundError:
            pass  # Some files open and close all the time
    return open_files


def check_if_file_is_open(file_name: str) -> bool:
    """
    Check if the given file_name is open in the current process.
    :param file_name: The filename to test.
    """
    return any(
        map(lambda open_file: file_name == open_file.name, _get_current_open_files())
    )
