#!/bin/bash

while :
do
  # loop infinitely
  scp pc3.home:~/dev/projects/icc2022/scores.json .
  python3 scores_to_csv.py
  sleep 30
done
