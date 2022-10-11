#!/bin/bash

# Show counts of the big 3 publishers
# This script will show the counts of the big 3 publishers in the dataset

path="/workspaces/Trending-Youtube-Videos-Data-Engineering-Project-Eric-Rios/Video_Games_Sales_2016.csv" # Path to the dataset

echo $path
echo "The counts of the publih in the dataset by global sales"

head -n 1 $path | cut -d ',' -f 1-5,10 > top10.csv

cat $path | cut -d ',' -f 1-5,10 | sort -t , -nr -k 6 | head -n 10 >> top10.csv

head -n 11 top10.csv