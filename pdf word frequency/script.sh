#!/bin/bash

# script takes the text and strips punctuation.
# counts the word frequency.
# only results after desired number.

# replace b.txt with filename 
# replace "/ 5" with the number from where to start.
# head -n lists number of results.

cat b.txt | tr -d '[:punct:]'  | tr ' ' '\n' | sort | uniq -ic | sort -nr | sed '1,/ 5 /d' | head -100
