# THE PROBLEM
# Given a string and a number of lines (k), print the string in zigzag form.
# In zigzag, characters are printed out diagonally from top left to bottom right until reaching the k line, then back up to top right, and so on.
# Example
# Sentence is "thisisazigzag" and k = 4 will print:
#
# t        a           g
#  h     s   z       a
#   i  i       i   z
#    s           g

# create string
sentence = "thisisazigzag"
# number of lines
k = 4

def zigzag(sentence, k):
    # get sentence length
    sentenceLength = len(sentence)
    # get range of lines
    rangeOfLines = range(k)
    # calculate the maximum space length
    spaceLength = (k - 1) * 2 - 1
    # take the string and convert to list
    listSentence = list(sentence)
    # final string
    zigzagString = ""

    print("Now creating a zigzag!")
    print(f"String entered - {sentence}")
    print(f"Number of lines entered = {k}")
    print(f"Based on the information provided, the maximum number of spaces will be - {spaceLength}")

    # print completed string
    print(zigzagString)

zigzag(sentence, k)