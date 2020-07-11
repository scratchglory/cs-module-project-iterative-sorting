def linear_search(arr, target):
    # Your code here
    for num in range(0, len(arr)):
        if (arr[num] == target):
            return num
    # return False
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # searching between low and high indeces
    low = 0
    high = len(arr) - 1

    # loop so long as low hasn't moved passed high
    while low <= high:
        mid = (low + high) // 2

        # check if arr[mid] == target
        # base case where we've found our target
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            # toss out the right side since the target has to be on the left side
            # has to be on the left side
            # do this by setting high to be mid - 1
            high = mid - 1
        else:
            # toss out the left side since the target ahs to be on the right side
            # do this by setting low to be mid + 1
            low = mid + 1

    return -1  # not found


'''
1. figure out the midpoint index
2. compare the target against the midpoin element
    - if target M midpoint elem, then its on the left side
'''
