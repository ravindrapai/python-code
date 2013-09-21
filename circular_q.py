'''
Implement a circular buffer of size N. Allow the caller to append, remove and list the contents of the buffer. Implement the buffer to achieve maximum performance for each of the operations.

The new items are appended to the end and the order is retained i.e elements are placed in increasing order of their insertion time. When the number of elements in the list elements exceeds the defined size, the older elements are overwritten.
 
 
There are four types of commands.
 
"A"  n -  Append the following n lines to the buffer. If the buffer is full they replace the older entries.
"R"  n -  Remove first n elements of the buffer. These n elements are the ones that were added earliest among the current elements.
"L"   - List the elements of buffer in order of their inserting time.
"Q"  - Quit.  
 
Your task is to execute commands on circular buffer.
 
Input format :
 
First line of input contains N ,  the size of the buffer.
A n  - append the following n lines to the buffer.
R n - remove first n elements of the buffer.
L - list the buffer.
Q - Quit.
 
Output format :
 
Whenever  L command appears in the input, print the elements of buffer in order of their inserting time. Element that was added first should appear first. 
'''
from collections import deque

size = int(raw_input())

Buffer = deque([], size)
while True:
    command = raw_input()
    if command == 'L':
        #display the element
        for item in Buffer:
            print item
    elif command == 'Q':
        #quit
        break
    else:
        try:
            command, count = command.split(' ', 1)
            count = int(count)
            if command == 'A':
                while count > 0:
                    count -= 1
                    element = raw_input()
                    Buffer.append(element)
            elif command == 'R':
                while count > 0:
                    count -= 1
                    Buffer.popleft()
            #invalid command
        except:
            continue
