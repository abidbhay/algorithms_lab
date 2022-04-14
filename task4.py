"""
Name: Abid Hossain
ID: 20301115
Sec: 1, Lab #2

@author: User
"""

#Merge Sort Algorithm

def Merge(l,r,A):
    i,j,k=0,0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            A[k]=l[i]
            i=i+1
        else:
            A[k]=r[j]
            j=j+1
        k=k+1
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
        mid=n//2
        l, r= [0]*(mid), [0]*(n-mid)
        for i in range(mid):
            l[i]=A[i]
        for j in range(mid,n):
            r[j-mid]=A[j]
    else:
        return
    MergeSort(l)
    MergeSort(r)
    Merge(l,r,A)
    
    return A
    

#tester section

inpfile=open("input4.txt","r")
outfile=open("output4.txt","w")

inp_list=inpfile.read().split("\n")
if len(inp_list)<2:
    raise Exception("Invalid Input. Must have two arguements")


size=int(inp_list[0])   #size of input array
#input array
arr=inp_list[1].split(" ")
arr=[int(i) for i in arr] #making items to int

MergeSort(arr)
for i in arr:
    outfile.write(str(i))
    outfile.write(" ")
  
    
#end program close files
inpfile.close()
outfile.close()