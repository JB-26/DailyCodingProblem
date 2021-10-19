# THE PROBLEM
# Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted.
# The array below should return (1,3)
# had to look at the answer for this problem

array = [3, 7, 5, 6, 9]

def window(array):
    # new variables that are empty
    left, right = None, None

    print(left)
    print(right)

    # sort the array to start with
    s = sorted(array)
    print(f"Unsorted - {array}")
    print(f"Sorted - {s}")

    # range will return a tuple of integers that represent the first and last of the number of elements in the array
    for i in range(len(array)):
        # print the value of i
        print(i)
        # if the element in the original array doesn't match the element in the sorted array AND left is None
        if array[i] != s[i] and left is None:
            # left will equal the index value
            left = i
        elif array[i] != s[i]:
            right = i
    
    #this will return a tuple
    return left, right

# run the function!
result = window(array=array)

print(result)