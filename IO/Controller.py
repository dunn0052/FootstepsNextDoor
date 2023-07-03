from enum import Enum
from Button import Button, ButtonInput, State
import pygame.joystick


class ControllerType(Enum):
    JOYSTICK = 1
    KEYBOARD = 2

class JoystickDirection:
    UP = "JOY_UP"
    DOWN = "JOY_DOWN"
    LEFT = "JOY_LEFT"
    RIGHT = "JOY_RIGHT"

class DPADDirection:
    UP = "DPAD_UP"
    DOWN = "DPAD_DOWN"
    LEFT = "DPAD_LEFT"
    RIGHT = "DPAD_RIGHT"

POSITIVE_AXIS = 0.9
NEGATIVE_AXIS = -1.0
X_AXIS = 0
Y_AXIS = 1
NUM_BUTTONS = 8

class Controller:
    def __init__(self, index, type) -> None:
        self.index = index
        self.type = type

        if type == ControllerType.JOYSTICK:
            try:
                pygame.joystick.init()
                self.joystick = pygame.joystick.Joystick(index)
                self.joystick.init()
            except:
                print(f"No controller detected for index: {self.index}!")
                self.type = ControllerType.KEYBOARD

        if self.type == ControllerType.JOYSTICK:
            self.buttonMap = {0:Button(ButtonInput.A), 1:Button(ButtonInput.B), \
                              2:Button(ButtonInput.X), 3:Button(ButtonInput.Y), \
                              4:Button(ButtonInput.L), 5:Button(ButtonInput.R), \
                              6:Button(ButtonInput.SELECT), 7:Button(ButtonInput.START), \
                              JoystickDirection.UP:Button(ButtonInput.UP), \
                              JoystickDirection.DOWN:Button(ButtonInput.DOWN), \
                              JoystickDirection.LEFT:Button(ButtonInput.LEFT), \
                              JoystickDirection.RIGHT:Button(ButtonInput.RIGHT), \
                              DPADDirection.UP:Button(ButtonInput.UP), \
                              DPADDirection.DOWN:Button(ButtonInput.DOWN), \
                              DPADDirection.LEFT:Button(ButtonInput.LEFT), \
                              DPADDirection.RIGHT:Button(ButtonInput.RIGHT)}
            self.getInput = self.getJoystickInput

        elif self.type == ControllerType.KEYBOARD:
            self.buttonMap = {pygame.K_x:Button(ButtonInput.X), pygame.K_a:Button(ButtonInput.A), \
                    pygame.K_b:Button(ButtonInput.B), pygame.K_y:Button(ButtonInput.Y), \
                    pygame.K_q:Button(ButtonInput.L), pygame.K_e:Button(ButtonInput.R), \
                    pygame.K_h:Button(ButtonInput.START), pygame.K_g:Button(ButtonInput.SELECT), \
                    pygame.K_UP:Button(ButtonInput.UP), pygame.K_DOWN:Button(ButtonInput.DOWN), \
                    pygame.K_LEFT:Button(ButtonInput.LEFT), pygame.K_RIGHT:Button(ButtonInput.RIGHT)}

            self.getInput = self.getKeyboadInput

    def getInput(self):
        print("getInput() is not assigned!")
        pass

    def getJoystickInput(self):
        pygame.event.get()

        x_axis = self.joystick.get_axis(X_AXIS)
        y_axis = self.joystick.get_axis(Y_AXIS)
        if x_axis >= POSITIVE_AXIS:
            self.buttonMap[JoystickDirection.RIGHT].pressed()
        else:
            self.buttonMap[JoystickDirection.RIGHT].released()

        if x_axis == NEGATIVE_AXIS:
            self.buttonMap[JoystickDirection.LEFT].pressed()
        else:
            self.buttonMap[JoystickDirection.LEFT].released()

        if y_axis >= POSITIVE_AXIS:
            self.buttonMap[JoystickDirection.DOWN].pressed()
        else:
            self.buttonMap[JoystickDirection.DOWN].released()

        if y_axis == NEGATIVE_AXIS:
            self.buttonMap[JoystickDirection.UP].pressed()
        else:
            self.buttonMap[JoystickDirection.UP].released()

        d_pad = self.joystick.get_hat(0)
        if d_pad[0] == -1:
            self.buttonMap[DPADDirection.LEFT].pressed()
            self.buttonMap[DPADDirection.RIGHT].released()
        elif d_pad[0] == 1:
            self.buttonMap[DPADDirection.LEFT].released()
            self.buttonMap[DPADDirection.RIGHT].pressed()
        else:
            self.buttonMap[DPADDirection.LEFT].released()
            self.buttonMap[DPADDirection.RIGHT].released()

        if d_pad[1] == -1:
            self.buttonMap[DPADDirection.DOWN].pressed()
            self.buttonMap[DPADDirection.UP].released()
        elif d_pad[1] == 1:
            self.buttonMap[DPADDirection.DOWN].released()
            self.buttonMap[DPADDirection.UP].pressed()
        else:
            self.buttonMap[DPADDirection.DOWN].released()
            self.buttonMap[DPADDirection.UP].released()

        for buttonIndex in range(NUM_BUTTONS):
            status = self.joystick.get_button(buttonIndex)
            if status:
                self.buttonMap[buttonIndex].pressed()
            else:
                self.buttonMap[buttonIndex].released()

    def getKeyboadInput(self):
        pygame.event.get()
        pressedKeys = pygame.key.get_pressed()

        for key in self.buttonMap.keys():
            if key in pressedKeys:
                self.buttonMap[key].pressed()
            else:
                self.buttonMap[key].released()

    def __str__(self):
        if self.type == ControllerType.JOYSTICK:
            return f"Controller {self.joystick.get_id()}: {self.joystick.get_name()} \r\n\
Number of buttons: {self.joystick.get_numbuttons()} Number of axis: {self.joystick.get_numaxes()}"
        elif self.type == ControllerType.KEYBOARD:
            return f"Keyboard"

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    cont = Controller(0, ControllerType.JOYSTICK)
    print(cont)

    while True:
        cont.getInput()

        for button in cont.buttonMap.values():
            if button.get_state() == State.PRESSED:
                print(f"Button pressed: {button.__str__()}")

        clock.tick(60)