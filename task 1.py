"""
Name: Abid Hossain
ID: 20301115
Sec: 1, Lab #2

@author: User
"""


#Task1


# MODIFIED BubbleSort Algorithm
def bubblesort(arr):
    flag=1  # variable used to check for an already sorted arr

    for i in range(  len(arr)  -  1  ):    
        for j in range(  len(arr) - i  - 1  ):
            
            if arr[j]>arr[j+1]:
                
                arr[j+1], arr[j]= arr[j], arr[j+1]       #    SWAP
                flag=-1
        if flag==1: # If flag is default 1, no swaps occured in first pass
            break     # which means array is already sorted.
    return arr 


#tester section

inpfile=open("input1.txt","r")
outfile=open("output1.txt","w")

inp_list=inpfile.read().split("\n")
if len(inp_list)<2:
    raise Exception("Invalid Input. Must have two arguements")
size=int(inp_list[0])
arr=inp_list[1].split(" ")
arr=[int(i) for i in arr] #making int from str input
bubblesort(arr)

#write into output file
for element in arr:
    outfile.write(str(element))
    outfile.write(" ")
 

#end    
inpfile.close()
outfile.close()
    