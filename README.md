# Advent of Code 2020

Starting AoC on Dec 16th is 2020-esque. It's the time of the year to come together and work on some fun CTF language-agnostic problem. Please pull and commit your code!


## Link to problems:
https://adventofcode.com

## How to get data
First, create an account. Then, click on a day on the Advent calendar. Read the problem and find a prompt like "get your puzzle input". Click on it and a new page will open with the data for the problem. Copy that text by downloading it or CMD-A or CTRL-A and save it as a text file. 

# Day 1
Problem: find all pairs of numbers that sum to 2020, then find all triplets of numbers that sum to 2020.

Solution: nested for loops. This is a poor solution in Python, but in Julia for loops aren't a performance issue. I tried coming up with a general solution using _recursion_ but was not able. A recursive solution would solve for pairs, triplets, or any numbered set of numbers that sum to some number like 2020.


# Day 2
Problem: how many passwords in the input file are valid based on the rules given in each line?

Solution: loop through each line and parse each password and rules. Count how many passwords are valid.
