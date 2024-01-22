#!/bin/bash
wal -i ~/Pictures/Wallpapers

feh --bg-max "$(< "${HOME}/.cache/wal/wal")"
#the following line in .bashrc
#(cat ~/.cache/wal/sequences &)
