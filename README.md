# Linux Micro Console
A prototype of a low-cost Linux-based gaming micro-console.

# Hardware

You can use any hardware you like. I only test on ODroid C2.

Probable minimum requirements:

- Dual-core 1GHz+ CPU
- 2GB of RAM
- HDMI port

You can buy something like this for under $50 on Ali Express. You can also try Raspberry Pi or ODroid C1/C2.

For development, you may want a VGA port and a headphone jack on your device.  You can also probably get away with 1GB of RAM, but I can't make any guarantees about how well things will run. Things also generally work on Windows, if that's your development-environment of choice.

You can use your OS of choice. For controllers, as long as you install drivers, things should work. If they don't, or if you want to add your controller's drivers/config to the default, open a pull-request. 

Officially, we only support **Ubuntu Mate** with a **Logitech F310 gamepad** (since that's what I use).

# Roug Notes

`Overscan.sh`
```
#!/bin/sh
### BEGIN INIT INFO
# Provides: overscan fix for my TV
# Required-Start:       $local_fs $syslog $remote_fs
# Required-Stop:        $local_fs $syslog $remote_fs
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
### END INIT INFO
echo 30 20 1889 1059 >  /sys/class/graphics/fb0/window_axis
echo 0x10001 > /sys/class/graphics/fb0/free_scale
```

TODO: add these to ODroid C2 setup file
- `sudo apt-get upgrade`
- `sudo apt-get install python3-pip`
- `sudo apt-get install git`
- `mkdir ~/Desktop/Code`
- `cd (above)`
- `git clone ... lmc ...`
- ` git clone ... dm ...`
- `cd dm`
- `make` (should chmod a+x build.sh, install pyinstaller and pyglet)
- `copy to lmc/games`
