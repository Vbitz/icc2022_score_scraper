#!/bin/bash

while :
do
  # loop infinitely
  scp pc3.home:~/dev/projects/icc2022/scores_ad.json .
  python3 scores_to_csv_ad.py
  sleep 120
done
