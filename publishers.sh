#!/bin/bash

# Show counts of the big 3 publishers
# This script will show the counts of the big 3 publishers in the dataset

path="/workspaces/Trending-Youtube-Videos-Data-Engineering-Project-Eric-Rios/Video_Games_Sales_2016.csv" # Path to the dataset

echo $path
echo "Titles under your favorite publisher in the dataset"
read -p "Enter the name of your favorite publisher: " publisher


head -n 1 $path | cut -d ',' -f 1-5,10 > your_publisher.csv
cat $path | cut -d ',' -f 1-5,10 | grep -n "$publisher" | sort >> your_publisher.csv

echo "Count of titles under $publisher"
cat your_publisher.csv | wc -l
echo "Now printing the first 25 titles under $publisher"
head -n 26 your_publisher.csv