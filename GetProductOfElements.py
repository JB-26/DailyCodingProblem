# THE PROBLEM
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i

arry = [1,2,3,4,5]
# this will return 120, 60, 40, 30, 24

# function 
def productArray(arry):
    # array for calculations
    calculateArry = []
    arryLength = len(arry)
    print(f"Length of array - {arryLength}")

    for position in arry:
        print("Print integer in position")
        print(position)

        # copy the array
        arryCopy = arry.copy()

        # get the index position of element
        indexPostion = arryCopy.index(position)

        # remove the appropriate element in the array
        arryCopy.pop(indexPostion)

        # length of the copied array
        arryCopyLength = len(arryCopy)

        timesMultiplied = 1
        arryPostion = 0

        print("First calculation!")
        print(f"Value 1 - {arryCopy[arryPostion]}")
        print(f"Value 2 - {arryCopy[arryPostion + 1]}")
        newValue = arryCopy[arryPostion] * arryCopy[arryPostion + 1]

        while timesMultiplied < arryCopyLength - 1:
            print(f"Multiplying {newValue} by {arryCopy[arryPostion + 2]}")
            newValue = newValue * arryCopy[arryPostion + 2]
            timesMultiplied += 1
            arryPostion += 1
    
        # add the calculated value to a new array
        calculateArry.append(newValue)

    # return new array
    return calculateArry
    

# call function and print new array
sortedArry = productArray(arry)
print(sortedArry)