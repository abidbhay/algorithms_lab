"""
Name: Abid Hossain
ID: 20301115
Sec: 1, Lab #2

@author: User
"""

#task 2

#start program

def  SelectionSort(arr): #Selection Sort Algorithm
    i=0
    while i <   len(arr):
        min_idx, j=i, i+1
        while j<len(arr):
            if int(arr[j])<int(arr[min_idx]):
                min_idx=j
            j+=1
        arr[i], arr[min_idx]= arr[min_idx], arr[i] #swap minimum
        i+=1
        
    return arr

inpfile=open("input2.txt","r")
outfile=open("output2.txt","w")
read_inp=inpfile.read().split("\n")
firstline=read_inp[0].split(" ")
m=int(firstline[1])  # M number of the total items are needed to output

arr=read_inp[1].split(" ")
arr=[int(i) for i in arr] #list comprehension

# Call SelectionSort to sort the input array
sorted_arr=SelectionSort(arr)

#select from m items
prefer_list=sorted_arr[0:m]

#copy the preferlist to output file 
for item in prefer_list: 
    outfile.write(str(item))
    outfile.write(" ")

inpfile.close()
outfile.close()

#end program