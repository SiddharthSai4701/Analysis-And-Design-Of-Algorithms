# -*- coding: utf-8 -*-
"""
KnapSackMethod2.py

This program solves the 0/1 Knapsack problem using the greedy method. It sorts the objects in decreasing order of profit.

Created on Fri Sep 30 21:51:11 2022

@author: Siddharth Vijay Sai
"""

# w is the list of weights
w = list(map(int,input("Enter the values of the weights: ").split()))

# p is the list of profits
p = list(map(int,input("Enter the values of the profits: ").split()))

# M is the total capacity of the knapsack
M = int(input("Enter capacity of knapsack: "))

# x is the solution set but the elements aren't arranged in order
x = []

# t is the list of tuples containing tuples
# Each element is a tuple. Each tuple contains a tuple and an index.
# Each inner tuple contains a weight, profit pair corresponding to an object
# initially t is empty but is later populated based on the entries from the user
t = []


# I've used a for loop for two purposes:
    # 1.) To initialise all the elements of x to 0
    # 2.) To populate t with the appropriate tuples
    # The variable r is the tuple consisting of a weight, profit pair
for i in range(len(w)):
    x.append(0)    
    r = (w[i],p[i])
    t.append((r,i))      


# I've defined a function that sorts a list of tuples containing tuples in descending order of profits using Bubble Sort
# I chose Bubble Sort because it handles duplicate values without any modification

def Descending_Profits(a):
    for i in range(len(a)-1):
        
        for j in range(len(a)-i-1):
            
            if a[j][0][1]<a[j+1][0][1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

# Calling the sorting function to sort t and re-assigning the sorted list to t
t = Descending_Profits(t)

# Creating an empty list t to store the values of the selected objects. Note that I'm counting the OBJECT and not the INDEX of the object
selected = []

# Running a for loop to select appropriate objects as well as update the solution list
for i in range(len(w)):
    
    # if the capacity of the bag is greater than the weight of the object, select the object. Else, reject it
    if M-t[i][0][0]>=0:
        
        # if the object is selected, update the value at the corresponding index in the original solution array, x
        x[i] = 1
        
        # Also append the object number (index+1)
        selected.append(t[i][1]+1)
        
    # Update the space available in the knapsack by subtracting the weight of the current object
    M = M - t[i][0][0]

# Making a copy of the original solution array. This array will contain the objects in order (from 1 to N)
soln_x = x.copy()

# Declaring a variable profit and initialising it to 0
profit = 0

# Running a for loop to arrange the new solution list appropriately
for i in range(len(x)):
    temp = t[i][1]
    soln_x[i] = x[temp]    
    profit +=soln_x[i]*p[i]
    

# Printing the selected objects
print("The selected objects are: ",selected)
    
# Printing the new, sorted solution array
print("\nThe solution set is: ",soln_x)

# Printing the total cost
print("\nThe total profit is: ",profit)
