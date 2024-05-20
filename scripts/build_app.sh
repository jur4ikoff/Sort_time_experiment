#!/bin/bash

# Проверка наличия параметров
if [[ $# -lt 2 ]]; then
    echo "Input two parameters"
    exit 1
fi

# Определение имени входных файлов
size=$1
sort=$2

if [[ "$sort" == 1 ]]; then
    method="sort_1"
elif [[ "$sort" == 2 ]]; then
    method="sort_2"
elif [[ "$sort" == 3 ]]; then
    method="sort_3"
else
    echo "Wrong parametr"
    exit 1
fi
gcc -std=gnu99 -Wall -O0 -Wvla -Werror -Wpedantic -Wextra -c ./c_files/sorts.c -o ./c_files/sorts.o
gcc -std=gnu99 -Wall -O0 -Wvla -Werror -Wpedantic -Wextra -DSIZE="$size" -DSORT="$sort" ./c_files/sorts.o ./c_files/internal_sort.c -o apps/app_internal_"$size"_"$method".exe -lm
gcc -std=gnu99 -Wall -O0 -Wvla -Werror -Wpedantic -Wextra -DSIZE="$size" -DSORT="$sort" ./c_files/sorts.o ./c_files/external_sort.c -o apps/app_external_"$size"_"$method".exe -lm
gcc -std=gnu99 -Wall -O0 -Wvla -Werror -Wpedantic -Wextra -DSIZE="$size" -DSORT="$sort" ./c_files/sorts.o ./c_files/ticks_sort.c -o apps/ticks_"$size"_"$method".exe -lm
