import sys

#use dynamic programming to tabulate the length of the longest common bitonic subsequence
def LCBS(a, b): 
    #filter the hexadecimals that are common to the 2 given sequences
    a, b = [int(i,16) for i in a if i in b], [int(i,16) for i in b if i in a]
    #set n to be the length of sequence a and m to be the length of sequence b
    n , m = len(a), len(b)
    #create a table to save the length of the longest common increasing subsequence 
    front = [0] * m 
    #create a table to save the length of the longest common decreasing subsequence
    back = [0] * m 
    #create a table to save the length of the longest common bitonic subsequence
    result = [0] * m 
    
    for i in range(n):
        #create counter to save the longest common increasing subsequence found thus far
        fcounter = 0
        #create counter to save the longest common decreasing subsequence found thus far
        dcounter = 0
        for j in range(m):
            #when common elements are found from the front of both sequences
            if (a[i] == b[j]): 
                front[j] = max(front[j], fcounter+1)
            if a[i] > b[j]: 
                fcounter = max(front[j], fcounter) 
            #when common elements are found from the rear of both sequences
            x = n-1-i
            y = m-1-j
            if (a[x] == b[y]): 
                back[y] = max(back[y], dcounter+1)
            if a[x] > b[y]: 
                dcounter = max(back[y], dcounter)
    #add the length of the longest common increasing and decreasing subsequence and deduct 1 to account for the duplication
    for i in range(len(front)):
        result[i] = front[i] + back[i] - 1
    return max(result)
    
num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    print(LCBS(a, b))