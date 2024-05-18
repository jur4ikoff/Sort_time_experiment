#!/bin/bash
# Инициализация переменных
SIZES="500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000"
SORTS="0"
path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной
if [[ ! -d "${path_to_script}/apps" ]]; then
    mkdir "${path_to_script}/apps"
else
    rm -rf "${path_to_script}"/apps/*.exe
fi

# Запуск скрипта build_app.sh с перебором параметров
for size in $SIZES; do
    for sort in $SORTS; do
        echo -n -e "compile size: $size sort type: $sort \r"
        "${path_to_script}/scripts/build_app.sh" "$size" "$sort"
    done
done
