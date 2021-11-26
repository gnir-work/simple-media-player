import time
import pytest
from tests.consts import FIRST_EPISODE_NAME, SECOND_EPISODE_NAME
from tests.utils import check_if_file_was_open


@pytest.mark.parametrize(["episode_name", "episode_number"], [(FIRST_EPISODE_NAME, 1), (SECOND_EPISODE_NAME, 2)])
def test_play_by_number(series_player, episode_name, episode_number):
    series_player.play_episode(1)
    time.sleep(3)
    assert check_if_file_was_open(FIRST_EPISODE_NAME), "First episode wasn't played!"

