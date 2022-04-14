''' Lab1  
    Sec: 01
    ID: 20301115
    
#task 1 File I/O
'''
inpfile=open("input.txt","r")
outfile=open("output.txt","w")
recfile=open("records.txt","w")
read=inpfile.read()
inp_list=read.split("\n")
totalcount=0
palindrome_count=0
even_count=0
odd_count=0


def isPalindrome(word): 
    global palindrome_count
    if word=='': 
        return "not Palindrome",palindrome_count 
    if word== word[::-1]:
        return "a Palindrome",palindrome_count
    else:
        palindrome_count+=1
        return "a Palindrome",palindrome_count
    
def ParityChecker(num):  
    global odd_count
    global even_count
    if "." in num:
        return "cannot have parity", odd_count, even_count
    if num.isdigit()==False:
        return "cannot have parity", odd_count, even_count
    num=int(num)
    if num%2==1:
        odd_count+=1
        return "has odd parity", odd_count, even_count
    else:
        even_count+=1
    return 'has even parity', odd_count, even_count

    
for i in inp_list:
    item=i.split(" ")
    num=item[0]
    word=item[1]
    totalcount+=1
    check_num=ParityChecker(num)
    odd_count,even_count= check_num[1], check_num[2]
    check_num=check_num[0]
    check_word=isPalindrome(word)
    palindrome_count=check_word[1]
    check_word=check_word[0]
    outfile.write(str(num)+" "+check_num+" "+ "and "+word+ " is "+ check_word+"\n")

#Percentage Calculation
perc_pal=(palindrome_count/totalcount)*100
perc_notpal=100-perc_pal
perc_odd=(odd_count/totalcount)*100
perc_even=(even_count/totalcount)*100
perc_nullpar=100-perc_odd-perc_even
recfile.write(f"Percentage of odd parity: {int(perc_odd)}% \n")
recfile.write(f"Percentage of even parity: {int(perc_even)}% \n")
recfile.write(f"Percentage of no parity: {int(perc_nullpar)}% \n")
recfile.write(f"Percentage of palindrome: {int(perc_pal)}% \n")
recfile.write(f"Percentage of non-palindrome: {int(perc_notpal)}% ")

inpfile.close()
outfile.close()
recfile.close()