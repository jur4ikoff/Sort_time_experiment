#!/bin/bash

path_to_script=$(dirname "$(readlink -f "$0")")

# Проверка на существование переменной
if [[ ! -d "${path_to_script}/data" ]]; then
    mkdir "${path_to_script}/data"
fi

echo "${path_to_script}/apps/"

for app in ${path_to_script}/apps/*.exe; do
    base=$(basename "$app")
    experiment=$(echo $base | sed 's/app_\(.*\).exe/\1/')
    echo $experiment
    ./"$app"
    exit
done