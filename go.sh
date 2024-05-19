#!/bin/bash

if [[ $# != 2 ]]; then
    echo "Input only two paramentrs"
    exit 1
fi

SIZES=$1
SORTS=$2

echo "experiment with sizes: $SIZES sorts_typs: $SORTS"
./build_apps "{$SIZES}" "{$SORTS}"

