import IO.Context
import IO.Controller
from pygame.sprite import Sprite

class DebugSprite(Sprite, IO.Context.Context):

    def __init__(self, x, y):

        super(DebugSprite, self).__init__()
        super(DebugSprite, self).__init__()

        self.x = x
        self.y = y

    def on_up(self):
        self.rect.y += 1

    def on_down(self):
        self.rect.y -= 1
        
    def on_x(self):
        print("pressed x")
        
        
    IO.Context.on_x = self.on_x

if __name__ == "__main__":
    s = DebugSprite(0,0)
    s.do_command()