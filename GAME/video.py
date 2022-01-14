from moviepy.editor import *
import pygame as pg
from size import *

class start_video:
    def __init__(self, vfile):
        self.vfile = vfile

    def play_vid(self):
        pg.mouse.set_visible(False)
        self.clip = VideoFileClip(self.vfile).resize(screensize)
        self.clip.preview()
    def __del__(self):
        print()
