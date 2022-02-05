"""
All of the basic sdk functions needed for streaming the video.
"""
from typing import Union
import vlc
from vlc import Instance, Media, State
from pathlib import Path


class MediaPlayer:
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
        self.player.set_fullscreen(True)
        self.player.play()

    def toggle_play(self):
        self.player.pause()

    def rewind_player(self, seconds: float):
        current_time = self.player.get_position()
        self.player.set_position(current_time + seconds)
