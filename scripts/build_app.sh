#!/bin/bash

# Проверка наличия параметров
if [[ $# -lt 2 ]]; then
    echo "Input two parameters"
    exit 1
fi

# Определение имени входных файлов
size=$1
sort=$2

# Компиляция
gcc -std=c99 -Wall -Wvla -Werror -Wpedantic -Wextra -Wfloat-conversion -Wfloat-equal ./*.c -o apps/app_"$size"_"$sort".exe -DSIZE="$size" -DSORT="$sort"
