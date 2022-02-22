"""
All of the basic sdk functions needed for streaming the video.
"""
from typing import Union
import vlc
from vlc import Instance, Media, State
from datetime import timedelta
from pathlib import Path
import time


class MediaPlayer:
    FULL_SCREEN_INITIALIZATION_TIME = timedelta(seconds=5).seconds

    def __init__(self) -> None:
        self.instance: Instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.current_media: Union[Media, None] = None

    def stop(self):
        self.player.stop()

    def play_video(self, video_path: Path):
        self.stop()
        self.current_media = self.instance.media_new(video_path.as_posix())
        self.player.set_media(self.current_media)
        self.player.play()
        time.sleep(self.FULL_SCREEN_INITIALIZATION_TIME)
        self.player.set_fullscreen(True)

    def toggle_play(self):
        self.player.pause()

    def rewind_player(self, seconds: float):
        current_time = self.player.get_position()
        self.player.set_position(current_time + seconds)
