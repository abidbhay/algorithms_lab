''' Lab1, Sec:1, ID: 20301115
            Task 4
'''
def MatrixMultiply(A,B):  #Algorithm to multiply two nxn matrix
    #Initialise empty matrix C
    n=len(A)
    C= [[0]*(n) for i in range(n)]
    for i in range(n): #multiplication loop
        for j in range(n):
            for k in range(n):
                C[i][j]+= int(A[i][k])*int(B[k][j])
    for row in C:  #print the matrix in output file
        outfile.write("\n")
        for column in row:
            outfile.write(str(column))
            outfile.write(" ")
        outfile.write("\n")

inpfile=open("matrixinput.txt","r")
outfile=open("matrixoutput.txt","w")
readinp=inpfile.read()
inp_list=readinp.split("\n")
A,B,i, flag=[],[], 0, ""
while i<len(inp_list):
    if inp_list[i]=="A":
        flag="A"
    elif inp_list[i]=="B":
        flag="B"
    elif inp_list[i]==None:
        break
    elif flag=="A":
        if inp_list[i]!="":
            A.append(inp_list[i].split(" "))
    elif flag=="B":
        if inp_list[i]!="":
            B.append(inp_list[i].split(" "))
    i+=1
MatrixMultiply(A,B)

inpfile.close()
outfile.close()