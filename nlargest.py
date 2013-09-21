'''
Given an unordered list of N elements, write a function to find the top four elements of the given list. Make sure your function runs in linear time O(N).
 
Input format :
 
First line of input contains N , number of elements in list.
Next N line , each contains a element.
 
Output format :
 
Print the top four elements of list.
'''
import heapq

count = int(raw_input())
result = []
# top 4 results
top = 4
#read n elements
while count:
    count -= 1
    item = int(raw_input())
    #if length is less than top add item to heap
    #if item is greater than smallest element remove it and add item
    if len(result) < top or item > result[0]:
        if len(result) == top:
            heapq.heappop(result)
        heapq.heappush(result, item)

#print it in reverse order
result = sorted(result, reverse = True)
for item in result:
    print item
