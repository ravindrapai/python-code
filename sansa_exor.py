'''
Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Can you help her in this task?

Note : [1,2,3] is contiguous subarray of [1,2,3,4] while [1,2,4] is not.

Input Format 
First line contains an integer T, number of the test cases. 
The first line of each test case contains an integer N, number of elements in the array. 
The second line of each test case contains N integers that are elements of the array.

Output Format 
Print the answer corresponding to each test case in a seperate line.

Constraints 
1≤T≤5 
2≤N≤105 
1≤numbers in array≤108

Sample Input

1
3
1 2 3
Sample Output

2
Explanation

1⊕ 2⊕ 3⊕ (1 ⊕ 2) ⊕ (2 ⊕ 3) ⊕ (1 ⊕  2 ⊕ 3) = 2
'''
t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    numbers = [int(i) for i in raw_input().split()]
    index = 0
    result = 0
    for number in numbers:
        frequency = (index + 1) * (n - index)
        index += 1
        if frequency%2:
            result = result ^ number
    print result
