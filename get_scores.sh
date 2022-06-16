#!/bin/bash

while :
do
  # loop infinitely
  timeout 5 python3 score_scrape.py | tee -a scores.json
  python3 scores_to_csv.py
  sleep 30
done
