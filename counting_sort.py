def counting(A,k):
    k += 1
    c = [0] * k
    j = 0
    for i in range (0,len(A)):
        c[A[i]] +=1
    for i in range (0,len(c)):
        if c[i] > 0:
            for k in range (0,c[i]):
                A[j] = i
                j += 1

A = [2,4,1,5,4,2,3,6,6,5,7,8,9,5,7,1,0,0,2]
counting(A,9)
print(A)