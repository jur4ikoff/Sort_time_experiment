#!/bin/bash

path_to_script=$(dirname "$(readlink -f "$0")")
path="$path_to_script"/../apps

rm -f "$path"/*.o
rm -f "$path"/*temp.txt*

exit 0
