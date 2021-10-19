# THE PROBLEM
# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array
# Example; [3, 4, 9, 6, 1] returns [1, 1, 2, 1, 0]

# create array
arry = [3, 4, 9, 6, 1]

def smaller_counts(arry):
    smallerArry = []

    for index, i in enumerate(arry):
        counter = 0
        # nested for loop when it reaches the end of the array it stops
        for x in arry[index + 1:]:
            if x < i:
                counter += 1
        smallerArry.append(counter)
    
    # return the new array
    return smallerArry
        

# call function
result = smaller_counts(arry)
print (f"Original input - {arry}")
print(f"Result - {result}")