#!/bin/bash

[[ -z "$1" ]] && echo needs test case number && exit 1;
echo "case '$1'"

# python3 *_tests.py > "input/input$1.txt"
python3 *_solve.py < "input/input$1.txt" | tee "output/output$1.txt"
