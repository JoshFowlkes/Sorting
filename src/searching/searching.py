# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in arr:
    if i == target:
      return True
   return False   


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  # cut our list in half, examine the midpoint item
  


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  start = 0
  end = len(arr)
  while end - start > 0:
    mid = start + (end - start) // 2
    item = arr[mid]
    print(start)
    print(mid)
    print(end)
    print('***')
    # If the item is equal to arr:
    if item == target:
      return True
    # Otherwise if its smaller
    elif item > target:
      end = mid - 1
      # Repeat binary search on first half of the list
    # Otherwise
    else:
      start = mid + 1
  return False # not found