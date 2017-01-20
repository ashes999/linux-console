#!/bin/sh
# Setup for ODroid C2 with my specific Sony TV

# `Overscan.sh`
# ```
# #!/bin/sh
# ### BEGIN INIT INFO
# # Provides: overscan fix for my TV
# # Required-Start:       $local_fs $syslog $remote_fs
# # Required-Stop:        $local_fs $syslog $remote_fs
# # Default-Start:        2 3 4 5
# # Default-Stop:         0 1 6
# ### END INIT INFO
# echo 30 20 1889 1059 >  /sys/class/graphics/fb0/window_axis
# echo 0x10001 > /sys/class/graphics/fb0/free_scale
# ```

# sudo, copy to /etc/init.d, chmod a+x, sudo update-rc.d overscan.sh defaults

# - `sudo`
# - `sudo apt-get upgrade -y`
# - `sudo apt-get install python3-pip -y`
# - `sudo apt-get install git -y`
# - `mkdir ~/Desktop/Code`
# - `cd (above)`
# - `git clone ... lmc ...`
# - ` git clone ... dm ...`
# - `cd dm`
# - `make` (should chmod a+x build.sh, install pyinstaller and pyglet)
# - `copy to lmc/games`
