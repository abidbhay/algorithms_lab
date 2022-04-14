A=[24,41,49,50,56,76]
count=0
def Merge(l,r,A):
    global count
    i,j,k=0,0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            A[k]=l[i]
            i=i+1
        else:
            A[k]=r[j]
            j=j+1
        k=k+1
        count+=1
    while i<len(l):
        A[k]=l[i]
        i,k=i+1,k+1
    while j<len(r):
        A[k]=r[j]
        j,k=j+1,k+1
    return

def MergeSort(A):
    n=len(A)
    if len(A)>1:
        mid=(n)//2
        l=A[0:mid]
        r=A[mid:]
    else:
        return
    
    MergeSort(l)
    MergeSort(r)
    Merge(l,r,A)
    
    return A
print(MergeSort(A))
print(count)