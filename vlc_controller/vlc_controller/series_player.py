from os import walk
from typing import List

from vlc_controller.media_player import MediaPlayer
from pathlib import Path
from logbook import Logger


class SeriesPlayer:
    def __init__(self, series_folder: Path):
        self.logger = Logger("SeriesPlayer")
        self.logger.info(f"Initialized series player with folder: {series_folder}")
        self.media_player = MediaPlayer()
        self.series_folder = series_folder

    @property
    def episodes(self) -> List[Path]:
        _, _, episode_names = next(walk(self.series_folder.as_posix()))
        return sorted(
            [self.series_folder / episode_name for episode_name in episode_names]
        )

    def play_episode(self, episode_number: int):
        self.logger.info(f"Playing episode {episode_number}")
        episode_path = self.episodes[episode_number - 1]
        self.media_player.play_video(episode_path)

    def stop(self):
        self.logger.info("Closing the current media")
        self.media_player.stop()

    def toggle_play(self):
        self.logger.info("Toggling the current media play status")
        self.media_player.toggle_play()

    def rewind_player(self, seconds: float):
        self.logger.info("Rewinding the media {seconds} seconds")
        self.media_player.rewind_player(seconds)
