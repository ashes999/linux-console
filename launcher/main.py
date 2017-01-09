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

window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=True)
window.push_handlers(on_mouse_release, on_key_release) # TODO: joypad

label = pyglet.text.Label('Hello, world!')
label.y = SCREEN_HEIGHT / 2
label.x = SCREEN_WIDTH / 2

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()