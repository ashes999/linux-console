###
# Cheap and fast Pyglet launcher. Will Pyglet work with controllers?
###

# TODO: run full-screen
# TODO: scale and black bands

import pyglet

def process_input(key):
    # TODO: process input, for reals
    key = selected_label.text
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
    # http://stackoverflow.com/questions/23013274/shutting-down-computer-linux-using-python#23013969
    import dbus
    sys_bus = dbus.SystemBus()
    ck_srv = sys_bus.get_object('org.freedesktop.ConsoleKit',
                                    '/org/freedesktop/ConsoleKit/Manager')
    ck_iface = dbus.Interface(ck_srv, 'org.freedesktop.ConsoleKit.Manager')
    stop_method = ck_iface.get_dbus_method("Stop")
    stop_method()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

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