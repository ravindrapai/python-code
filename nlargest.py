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
