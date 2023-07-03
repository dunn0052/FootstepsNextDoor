
# Controller buttons
class ButtonInput:
    X = "X"
    A = "A"
    B = "B"
    Y = "Y"
    L = "L"
    R = "R"
    SELECT = "SELECT"
    START = "START"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    UP = "UP"
    DOWN = "DOWN"

class State:
    PRESSED = 1
    RELEASED = 2
    HELD = 3
    OPEN = 4

class Button:

    def __init__(self, buttonType):
        self.buttonType = buttonType

        self.buttonState = State.OPEN

        self.currentState = State.RELEASED
        self.previousState = State.RELEASED

    def get_state(self):
        if self.currentState == State.PRESSED and self.previousState == State.PRESSED:
            self.buttonState = State.HELD
        elif self.currentState == State.PRESSED and self.previousState == State.RELEASED:
            self.buttonState = State.PRESSED
        elif self.currentState == State.RELEASED and self.previousState == State.RELEASED:
            self.buttonState = State.OPEN
        elif self.currentState == State.RELEASED and self.previousState == State.PRESSED:
            self.buttonState = State.RELEASED

        return self.buttonState

    def pressed(self):
        self.previousState = self.currentState
        self.currentState = State.PRESSED

    def released(self):
        self.previousState = self.currentState
        self.currentState = State.RELEASED

    def __str__(self) -> str:
        return self.buttonType

# testing code
if __name__ == "__main__":
    button = Button(ButtonInput.X)