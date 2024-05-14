#!/bin/bash

path_to_script=$(dirname "$(readlink -f "$0")")
path_to_apps="$path_to_script"/../apps

rm -f "$path_to_apps"/*.o
rm -f "$path_to_apps"/*.exe
rm -f "$path_to_apps"/*temp.txt*

exit 0