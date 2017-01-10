###
# Cheap and fast Pyglet launcher. Will Pyglet work with controllers?
###

import os

import pyglet

def process_input(key):
    # TODO: process input, for reals
    key = selected_label.text
    key = "Shutdown"
    execute = OPTIONS[key]
    execute()

def on_key_release(symbol, modifiers):
    # Use up-down arrows to browse and space/enter to launch
    # Use analog or d-pad to move, press a button to launch
    process_input(symbol)

def on_mouse_release(x, y, button, modifiers):
    # Execute the clicked-on option
    process_input(button)

def shutdown():
    os.system("shutdown -P 0")

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

OPTIONS = {
    "Dajjal's Minions": lambda: print("DM!"),
    "Shutdown": lambda: shutdown(),
    "OS": lambda: pyglet.app.exit()
}

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=True)
window.push_handlers(on_mouse_release, on_key_release) # TODO: joypad

labels = []
i = 0

for option in OPTIONS:
    i += 1
    label = pyglet.text.Label(option)
    label.x = 150
    label.y = SCREEN_HEIGHT - 250 - (32 * i)
    labels.append(label)

selected_label = labels[0]


@window.event
def on_draw():
    window.clear()
    for label in labels:
        label.draw()

pyglet.app.run()