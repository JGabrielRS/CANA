def pivotacao(A,ini,f,x):
    j = ini - 1
    for i in range (ini,f):
        if A[i] <= A[x]:
            j+=1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[x]
    A[x] = A[j+1]
    A[j+1] = temp
    return j+1
def quicksort(A,i,f):
    if i >= f:
        return
    q = pivotacao(A,i,f,f)
    quicksort(A,i,q-1)
    quicksort(A,q+1,f)
    
A = [1,4,6,3,2,4,6,8,9,2,3,4,5,6,7,8,9,21,11,21]
quicksort(A,0,len(A)-1)
print(A)