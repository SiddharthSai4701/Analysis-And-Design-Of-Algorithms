# -*- coding: utf-8 -*-
"""
BinarySearchUsingDivideAndConquer.py

Program no. 2

This program performs binary search (which implements the technique of divide and conquer).

Created on Tue Sep  6 09:27:45 2022

@author: Siddharth Vijay Sai
"""

# Binary Search using recursive method

def BinarySearch(lst,search_value,low,high):
    
    if high>=low:
        
        # Calculate the middle index, i.e, (low index + high index)/2
        mid = int((low+high)/2)
        
        # If the value at the middle index is equal to the search value, return the index value
        if lst[mid] == search_value:
            return f"The value was found at index {mid}"
        
        # If the value at the middle index is greater than the search value, recursively call the Binary Search function
        # Since the value at mid is greater than the search value, the element to be found must be to the left of mid
        # Hence, the value of the high index is given as mid-1
        elif lst[mid]>search_value:
            return BinarySearch(lst, search_value, low, mid-1)
        
        # If the value at the middle index is lesser than the search value, recursively call the Binary Search function
        # Since the value at mid is lesser than the search value, the element to be found must be to the right of mid
        # Hence, the value of the low index is given mid+1
        else:
            return BinarySearch(lst, search_value, mid+1, high)
        
    # If the search value isn't in the list, return "Element not found"
    else:
        return "Element not found"
    
# Accepting sorted values in ascending order from the user into a list
l = list(map(int, input().split()))

# Accepting the search value from the user
x = int(input("Enter the search value: "))

# Calling the BinarySearch function and storing the return value in r
r = BinarySearch(l,x,0,len(l)-1)

# Printing r
print(r)