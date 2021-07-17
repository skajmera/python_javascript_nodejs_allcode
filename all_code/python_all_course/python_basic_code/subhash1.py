# a=0
# i=10
# while i>0:
#     print("enter numbeer")
#     b=int(input())
#     a=a+b
#     i=i-1
# print("average is",a/1)



# number=[54,21,65,48,65]
# b=0
# for i in number:
#     b=b+1
# print(b)


# num=[56,25,36,48,87,54]
# b=0
# for i in num:
#     if i>20 and i<40:
#         b=b+1
#         print(i)
# print(b)




# num=[25,65,41,70,23,56]
# num=max(num)
# print(num)


# num=[45,5,6,8,66,92,5,54]
# num.sort()
# print(num[-2])




# a=input()
# b=""
# for i in a:
#     b=i+b
# if a==b:
#     print("yes")
# else:
#     print("no")
# 

# num=[17,59,18,19,20,1,2,4,56,76,7,5,46,36,56,89,98,8,890,8,9]
# prime=[]
# even=[]
# odd=[]
# for i in range(2,len(num)):
#     if num[i]>1 and i in num:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             prime.append(i)
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(prime)
# print(even)
# print(odd)
##############################################################################################

# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# for i in num:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i==1:
#             continue
#         prime.append(i)    
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
# #         odd.append(i)
# # print(prime,"prime")
# # print(odd,"odd")
# # print(even,"even")
# ####################################################################################################

# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,289,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# while a<len(num):
#     if num[a]%2==0:
#         even.append(num[a])
#     else:
#         odd.append(num[a])
#     a+=1
# for i in num:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i==1:
#             continue
#         prime.append(i)    
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")
#####################################################################
# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# while a<len(num):
#     if num[a]%2==0:
#         even.append(num[a])
#     else:
#         odd.append(num[a])
#         if(num[a]%3!=0 and num[a]%5!=0):
#             prime.append(num[a])
#     a+=1
    
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")
# #####################################################################

# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# while a<len(num):
#     if num[a]%2==0:
#         even.append(num[a])
#     else:
#         odd.append(num[a])
#         if num[a]>1:
#             if(num[a]%3!=0 and num[a]%5!=0):
#                 prime.append(num[a])
#     if num[a]==2 or num[a]==3:
#         prime.append(num[a])

        
#     a+=1
    
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")
################################## odd even prime #############
# num=[289,121,131,1,2,251,3,4,5,6,361,7,8,9,10,11,12,13,14,15,16,17,18,19,20,289,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# prime=[]
# odd=[]
# even=[]
# a=1
# while a<len(num):
#     if num[a]%2==0:
#         even.append(num[a])
#     else:
#         odd.append(num[a])
#         if num[a]>1:
#             if(num[a]%3!=0 and num[a]%5!=0 and num[a]%7!=0):
#                 prime.append(num[a])
#     if (num[a]==2 or num[a]==3 or num[a]==5 or num[a]==7):
#         prime.append(num[a])

        
#     a+=1
    
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")

# ###########################################################
# magic_square = [
#     [ 4,2,2,5],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# print (type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))

# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2])) 

#######################################
# num=[45,67,89,1,2,3,4,5,6,7,8,9,10,11,12,45,7,9,289,89,55,13,14,15,16,17,18,19,20]
# prime=[]
# odd=[]
# even=[]
# a=1
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i==1:
#             continue
#         prime.append(i)          
# print(prime,"prime")
# print(odd,"odd")
# print(even,"even")
# ##################################################

# a=[[1,2,3],[4,5,6],[7],[8,9]]
# import itertools
# flat=list(itertools.chain(*a))
# # print(*a)
# b="riyaz"
# # c=(list(b))

# # print(*c)
# a.append([6])
# print(a)
# from collections import deque
# a=[1,2,3,4,5,6]
# b=deque(a)
# b.rotate(-1)
# print(b)

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# length = len(students) 
# counter = 0
# while counter < length:
#     print (students[counter] + str(marks[counter]))
#     counter+=1 


# number=[54,21,65,48,65]
# b=0
# for i in number:
#     b=b+1
# print(b)


# num=[56,25,36,48,87,54]
# b=0
# for i in num:
#     if i>20 and i<40:
#         b=b+1
#         print(i)
# print(b)




# num=[25,65,41,70,23,56]
# num.sort()
# print(num[-1])


# num=[25,65,41,70,23,56]
# num=max(num)
# print(num)


# num=[45,5,6,8,66,92,5,54]
# num.sort()
# print(num[-2])

# num=[25,65,41,70,23,56]
# for i in range(1,len(num)):
#     print(num[i])

# if a[i]<a[i]:
#         print(a[i])
#     else:
#         print(a[i])
 #print(a[i])
