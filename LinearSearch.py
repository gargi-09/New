# Algo1
# Linear Search

from cv2 import line
import numpy as np

def linear_search(arr,item):
    for index,x in enumerate(arr):
        if x==item:
            return f"Item found at index: {index}"
    return "Item not in the list"


string1=input("Enter a list of numbers:")
item=int(input("Enter the number to be searched:"))
l=[]
l=string1.split()
lst=[]
for x in l:
    ele=int(x)
    lst.append(ele)

print(linear_search(lst,item))


