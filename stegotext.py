#!/usr/bin/env python
import os.path

# Message
message = 'something cool'

# Output - cover file with message in it
output = []

# Get words from a cover file
def getWords(cover_file, words):
    if not os.path.isfile(cover_file):
        print('File does not exist.')
    else:
        with open(cover_file) as content:
            for line in content:
                for word in line.split():
                    words.append(word+' ') #find smarter way to put spaces between words

# stego stuff - extended line
def stegoStuff(binary, words, limit):
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

# message to binary
def messageToBinary():
    list("Hello".encode('ascii'))

if __name__ == "__main__":
    # Define a cover file
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'cover_files/lorem_ipsum.txt')

    # List of words
    words = []

    # Binary code of the message
    binary = [1,1,0,1,0]

    # Line limit
    limit = 30

    getWords(filename, words)
    stegoStuff(binary, words, limit)
