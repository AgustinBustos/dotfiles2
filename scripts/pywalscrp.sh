#!/bin/bash

#wal -a 100 -i ~/Pictures/Wallpapers --saturate 0.99 
#wal -a "alpha" --saturate 0.99  -i ~/Pictures/Wallpapers 
wal -a 0.99 --saturate 0.99  -i ~/Pictures/Wallpapers 

# -a 92
# -a 100 
wpg -a ~/Pictures/Wallpapers/
feh --bg-max "$(< "${HOME}/.cache/wal/wal")"
python3 /home/agus/.config/rofi/colors/create_color_theme.py
#bash ~/scripts/thor-colors.sh
