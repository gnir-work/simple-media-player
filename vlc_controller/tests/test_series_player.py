import time
import pytest
from tests.consts import VLC_SETUP_TIME, FIRST_EPISODE_NAME, SECOND_EPISODE_NAME
from tests.utils import check_if_file_is_open


@pytest.mark.parametrize(
    ["episode_name", "episode_number"],
    [(FIRST_EPISODE_NAME, 1), (SECOND_EPISODE_NAME, 2)],
)
def test_play_by_number(series_player, episode_name, episode_number):
    series_player.play_episode(episode_number)
    time.sleep(VLC_SETUP_TIME)
    assert check_if_file_is_open(episode_name), "First episode wasn't played!"


def test_play_folder(capfd, series_player):
    folder_index = 3
    series_player.play_episode(folder_index)
    time.sleep(VLC_SETUP_TIME)
    error_msg = capfd.readouterr().err
    assert "libdvdread: Can't open file VIDEO_TS.IFO." in error_msg
