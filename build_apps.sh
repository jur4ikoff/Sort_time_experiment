#!/bin/bash

# Инициализация переменных
SIZES="1000"
SORTS="1"
path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной
if [ ! -d "apps" ]; then
    mkdir "apps"
else
    rm apps/*.exe
fi

# Запуск скрипта build_app.sh с перебором параметров
for size in $SIZES; do
    for sort in $SORTS; do
        "${path_to_script}/scripts/build_app.sh" "$size" "$sort"
    done
done
