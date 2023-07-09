import pygame as pg
from . import Screen


class Console:
    def __init__(self, size = (1920,1080), fps = 60, Title = "Game"):
        pg.init()

        self.clock = pg.time.Clock()
        self.screen = Screen.Screen(size)
        self.controllers = list()
        self.levels = list()

        self.FPS = fps
        self.dt = 0 # time differential
        self.running = False

    def start(self):
        self.running = True

        while self.running:
            # divide by 1024 ~1000 but faster
            self.dt = self.clock.tick(self.FPS) >> 10
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.update()