# d=[]
# c=[]
# a=(7,6,54,2,3,4,5,95,6)
# d=a[0]
# for i in range (0,len(a)):
#     if a[i]>d:
#         print(a[i],"maximum")
############################################################
# a=[1,105,90,7,6,54,100,2,3,4,5,95,6]
# d=a[0]
# for i in a:
#     if i>d:
#         d=i
# print(d,"max")



########################

# pl=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# a=1
# rev_rse=[]
# for i in(pl):
#     rev_rse.append(pl[-a])
#     a+=1
# print(rev_rse)

# x=["n","subh","i","t","i","hh","n"]
# y=[]
# a=1
# for i in x:
#     if x[-a]==i:
#         y.append(x[-a])
#     a+=1
# if x==y:
#     print("palindrome")
# else:
#     print("not palindrome")        

###########################################
# x=["n","k","t","i","n"]
# y=[]
# for i in range(len(x)):
#     if x[i]==x[-i-1]:
#         y.append(x[i])
# if x==y:
#     print('this is palindrome')
# else:
#     print('this is not a palindrome')
##########################################################
# x=["n","k","t","i","n"]
# y=[]
# a=0
# while a<len(x):
#     if x[a]==x[-a-1]:
#         y.append(x[a])
#     a+=1
# if x==y:
#     print(" this is palindrome")
# else:
#     print("this is not palindrome")

###################################################################

# x=["n","k","t","i","n"]
# y=[]
# a=0
# while a<len(x):
#     if x[a]==x[-a-1]:
#         y.append(x[a])
#     a+=1
# if x==y:
#     print(" this is palindrome")
# else:
#     print("this is not palindrome")

#####################################################################

# binary= [1, 0, 0, 1, 1, 0, 1, 1] 
# y=[]
# a=1
# summ=0
# total=0
# b=0
# for i in binary:
#     summ=binary[-a]*2**b
#     total=total+summ
#     y.append(summ)
#     a+=1
#     b+=1
# print(y)
# print(total)


#######################################    banary   banary  
# binary= [1, 0, 0, 1, 1, 0, 1, 1] 
# y=[]
# a=1
# summ=0
# total=0
# b=0
# for i in binary:
#     summ=binary[-a]*2**b
#     total=total+summ
#     #y.append(summ)
#     a+=1
#     b+=1
# #print(y)
# print(total)

   


###########################################3  strong password   



# pas=input("enter password")
# if len(pas)>8 and len(pas)<16:
#     if ("A"in pas or"B" in pas or"C" in pas or"D" in pas or"E"in pas or"F" in pas or"H" in pas or "I"in pas  or "J"in pas or "K"in pas or "L"in pas or "M"in pas or "N"in pas or "O"in pas or "P"in pas or "Q"in pas or "R"in pas or "S"in pas or "T"in pas or "U"in pas or "V"in pas or "W"in pas or "X"in pas or "Y"in pas  or "Z"in pas):
#         if ("a"in pas or"b"in pas or"c"in pas or"d"in pas or"e"in pas or"f"in pas or "g"in pas or"h"in pas or"i"in pas or"j"in pas or"k"in pas or"l"in pas or"m"in pas or"n"in pas or"o"in pas or"p"in pas or"q"in pas or"r"in pas or"s"in pas or"t"in pas or"u"in pas or"v"in pas or"w"in pas in pas or"x"in pas or"y"in pas or"z"in pas):
#             if "@"in pas  or "#"in pas or "$"in pas  or "!"in pas:
#                 if ("1"in pas  or "2"in pas  or "3"in pas  or "4"in pas  or "5"in pas  or "6"in pas  or "7"in pas  or "8"in pas or"9"in pas or"0"in pas):
#                     print("correct password")
#                 else:
#                     print("enter number")
#             else:
#                 print("not special character")
#         else:
#             print("small")           
#     else:
#         print("capital")
# else:
#     print("enter 8 to 16 character
# 
# ###############################################################################################  two list ek chalana 
# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# print (len(students))
# print (len(marks))
# length = len(students) 
# counter = 0
# while counter < length:
#     print ((students[counter]) + str(marks[counter]))
#     counter+=1
###########################################################################3

# lst1 = [1,2,3,4,5,6,10,9,11]
# list2 = [2,3,1,0,6,7,2,5,6] 
# x=[]
# for i in list1:
#     a=0
#     for j in list1:
#         if list1[j]==list2[a]:
#             x.append(list1[j])
#         else:
#             print(list2[j],"yyyyy")
#         a+=1
#     print(x)

##############################################  list compare 

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7] 
# a=0
# x=[]
# for i in list1:
#     if i in list2:
#         continue
#     else:
#         print(i)

################################################################

# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(sum(list1[0]))
# print(sum(list1[1]))
# print(sum(list1[2]))
# for 
################################################################  for loop iterate  
# a=[1]
# for i in a:
#     a.append(i)
#     print(a)
################################################################



# a=0
# i=10
# while i>0:
#     print("enter numbeer")
#     b=int(input())
#     a=a+b
#     i=i-1
# print("average count is",a/1)

#########################################################  max 

# a=[1,105,90,7,6,2,54,100,2,3,4,5,95,6]
# d=a[0]
# for i in a:
#    if i>d:
#        d=i
# print(d)
################################################################   minimum
# a=[1,105,90,7,6,2,54,100,2,3,4,5,95,6]
# d=0
# for i in a:
#    if i<d:
#        d=i
# hangman=1,2,3,4,5,6,7
# print("wel-come")
# name=input("what is yourname")
# print("hello,"+name,"time to lay hangman")
# word=["subhash","abhishek","pawan","tushar","ajay","atul","sanjay"]
# guesses=("")
# while True:
#     a=1
#     t=7
#     while t>0:
#         b=0
#         for i in word:
#             if i in guesses:
#                 print(i)
#             else:
#                 print("________")
#                 b=+1
#         if b==0:
#             print("you won")
#             break
#         guess=input("guess the character")
#         guesses+=guess
#         if guess not in word:
#             t-=1
#             print(hangman[-a])
#             a+=1
#             print("you have",+t,"more guess")
#             if t==0:
#                 print("you are lose")
#     print("do you want play: y/n")
#     again=input()
#     if again=="y":
#         print("thank you")
#         guesses="0"
        
#     else:
#         print("good bye")
#         break   


# hangman= ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# print("wel-come")
# name=input("what is yourname\n")
# print("hello,"+name,"time to lay hangman")
# word=["subhash","abhishek","pawan","navid","ajay","atul","sanjay"]
# guesses=("")
# while True:
#     a=1
#     t=7
#     while t>0:
#         b=0
#         for i in word:
#             if i in guesses:
#                 print(i)
#             else:
#                 print("________")
#                 b=+1
#         if b==0:
#             print("you won")
#             break
#         guess=input("guess the character\n")
#         if guess in guesses:
#             print("already use this word")
#         guesses+=guess
#         if guess not in word:
#             t-=1
#             print(hangman[-a])
#             a+=1
#             print("you have",+t,"more guess")
#             print("do you help me: yes/no")
#             help=input()
#             if help=="yes":
#                 for i in range(1):
#                     print("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
#                     helpp=input("you have 3 chance")
#                     if helpp=="1":
#                         print("*ajay*")
#                     elif helpp=="2":
#                         print("*pawan*")
#                     elif helpp=="3":
#                         print("*abhishek*")
#             elif help== "no":
#                 print("ok")
            
                
#             if t==0:
#                 print("you are lose")
#     print("do you want play: y/n")
#     again=input()
#     if again=="y":
#         print("thank you")
#         guesses="0"
        
#     else:
#         print("good bye")
#         break   


# hangman= ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# print("wel-come")
# name=input("what is your name\n")
# print("hello,"+name,"time to lay hangman")
# word=["subhash","abhishek","pawan","navid","ajay","atul","sanjay"]
# guesses=("")
# while True:
#     a=1
#     t=7
#     while t>0:
#         b=0
#         for i in word:
#             if i in guesses:
#                 print(i)
#             else:
#                 print("________")
#                 b=+1
#         if b==0:
#             print("you won")
#             break
#         guess=input("guess the character\n")
#         if guess in guesses:
#             print("already use this word")
#         guesses+=guess
#         if guess not in word:
#             t-=1
#             print(hangman[-a])
#             a+=1
#             print("you have",+t,"more guess")
#             print("do you help me: yes/no")
#             help=input()
#             if help=="yes":
#                 for i in range(1):
#                     print("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
#                     helpp=input("you have 3 chance")
#                     if helpp=="1":
#                         print("*ajay*")
#                     elif helpp=="2":
#                         print("*pawan*")
#                     elif helpp=="3":
#                         print("*abhishek*")
#             elif help== "no":
#                 print("ok")
            
                
#             if t==0:
#                 print("you are lose")
#     print("do you want play: y/n")
#     again=input()
#     if again=="y":
#         print("thank you")
#         guesses="0"
        
#     else:
#         print("good bye")
#         break   
#######################################################################

##########################################3  bubble  shorting  

# a=[5,1,4,2,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
# print(a)


# ########################################################  list  input 
# a = int(input("enter your list lenght: "))
# b = []
# for i in range(a):
#     c = int(input("enter your element: "))
#     b.append(c)
# print(b)


########################################################################################3 sort function 





#def my(num):
#    num.reverse()
#    print(num)
#my([6,85,89,8])
#
#
#













