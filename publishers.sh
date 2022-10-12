#!/bin/bash


# This script will show the best selling titles of the publishers as well as their overall amount of titles published

path="Video_Games_Sales_2016.csv" # Path to the dataset

echo $path
echo "Titles under your favorite publisher in the dataset"
read -p "Enter the name of your favorite publisher: " publisher


head -n 1 $path | cut -d ',' -f 1-5,10 > your_publisher.csv
cat $path | cut -d ',' -f 1-5,10 | grep -n "$publisher" | sort -t , -nr -k 6 >> your_publisher.csv

echo "Count of titles under $publisher"
cat your_publisher.csv | wc -l
echo "Now printing the best selling 25 titles under $publisher"
head -n 26 your_publisher.csv