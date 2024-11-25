#!/bin/bash

wal -i ~/Pictures/Wallpapers/ --saturate 0.9
#wpg -a ~/Pictures/Wallpapers
# -a 92
feh --bg-max "$(< "${HOME}/.cache/wal/wal")"
python3 /home/agus/.config/rofi/colors/create_color_theme.py
#bash ~/scripts/thor-colors.sh
