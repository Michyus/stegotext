#!/usr/bin/env python
import os.path

# Line limit
limit = 30

# Message
message = 'something cool'

# Binary code of the message
binary = [1,1,0,1,0]

# List of words
words = []

# Output - cover file with message in it
output = []

# Define a cover file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'cover_files/lorem_ipsum.txt')

# Get words from a cover file
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as content:
        for line in content:
            for word in line.split():
                words.append(word+' ') #find smarter way to put spaces between words

# stego stuff - extended line
word_nummber = 0
for value in binary:
    print(value)
    line = ''
    if value == 0:
        while len(line)+len(words[word_nummber]) <= limit:
            line += words[word_nummber]
            word_nummber += 1
    elif value == 1:
        while len(line) <= limit:
            line += words[word_nummber]
            word_nummber += 1
    output.append(line)
    output.append(len(line))


print(output)
