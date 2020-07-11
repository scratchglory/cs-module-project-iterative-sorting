# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements, the whole array
    for i in range(0, len(arr) - 1):
        cur_index = i
        # starts at our cur_index
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # iterate through the unsorted portion of the array, finding the index of the smallest element

        for j in range(i + 1, len(arr)):
            # update our smalles_index variable, if value < smallest_index element
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Swap the found minimum element with the first element
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     for i in range(0, len(arr) - 1):  # outer for loop
#         # INNER for loop; j will go from 0 to n - 1 because the last item in the list is already sorted
#         for j in range(0, len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# recursive implementation
# have to pass in unsorted length
def bubble_sort(arr, unsorted_length):
    # recursive implementation of bubble sort
    # base case
    # once we get to an empty unsorted portion, then everything is sorted
    # how to move closer to base?
    for i in range(0, unsorted_length - 1):
        if arr[i] > arr[i + 1]:
            # swaps them if the two elements aren't in order
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # must run the swapping first before the recursive
    # we've done one iteration of the swapping, check to see if there's more sorting to do
    if unsorted_length > 0:
        bubble_sort(arr, unsorted_length - 1)

    return arr


arr = [4, 3, 67, 34, 29, 30, 2, 15, 6]
bubble_sort(arr, len(arr))
print(arr)
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
