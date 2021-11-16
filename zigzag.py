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

    for row in range(k):
        i = row
        # creates a list of spaces (strings)
        line = [" " for _ in range(sentenceLength)]

        # this while loop takes the list and populates it with the correct value from the sentence (on both sides of the zigzag)
        while i < sentenceLength:
            # check if zigzag is descending or not
            line[i] = sentence[i]
            desc = is_desc(i, k)
            newSpaces = get_spaces(row, desc, k)
            i += newSpaces + 1
        
        print("".join(line))

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

# function for checking if descending
def is_desc(index, k):
    # back to the starting point - will return true or false
    # compares calculated result to the sentence length - 1
    return index % (2 * (k - 1)) < k - 1

zigzag(sentence, k)