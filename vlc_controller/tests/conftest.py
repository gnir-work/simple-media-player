import sys
from pathlib import Path

from logbook import StreamHandler
from pytest import fixture, yield_fixture

from tests.consts import EPISODES_FOLDER
from vlc_controller.series_player import SeriesPlayer


@fixture
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
