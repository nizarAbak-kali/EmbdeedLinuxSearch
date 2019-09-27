#!/usr/bin/python

import csv
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    #input number you want to search
    words = input('Enter key words : \n')

    csv_file = csv.reader(open('ecs_blogs.csv', 'r'), delimiter=';', quoting=csv.QUOTE_MINIMAL)
    key_words = words.split(' ')
    matching_titles = {}
    for word in key_words : matching_titles[word] = []
    #loop through csv list
    for row in csv_file:
        words_in_title  = row[0].split(' ')
        words_in_title = [x.lower() for x in words_in_title]
        for word in key_words:
            if  word in words_in_title :
                matching_titles[word].append(row)

    pp.pprint (matching_titles)