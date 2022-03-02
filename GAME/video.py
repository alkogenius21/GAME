from moviepy.editor import *
import pygame as pg
from size import *
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx


class start_video:
    def __init__(self, vfile):
        self.vfile = vfile

    def play_vid(self):
        pg.mouse.set_visible(False)
        self.clip = VideoFileClip(self.vfile).resize(screensize)
        self.clip.preview()

    def stop(self):
        self.clip.close()

    def __del__(self):
        print()
