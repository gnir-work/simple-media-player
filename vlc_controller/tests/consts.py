from pathlib import Path
from datetime import timedelta

EPISODES_FOLDER = "test_episodes"
CURRENT_PROCESS_FILE_DESCRIPTORS_FOLDER = Path("/proc/self/fd/")
FIRST_EPISODE_NAME = "episode_1.mp4"
SECOND_EPISODE_NAME = "episode_2.mp4"

VLC_SETUP_TIME = timedelta(seconds=1).seconds
