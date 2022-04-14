# -*- coding: utf-8 -*-

"""
Name: Abid Hossain
ID: 20301115
Sec: 1, Lab #2

@author: User
"""

#task 3
def InsertionSort(arr):   #Modified to work in a descending order
    i=1
    while i<len(arr):
        key=arr[i]
        j=i-1
        while j>=0 and key>arr[j]:  #changed here
            arr[j+1]=arr[j]
            j-=1
        i+=1
        arr[j+1]=key
    return arr
# getKey func returns the unique key of a certain value. 
def getKey(val,hashtable,final_list):
    for key,value in hashtable.items():
        if val==value and key not in final_list:
            return key
        
inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")
inp_list=inpfile.read().split("\n")
size=int(inp_list[0])
id=inp_list[1].split(" ")
id=[int(i) for i in id]
marks=inp_list[2].split(" ")
marks=[int(j) for j in marks]

if len(id)!=len(marks):
    print("Invalid input. Every id must have corresponding mark")
else:
    #create a hashtable to map id to marks. Python Dictionary
    hashtable={}
    for i in range(len(id)):
        hashtable[id[i]]=marks[i]
    marks=InsertionSort(marks)
    final_list=[]
    for item in marks:
        final_list.append(getKey(item,hashtable,final_list))
   
    
    #write files in the text file of task 3
    for element in final_list:
        outfile.write(str(element))
        outfile.write(" ")
        
inpfile.close()
outfile.close()



