#!/bin/bash
wal -i ~/Pictures/Wallpapers

feh --bg-max "$(< "${HOME}/.cache/wal/wal")"

#bash ~/scripts/thor-colors.sh
