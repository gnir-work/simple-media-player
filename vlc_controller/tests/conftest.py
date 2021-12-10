from pathlib import Path

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
