#!/bin/bash

[[ -z "$1" ]] && echo needs test case number && exit 1;
echo "case $1"

python3 torrent_tests.py > "input/input$1.txt"
python3 torrent_solve.py < "input/input$1.txt" | tee "output/output$1.txt"
