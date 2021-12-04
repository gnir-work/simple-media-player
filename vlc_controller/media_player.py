"""
All of the basic sdk functions needed for streaming the video.
"""
from ctypes import Union
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
        self.player.play()

    def pause(self):
        if self.player.get_state() == State.Playing:
            self.player.pause()

    def resume(self):
        if self.player.get_state() == State.Paused:
            self.player.pause()
