#!/usr/bin/env python
import os.path

# Output - cover file with message in it
output = []

# Get words from a cover file
def getWords(cover_file):
    words = []
    if not os.path.isfile(cover_file):
        print('File does not exist.')
    else:
        with open(cover_file) as content:
            for line in content:
                for word in line.split():
                    words.append(word+' ') #find smarter way to put spaces between words
    return words

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

    # todo once there are no values left in binary, generate a few random

    print(output)

# returns binary values of the message
def messageToBinary(message):
    dec_values = list(message.encode('ascii'))
    bin_values = [format(i,'08b') for i in dec_values]
    bin_string = ''.join(str(x) for x in bin_values) # TODO: this is not nice and overcomplicated
    bin_array = [int(value) for value in bin_string]
    return bin_array

# TODO decode method decode(file, limit)
# TODO input params
# TODO output to file/cli

if __name__ == "__main__":
    # Message
    message = 'Hi'

    # Define a cover file
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'cover_files/lorem_ipsum.txt')

    # List of words
    words = []

    # Line limit
    limit = 30

    binary = messageToBinary(message)
    print(binary)
    words = getWords(filename)
    stegoStuff(binary, words, limit)
