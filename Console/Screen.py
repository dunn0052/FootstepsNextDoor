import pygame as pg

class Screen:
    def __init__(self, size = (1920, 1080)):

        flags = pg.OPENGL | pg.DOUBLEBUF
        try:
            self.screen = pg.display.set_mode(size, flags, vsync=1)
        except pg.error:
            self.screen = pg.display.set_mode()
            print(f"[ERROR] Could not initialize screen: {pg.get_error()}")

    def update(self):
        self.screen.fill((0,0,0))
        pg.display.flip()