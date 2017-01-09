###
# Cheap and fast Pyglet launcher. Will Pyglet work with controllers?
###

# TODO: run full-screen
# TODO: scale and black bands

import pyglet

def process_input(key):
    print(key)

def on_key_release(symbol, modifiers):
    print(symbol)

def on_mouse_release(x, y, button, modifiers):
    process_input(button)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
OPTIONS = ["Dajjal's Minions", "Shutdown", "OS"]

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

@window.event
def on_draw():
    window.clear()
    for label in labels:
        label.draw()

pyglet.app.run()