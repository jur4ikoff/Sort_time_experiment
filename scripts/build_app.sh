#!/bin/bash


# Проверка наличия параметров
if [[ $# -lt 2 ]]; then
    echo "Need 2 params"
    exit 2
fi

# Определение имени входных файлов
size=$1
sort=$2


for file in *.c; do
    echo "$file"
    base=$(basename -s .c "$file")
    gcc -std=c99 -Wall -Wvla -Werror -c "$file" -o "apps/$base".o
done

gcc -o apps/app_"$size"_"$sort".exe apps/*.o -lm -DSIZE="$size" -DSORT="$sort"
./scripts/clean.sh 