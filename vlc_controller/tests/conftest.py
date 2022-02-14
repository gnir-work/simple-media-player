import sys
from os import listdir
from pathlib import Path

from logbook import StreamHandler
from pytest import fixture, yield_fixture
from tests.consts import EPISODES_FOLDER
from vlc_controller.series_player import SeriesPlayer


@fixture(scope="session")
def episodes_folder():
    return Path(__file__).parent / EPISODES_FOLDER


@yield_fixture(scope="function")
def series_player(episodes_folder):
    player = SeriesPlayer(episodes_folder)
    yield player
    player.stop()


@fixture(scope="session", autouse=True)
def setup_logger():
    StreamHandler(sys.stdout).push_application()


@fixture(scope="session")
def folder_index(episodes_folder: Path):
    episodes = listdir(episodes_folder.as_posix())
    folder_name = "should_be_ignored"
    return episodes.index(folder_name) + 1
