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


def test_play_folder(folder_index, series_player):
    with pytest.raises(IndexError):
        series_player.play_episode(folder_index)
