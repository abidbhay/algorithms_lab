# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:39:44 2021

@author: User
"""

inpfile=open("task1_input.txt","r")
outfile=open("task1_output.txt","w")
inp_list=inpfile.read()
readinp=inp_list.split("\n")

nodes=int(readinp[0])

edges=int(readinp[1])
readinp.pop(0)
readinp.pop(0)

newlst=[]
for i in readinp:
    a=i.split(" ")
    newlst.append(' '.join(a).split())
graph={}
for i in range(edges):
    key=int(newlst[i][0])
    value=int(newlst[i][1])
    if key not in graph:
        graph[key]=[value]
    else:
        graph[key]+=[value]
         



    

inpfile.close()
outfile.close()