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
