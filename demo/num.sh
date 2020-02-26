#!/usr/bin/bash

cat num.txt | head -n 100 > num1.txt
cat num.txt | head -n 200 | tail -n 100 > num2.txt 
