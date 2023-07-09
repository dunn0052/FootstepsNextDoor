
from IO.Button import ButtonInput

'''
Context class is used as a virtual class that connects conrollers to sprites.
Overload the on_*() functions and use do_command() with a button retrieved
from a Controller to perform the action.
'''
class Context:
    def __init__(self):
        self.commands = {
                ButtonInput.A:self.on_a,
                ButtonInput.B:self.on_b,
                ButtonInput.X:self.on_x,
                ButtonInput.Y:self.on_y,
                ButtonInput.DOWN:self.on_down,
                ButtonInput.UP:self.on_up,
                ButtonInput.LEFT:self.on_left,
                ButtonInput.RIGHT:self.on_right,
                ButtonInput.L:self.on_l,
                ButtonInput.R:self.on_r,
                ButtonInput.START:self.on_start,
                ButtonInput.SELECT:self.on_select
            }

        print("Context class")

    def do_command(self, button):
        self.commands[button]()

# Overload these to perform upon a button call.
# Otherwise does pass if not defined.

    def on_a(self):
        pass

    def on_b(self):
        pass

    def on_x(self):
        pass

    def on_y(self):
        pass

    def on_l(self):
        pass

    def on_r(self):
        pass

    def on_start(self):
        pass

    def on_select(self):
        pass

    def on_left(self):
        pass

    def on_right(self):
        pass

    def on_up(self):
        pass

    def on_down(self):
        pass