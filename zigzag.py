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
    # calculate the maximum space length
    spaceLength = (k - 1) * 2 - 1
    # get range of lines
    rangeOfLines = range(k)
    # count spaces used
    spaceCount = 0
    # creates a list of spaces (strings)
    line = [" " for _ in range(sentenceLength)]
    # take the string and convert to list
    listSentence = list(sentence)
    # check if zigzag is descending or not
    desc = True

    print("Now creating a zigzag!")
    print(f"String entered - {sentence}")
    print(f"Number of lines entered = {k}")
    print(f"Based on the information provided, the maximum number of spaces will be - {spaceLength}")

    while spaceCount < spaceLength:
        for character in listSentence:
            print(line[spaceCount].join(f"{character}"))
            spaceCount += 1

# function for getting spaces
def get_spaces(row, desc, k):
    # calculate the maximum space length
    spaceLength = (k - 1) * 2 - 1

    # check if descending (add spaces)
    if desc:
        spaces = spaceLength - row + 2
    # or if ascending (remove spaces)
    else:
        spaces = spaceLength - (k - 1 - row) * 2
    
    return spaces

zigzag(sentence, k)