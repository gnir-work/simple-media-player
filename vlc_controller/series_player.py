from os import listdir
from typing import List

from .media_player import MediaPlayer
from pathlib import Path


class SeriesPlayer:
    def __init__(self, series_folder: Path):
        self.media_player = MediaPlayer()
        self.series_folder = series_folder

    @property
    def episodes(self) -> List[Path]:
        episode_names = listdir(self.series_folder.as_posix())
        return [self.series_folder / episode_name for episode_name in episode_names]
    
    def play_episode(self, episode_number: int):
        episode_path = self.episodes[episode_number - 1]
        self.media_player.play_video(episode_path)

    def stop(self):
        self.media_player.stop()

    def pause(self):
        self.media_player.pause()

    def resume(self):
        self.media_player.resume()