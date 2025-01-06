#!/bin/bash

#configuracion de inicio para qtile



udiskie -t &
volumeicon &
cbatticon -u 5 &
nm-applet &
onboard &
#
#para que funcionen debe estar el widget de systray
# picom
picom &
# nitrogen
nitrogen --restore &

#mapeo de tecla tab que no me sirve
xmodmap -e "keycode 49=Tab"

#redshift default color
redshift -P -O 6000
