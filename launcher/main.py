###
# Cheap and fast Pyglet launcher. Will Pyglet work with controllers?
###

import os

import pyglet

def execute_selected_option():
    # TODO: process input, for reals
    op = selected_label.text
    execute = OPTIONS[op]
    execute()

def on_key_release(symbol, modifiers):
    # Use up-down arrows to browse and space/enter to launch
    # Use analog or d-pad to move, press a button to launch
    print(symbol)

def on_mouse_release(x, y, button, modifiers):
    # Execute the clicked-on option
    print(x, y, button)

# Buttons only, doesn't include D-pad
def on_joybutton_release(joystick, button):
    print("{0} => {1}".format(joystick, button))

def on_joyaxis_motion(joystick, axis, value):
    # Crude dead-zones. Tested on Logitech F310
    if abs(value) < 0.01:
        value = 0
    print("Joystick D-Pad: {0} => {1}".format(axis, value))

def shutdown():
    os.system("shutdown -P 0")

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

OPTIONS = {
    "Dajjal's Minions": lambda: print("DM!"),
    "Shutdown": lambda: shutdown(),
    "OS": lambda: pyglet.app.exit()
}

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=False)
window.push_handlers(on_mouse_release, on_key_release)

labels = []
i = 0

for option in OPTIONS:
    i += 1
    label = pyglet.text.Label(option)
    label.x = 150
    label.y = SCREEN_HEIGHT - 250 - (32 * i)
    labels.append(label)

selected_label = labels[0]

joysticks = []

@window.event
def on_draw():
    window.clear()
    for label in labels:
        label.draw()

def open_joysticks(elapsed):
    current_joysticks = pyglet.input.get_joysticks()
    if current_joysticks and len(current_joysticks) != len(joysticks):
        print("Joystick change")
        joysticks.clear()
        for j in current_joysticks:
            j.open()
            j.push_handlers(on_joybutton_release, on_joyaxis_motion)
            joysticks.append(j)

pyglet.clock.schedule_interval(open_joysticks, 1)
open_joysticks(0)
pyglet.app.run()