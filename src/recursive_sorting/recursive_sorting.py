# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr




''' Class Notes on Recursion '''
def exponent(base, power):
    print(power)
    if power == 0:
        return 1
    elif power == 1:
        return base
    return base * exponent(base, power-1)

def exponent_iterative(base, power):
    total = base
    for i in range(power - 1):
        total *= base
    return total

''' Anything you can solve recursively, you can
    solve iteratively
'''
    
# Quick Sort
# 1. Pick a pivot and move it until everthing on the left is smaller,
# everything on the right is greater 
# 2. REcursively quicksort the left half, then the right half 

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = []
    larger = []
    for i in range(len(arr) - 1):
        element = arr[i]
        if element < pivot:
            smaller.append(element)
        else:
            # you have to TRUST that its returning the sorted list
    return quicksort(smaller) + [pivot] + quicksort(larger)
