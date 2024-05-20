#!/bin/bash

path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной
if [[ ! -d "${path_to_script}/data" ]]; then
    mkdir "${path_to_script}/data"
fi

for app in "$path_to_script"/apps/*.exe; do
    base=$(basename "$app")
    experiment=${base#app_}
    experiment=${experiment%.exe}
    echo -n -e "calculate file: $experiment \r"
    if [[ $experiment == internal* ]]; then
        "$app" >>"${path_to_script}/data/$experiment.txt"
    elif [[ $experiment == external* ]]; then
        # Формирование файла с временами для внутреннего эксперемента
        # Пробегаемся в цикле, пока RSE не будет меньше 1
        res=1
        while [ "$res" != 0 ]; do
            "$app" >>"${path_to_script}/data/$experiment.txt"
            res=$(python3 "${path_to_script}/scripts/calculate_rse.py" "${path_to_script}/data/$experiment.txt")
        done
    elif [[ $experiment == ticks* ]]; then
        "$app" >>"${path_to_script}/data/$experiment.txt"
    fi
done
