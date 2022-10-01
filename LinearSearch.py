# -*- coding: utf-8 -*-
"""
LinearSearch.py

Program no. 1

This program accepts n elements, sorted in ascending order, along with a search value from the user. It then proceeds to perform linear search
and returns the index at which the search value is found. If not found, it alerts the user of the same.

Created on Tue Sep  6 09:26:46 2022

@author: Siddharth Vijay Sai

Linear Search is a searching technique used to search for an element in a given array.

"""
# Function to perform Linear Search. Takes two arguments: the array and the search value
def LinearSearch(arr, search_val):
    
    # Outer for loop used to search through each element in the array
    for i in range(len(arr)):
        
        # If the search value is found, return the index
        if arr[i] == search_val:
            return f"{search_val} found at index {i}"
    
    # If the search value isn't in the array, return value not found
    if search_val not in arr:
        return f"{search_val} not found in {arr}"

# Taking array input from the user        
a = list(map(int, input("Enter your values: ").split()))

# Taking search value as input from the user        
k = int(input("Enter your search value: "))

# Calling the LinearSearch function
b = LinearSearch(a,k)
print(b)