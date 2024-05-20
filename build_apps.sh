#!/bin/bash
# Инициализация переменных
if [[ $# != 2 ]]; then
    echo "Input only two paramentrs"
    exit 1
fi

SIZES=$1
SORTS=$2

path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной и удаление старых файлов
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
