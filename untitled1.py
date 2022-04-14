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
# POPULATE A AND B FROM THE INPUT FILE

'''
1 2 3 4
5 6 7 8

1 2 3 4
5 6 7 8

'''

inpfile=open("matrixinput.txt","r")
outfile=open("matrixoutput.txt","w")
readinp=inpfile.read()
inp_list=readinp.split("\n")
print(inp_list)
A,B=[],[]

['0 1 2', '1 2 3', '0 1 2', '', '0 1 2', '1 2 3', '0 1 2']
boolean=True
for i in range(len(inp_list)):
    n=list(inp_list[i].split())
    if n==[]:
        boolean=False
    if boolean==True:
        A.append(n)
    elif boolean==False:
        if n!=[]:
            B.append(n)
 
print(A)
print(B)
MatrixMultiply(A,B)

inpfile.close()
outfile.close()