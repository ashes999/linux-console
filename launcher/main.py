###
# Cheap and fast Pyglet launcher. Will Pyglet work with controllers?
###

import os

import pyglet
from pyglet.window import key, mouse

class Launcher:
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 576

    OPTIONS = [
        ("Dajjal's Minions", lambda: print("DM!")),
        ("Shutdown", lambda: os.system("shutdown -P 0")),
        ("OS", lambda: pyglet.app.exit())
    ]

    # RGBA
    SELECTED_COLOUR = (255, 0, 0, 255) # red
    UNSELECTED_COLOUR = (255, 255, 255, 255) # white

    def __init__(self):
        self.window = pyglet.window.Window(Launcher.SCREEN_WIDTH, Launcher.SCREEN_HEIGHT, fullscreen=False)
        self.window.push_handlers(self.on_mouse_release, self.on_key_release)

        self.labels = []

        for i in range(len(Launcher.OPTIONS)):
            option = Launcher.OPTIONS[i]
            label = pyglet.text.Label(option[0])
            label.x = 150
            label.y = Launcher.SCREEN_HEIGHT - 250 - (32 * i)
            self.labels.append(label)

        self.selected_index = 0
        self.joysticks = []

        @self.window.event
        def on_draw():
            self.window.clear()
            for i in range(len(self.labels)):
                label = self.labels[i]
                if self.selected_index == i:
                    label.color = Launcher.SELECTED_COLOUR
                else:
                    label.color = Launcher.UNSELECTED_COLOUR
                label.draw()

    def execute_selected_option(self):
        # TODO: process input, for reals
        option = Launcher.OPTIONS[self.selected_index]
        execute = option[1]
        print("Executing {0}".format(option[0]))
        execute()

    def select_previous_option(self):
        self.selected_index -= 1
        if self.selected_index < 0:
            self.selected_index = len(Launcher.OPTIONS) - 1

    def select_next_option(self):
        self.selected_index += 1
        if self.selected_index >= len(Launcher.OPTIONS):
            self.selected_index = 0

    def on_key_release(self, symbol, modifiers):
        # Use up-down arrows to browse and space/enter to launch
        # Use analog or d-pad to move, press a button to launch
        if symbol == key.UP:
            self.select_previous_option()
        elif symbol == key.DOWN:
            self.select_next_option()

    def on_mouse_release(self, x, y, button, modifiers):
        # Execute the clicked-on option
        pass

    # Buttons only, doesn't include D-pad
    def on_joybutton_release(self, joystick, button):
        print("{0} => {1}".format(joystick, button))

    # Thumbstick and D-pad
    def on_joyaxis_motion(self, joystick, axis, value):
        # Crude dead-zones. Tested on Logitech F310
        if abs(value) < 0.01:
            value = 0
        if axis == "y" and abs(value) == 1:
            if value == -1:
                self.select_previous_option()
            elif value == 1:
                self.select_next_option()

    def open_joysticks(self, elapsed):
        current_joysticks = pyglet.input.get_joysticks()
        if current_joysticks and len(current_joysticks) != len(self.joysticks):
            print("Joystick change")
            self.joysticks.clear()
            for j in current_joysticks:
                j.open()
                j.push_handlers(self.on_joybutton_release, self.on_joyaxis_motion)
                self.joysticks.append(j)

    def run(self):
        pyglet.clock.schedule_interval(self.open_joysticks, 1)
        self.open_joysticks(0)
        pyglet.app.run()

Launcher().run()