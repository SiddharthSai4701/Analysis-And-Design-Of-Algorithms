# -*- coding: utf-8 -*-
"""
KnapSackMethod3.py

This program solves the 0/1 Knapsack problem using the greedy method. It sorts the objects in decreasing order of profit/weight.

Created on Fri Sep 30 14:50:16 2022

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
    
# Creating a list contains tuples
# The 0th index of each tuple contains ratios of profits to weights of the objects
# The 1st index contains the index values of the objects. This will be useful in sorting later
pi_by_wi = [(t[i][0][1]/t[i][0][0],i) for i in range(len(w))]


# Defining a function that takes a list of tuples as an argument and sorts it in descending order using bubble sort
def Descending(a):
    for i in range(len(a)-1):
        
        for j in range(len(a)-i-1):
            
            if a[j][0]<a[j+1][0]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

# Sorting the list in descending order
pi_by_wi = Descending(pi_by_wi)

# Lines 37 - 41 can also be done as shown in line 44
# pi_by_wi = s.Descending_Profits([(t[i][0][1]/t[i][0][0],i) for i in range(len(w))])

# Creating a variable profit and initialising it to 0
profit = 0

# Creating an empty list to store the selected objects
selected = []

# Running a for loop to check how many of the objects will fit into the knapsack
for i in range(len(pi_by_wi)):

    # If the weight of an object is less than the available space in the knapsack, it is selected    
    if M - w[pi_by_wi[i][1]]>=0:
        
        # If the object is selected, the index of that object is referred to in the list of tuples and added to the list of selected objects
        selected.append(pi_by_wi[i][1])

        # Also, the value at the corresponding index in the solution list is updated to 1
        x[pi_by_wi[i][1]] = 1
        
    # The available space in the knapsack is updated after each run of the loop
    M-= w[pi_by_wi[i][1]]
        
# Printing the selected object NUMBERS (not INDICES)
print("The selected objects are: ",[i+1 for i in selected])

# Printing the solution list, x
print("The solution set is: ",x)

# Calculating the total profit
for i in range(len(x)):
    profit+= p[i]*x[i]
    
# Printing the total profit
print("The total profit is: ",profit)
