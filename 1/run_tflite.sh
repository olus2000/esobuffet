#/bin/bash
if [ "$#" -ne 2 ]; then
    echo "usage: $0 source input" >&2
    exit 1
fi
if ! [ -e "$1" ]; then
    echo "$1: not found" >&2
    exit 1
fi
if ! [ -e "$2" ]; then
    echo "$2: not found" >&2
    exit 1
fi
cat $2 | python3 -c "$(cat $1 | python3 ./tflite.py)"