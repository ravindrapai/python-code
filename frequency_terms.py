'''
Frequency Counting of Words / Top N words in a document.
 
Given N terms, your task is to find the k most frequent terms from given N terms.
 
Input format :
 
First line of input contains N, denoting the number of terms to add.
In each of the next N lines, each contains a term.
Next line contains k, most frequent terms.
 
Output format :
 
Print the k most frequent terms in descending order of their frequency. If two terms have same frequency print them in lexicographical order.
 
Sample input :
 
14
Fee
Fi
Fo
Fum
Fee
Fo
Fee 
Fee
Fo
Fi
Fi
Fo
Fum
Fee
3
 
Sample output :
 
Fee
Fo
Fi
 
Constraint :
0 < N < 300000 
0 < term length < 25.
'''
count  = int(raw_input())
word_frequency = {}
while count > 0:
    count -= 1
    word = raw_input()
    frequency = word_frequency.get(word)
    if frequency:
        word_frequency[word] = frequency + 1 
    else:
        word_frequency[word] = 1
k = int(raw_input())
#print word_frequency
sort_frequency = {}
for word in word_frequency:
    frequency = word_frequency.get(word)
    #add it to list with same frequency
    if frequency in sort_frequency:
        sort_frequency[frequency].append(word) 
    else:
        sort_frequency[frequency] = [word]      
# get key in ascending order
for key in sorted(sort_frequency, reverse=True):
    #lexicographic order
    wordlist = sort_frequency[key]
    wordlist.sort()
    for word in wordlist:
        print word
        k -= 1
        if k == 0:
            exit()

