# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    ''' Find the lowest element, and switch places with its place in the sequence '''
    # loop through n-1 elements
    for i in range(len(arr)-1):
        cur_index  = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = ar[cur_index], arr[smallest_index]

        print(arr)


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    ''' Highly Optimized Code From Lecture '''
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr




def insertion_sort(arr):
    # split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(arr)):
        print(arr)
        # Insert that element into the correct place in a sorted by:
        # Store the element in a temp variable
        temp = arr[i]
        # Shifting all larger sorted elements to the right by 1
        j = 1
        while j > 0 and temp < arr[j - 1]:
            counter += 1
            arr[j] = arr[j-1]
            j -= 1
        # insert the element after the first smaller element 
        arr[j] = temp
        print(f"counter: {counter}")
    return arr 


import random
l = [7,4,9,2,6,3,0,8,5,1]
#random.shuffle(l)
insertion_sort(l)