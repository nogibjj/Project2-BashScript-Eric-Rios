#!/bin/bash

# This script will leave only the title of the game, the publisher, and the global sums for the top 10 entries.

path="/workspaces/Trending-Youtube-Videos-Data-Engineering-Project-Eric-Rios/Video_Games_Sales_2016.csv" # Path to the dataset

# This function will print the top 10 entries in the dataset
echo $path
echo "Top 10 entries in the dataset by global sales"

head -n 1 $path | cut -d ',' -f 1-5,10 > top10.csv

cat $path | cut -d ',' -f 1-5,10 | sort -t , -nr -k 6 | head -n 10 >> top10.csv

head -n 11 top10.csv


