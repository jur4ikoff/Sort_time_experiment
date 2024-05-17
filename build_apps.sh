#!/bin/bash
# Инициализация переменных
SIZES="1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 "
SORTS="0 1 2"
path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной
if [[ ! -d "${path_to_script}/apps" ]]; then
    mkdir "${path_to_script}/apps"
else
    rm -rf "${path_to_script}/apps/*.exe"
fi

# Запуск скрипта build_app.sh с перебором параметров
for size in $SIZES; do
    for sort in $SORTS; do
        "${path_to_script}/scripts/build_app.sh" "$size" "$sort"
    done
done



