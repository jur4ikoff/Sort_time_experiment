#!/bin/bash

# Проверка наличия параметров
if [[ $# -lt 2 ]]; then
    echo "Input two parameters"
    exit 1
fi

# Определение имени входных файлов
size=$1
sort=$2

if [[ "$sort" == 0 ]]; then
    method="sort_1"
elif [[ "$sort" == 1 ]]; then
    method="sort_2"
else
    [[ "$sort" == 2 ]]
    method="sort_3"
fi

# Компиляция
gcc -std=c99 -Wall -O0 -Wvla -Werror -Wpedantic -Wextra -DSIZE="$size" -DSORT="$sort" -lm -lrt ./*.c -o apps/app_"$size"_"$method".exe
