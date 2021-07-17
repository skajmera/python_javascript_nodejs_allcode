
##############################   1   se 10 tak devide  

#a=1
#total=int(input())
#b=1
#while a<total:
#    b=1
#    while b<=10:
#        if a%b==0:
#            if b==10:
#                print(a,"devide h")
#                break
#        else:
#            break
#        b+=1
#    a=a+1
#


# num=1
# while num<=100:
#     if num%3==0:
#         print("nav")
#     if num%7==0:
#         print("gurukul")
#     if (num%3==0 and num%7==0):
#         print("navgurukul")
#     else:
#         print(num)
#     num=num+1

#########################################

# total=0
# count=50
# while count>40:
#     a=int(input())
#     total=total+a
#     count=count-1
# print(total)
#
######################################
# bina multiple kiye bina multiple krna 
# g=0
# c=0
# a=int(input())
# b=int(input())
# while c<a:
#     g=g+b
#     c=c+1
# print(g)
#############################################
#
#b=0
#a=1
#while b<10:
#    b=a/2
#    print(a)
#    a=a+1         
##################################################
# counter=156
# while counter>146:
# 	b=(counter-146)-11
# 	counter=counter-1
# 	print(-b)
################################################
# d=0
# a=int(input("kitni baar input le"))
# while a>0:
# 	b=int(input())
# 	a=a-1
# 	d=d+b
# print(d)
##############################################3
# a=int(input())
# for i in range(1,a):
# 	for j in range(1,i+1):
# 		print ("*",end="")
# 	print("")

#####################################333
# a=int(input())
# for i in range (a,0,-1):
# 	for j in range (1,i+1):
# 		print("*",end="")
# 	print("")	
####################################3
# a=int(input())
# for i in range (1,a):
# 	for k in range (1,a-1):
# 		print("",end="")
# 	for j in range (1,i+1):	
# 		print("*",end="")
# 	print("")

########################################33


# a=int(input())
# b=0
# while b<a:
# 	print(""*(a-b-1)+"*"*(b+1))
# 	b+=1

#############################################################


# a=int(input())
# for i in range(a):
# 	print(""*(a-i-1)+"*"*(i+1))


###############################################
# a=int(input())
# b=1
# c=b+a
# for i in range(a):
# 	print(""*c,"*"*b)
# 	b=b+1
# 	c=c+1

####################################################3

# num=20
# while num<=100:
# 	if num%2==0:
# 		print(num)
# 	num+=1


############################################
# num=1
# while num<=100:
# 	if num%7==0:
# 		print(num)
# 	num+=1


###############################################
# sum=0
# num=12
# while num<=421:
# 	sum=sum+num
# 	print(num)
# 	num+=1
# print(sum)


###############################################################3
# sum=0
# num=30
# while num<=420:
# 	if num%8==0:
# 		print(num)
# 		sum=sum+num
# 	num+=1
# print(sum)

#######################################


# sum=0
# num=1
# while num<=48:
# 	print(num)
# 	sum=sum+num
# 	num+=1
# print(sum)
#####################################
# sum=0
# a=1
# while a<=11:
# 	b=int(input())
# 	sum=sum+b
# 	a+=1
# print(sum)
# if sum%5==0:
# 	print("5 k multiple h")
# else:
# 	print("nhi hai")

#################################################33


# a=1
# while a<=100:
# 	if a%2==0:
# 		print(a)
# 	else:
# 		print(-a)
# 	a+=1

##############################################

##guessing game

# num=5
# a=1
# while a<=6:
# 	b=int(input("1 se 10 k beech m no. guess kro:"))
# 	if b==num:
# 		print("congratulation")
# 		break
# 	a+=1
# if a==7:
# 	print("users ne koi no. guess nhi kra")

##############################################################3      guessing game    


# num=5
# a=1
# while a<=10:
# 	b=int(input("1 se 10 k beech m no. guess kro:"))
# 	if b<num:
# 		print("aapka number chhota he ")
# 	elif b>num:
# 		print("aapka number bda he")
# 	else:
# 		print("aap game jeet gye")
# 		print("congratulation")
# 		break
# 	a+=1
# if a==11:
# 	print("users ne koi no. guess nhi kra")s

# ###########################################
                                                   #bina multiple kiye bina multiple krna 

# g=0
# c=0
# a=int(input())
# b=int(input())
# while c<a:
# 	g=g+b
# 	c=c+1
# print(g)


################################################################

# c = 0
# d = 1

# while c < 3:
#     c = c + 1
#     d = d * c
#     print("Loop Ke Andar", c, d)
# else:
#     print ("Loop Ke Bahar", c, d )



#############################################################

# n = 6
# s = 0
# i = 1

# while i <= n:
#     s = s + i
#     i = i + 1

# print(s)


####################################################3           prime number 
# num=int(input())
# i = 2
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#    	print(num, 'is a prime number')

########################################################

# n=int(input())
# count = 0
# i=1
# while (i<=n):
# 	if (n%i==0):
# 		count=count+1
# 	i=i+1
# if (count==2):
# 	print("prime number")
# else:
# 	print("not number")

############################################333

# i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print ("*") 
#         j = j + 1    
#     print ('')
#     i = i + 1
 


##########################################################          bugs   




# x = 0
# while(x<7):
#     if (x == 3 or x==5):
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1 


#########################################################

# index = 1
# while(index < 10):
# 	print(index)
# 	index = index + 1


##################################################

# sum=0
# i = 1
# while(i <= 140):
#     if(i % 3 == 0):
#     	sum = sum + i
#     i = i + 1
# print(sum) 


##########################################################

# i=0
# while(i<10):
# 	j = 0
# 	while(j<=5):
# 		print(j)
# 		j = j + 1
# 	i = i + 1
 



############################################################      positive negetive number    
# i = 0
# num = int(input("Enter your number:- "))
# while(i <= num):
#     if(num >0):
#         print(num," is positive")
#         break
#     elif(num<0):
#     	print(num,"is negetive")
#     else :
#         print(num,"zero")
#     i = i + 1
# if num<0:
# 	print("negetive")

#  ###############################################################      lenth nikalna



# num= int(input())
# count=0
# while num!=0:
# 	num//=10
# 	count+=1
# print("total digit are",count)


#####################################################################

#                                                                            # fibonacci  
# n=int(input())
# x=0
# y=1
# z=0
# while z<=n:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y



######################################################################



# num=int(input())
# if(num==2 or num ==3):
# 	print("prime number")
# elif (num%2==0 or num%3==0 or num%5==0):
# 	print("not prime number")
# else:
# 	print("prime")
#######################
#
#################################################################################


# print("wel-come to punjab nation bank ")
# pin=input("enter your correct four digit password:")
# balance=10000
# if len(pin)==4:
# 	print("correct password")
# 	b=1
# 	while b==1:
# 		choice=int(input('''please choose an option: 
# 			1-withdraw,
# 			2-deposit,
# 			3-check balance, 
# 			4-exit:'''))
# 		if choice==1:
# 			withdraw=float(input('''select your amount:-
# 				1 withdraw 500,
# 				2 withdraw 1000,
# 				3 withdraw 1500,
# 				4 withdraw 2000,or
# 				(enter your amount)'''))
# 			if withdraw==1:
# 				balance=balance-500
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==2:
# 				balance=balance-1000
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==3:
# 				balance=balance-1500
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			elif withdraw==4:
# 				balance=balance-2000
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance-withdraw
# 				print("successfull withdraw")
# 				print("current balance:$",balance)
# 		elif choice==2:
# 			deposit=float(input('''select your amount:-
# 				1 deposit 500,
# 				2 deposit 1000,
# 				3 deposit 1500,
# 				4 deposit 2000,or
# 				(enter your amount)'''))
# 			if deposit==1:
# 				balance=balance+500
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==2:
# 				balance=balance+1000
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==3:
# 				balance=balance+1500
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			elif deposit==4:
# 				balance=balance+2000
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance+deposit
# 				print("successfull deposit")
# 				print("current balance:$",balance)
# 		elif choice==3:
# 			print(balance)
# 		elif choice==4:
# 			print("good bye")
# 			break
# 		print("do you use the atm press y/n ")
# 		c=input()
# 		if c=="y":
# 			print("SWIPE THE CARD")
# 		else:
# 			print("good bye")
# 			break
# else:
# 	print("wrong password")









########################################################################################################

# print("wel-come to punjab nation bank ")
# pin=input("enter your correct four digit password:")
# balance=10000
# if len(pin)==4:
# 	print("correct password")
# 	b=1
# 	while b==1:
# 		choice=int(input('''please choose an option: 
# 			1-withdraw,
# 			2-deposit,
# 			3-check balance, 
# 			4-exit:'''))
# 		if choice==1:
# 			withdraw=float(input('''select your amount:-
# 				1 withdraw 500,
# 				2 withdraw 1000,
# 				3 withdraw 1500,
# 				4 withdraw 2000,or
# 				(enter your amount)'''))
# 			if withdraw==1:
# 				balance=balance-500
# 				print("successfull withdraw 500 ")
# 				print("current balance:$",balance)
# 			elif withdraw==2:
# 				balance=balance-1000
# 				print("successfull withdraw 1000 ")
# 				print("current balance:$",balance)
# 			elif withdraw==3:
# 				balance=balance-1500
# 				print("successfull withdraw 1500 ")
# 				print("current balance:$",balance)
# 			elif withdraw==4:
# 				balance=balance-2000
# 				print("successfull withdraw 2000 ")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance-withdraw
# 				print("successfull withdraw",withdraw)
# 				print("current balance:$",balance)
# 		elif choice==2:
# 			deposit=float(input('''select your amount:-
# 				1 deposit 500,
# 				2 deposit 1000,
# 				3 deposit 1500,
# 				4 deposit 2000,or
# 				(enter your amount)'''))
# 			if deposit==1:
# 				balance=balance+500
# 				print("successfull deposit 500")
# 				print("current balance:$",balance)
# 			elif deposit==2:
# 				balance=balance+1000
# 				print("successfull deposit 1000 ")
# 				print("current balance:$",balance)
# 			elif deposit==3:
# 				balance=balance+1500
# 				print("successfull deposit 1500 ")
# 				print("current balance:$",balance)
# 			elif deposit==4:
# 				balance=balance+2000
# 				print("successfull deposit 2000 ")
# 				print("current balance:$",balance)
# 			else:
# 				balance=balance+deposit
# 				print("successfull deposit",deposit)
# 				print("current balance:$",balance)
# 		elif choice==3:
# 			print(balance)
# 		elif choice==4:
# 			print("good bye")
# 			break
# 		print("do you use the atm press y/n ")
# 		c=input()
# 		if c=="y":
# 			print("SWIPE THE CARD")
# 		else:
# 			print("good bye")
# 			break
# else:
# 	print("wrong password")



#num=[17,59,18,19,20,1,2,4,56,76,7,5,46,36,56,89,98,8,890,8,9]
#prime=[]
#even=[]
#odd=[]
#for i in range(2,len(num)):
#    if num[i]>1 and i in num:
#        for j in range(2,i):
#            if i%j==0:
#                break
#        else:
#            prime.append(i)
#for i in num:
#    if i%2==0:
#        even.append(i)
#    else:
#        odd.append(i)
#print(prime)
#print(even)
#print(odd)
#
#
##############################################################

#num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#prime=[]
#odd=[]
#even=[]
#a=1
#while a<len(num):
#    if num[a]%2==0:
#        even.append(num[a])
#    else:
#        odd.append(num[a])
#        if num[a]>1:
#            if(num[a]%3!=0 and num[a]%5!=0 and num[a]%7!=0):
#                prime.append(num[a])
#    if num[a]==2 or num[a]==3 or num[a]==5 or num[a]==7:
#        prime.append(num[a])
#
#        
#    a+=1
#    
#print(prime,"prime")
#print(odd,"odd")
#print(even,"even")
####################################################################################################

#num=[45,67,89,1,2,
#3,4,5,6,7,8,9,10,11,12,45,7,9,89,55,13,14,15,16,17,18,19,20]
#prime=[]
#odd=[]
#even=[]
#a=1
#while a<len(num):
#    if num[a]%2==0:
#        even.append(num[a])
#    else:
#        odd.append(num[a])
#    a+=1
#for i in num:
#    for j in range(2,i):
#        if i%j==0:
#            break
#    else:
#        if i==1:
#            continue
#        prime.append(i)    
#print(prime,"prime")
#print(odd,"odd")
#print(even,"even")
#############################################################  maxxxx     maxxxxx  


#a=[1,105,90,7,6,54,100,2,3,4,5,95,6]
#d=a[0]
#for i in a:
#    if i>d:
#        d=i
#print(d)
############################################################  MINIMUM  #############

#a=[1,105,90,7,6,54,100,2,3,4,5,95,6]
#d=a[0]
#for i in a:
#    if i<d:
#        d=i
#print(d)






####################################################  second max    ############3
#num=[200,10,80,90,105,10000,7,6,1000,500,54,100,2,3,4,5,95,6]
#total=num[2:]
#if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
#else:
#    s=num[1]
#    s1=num[0]
#for i in total:
#    if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#print(s1)
#    
#




#############################################  second max    ############3
#num=[200,10,80,90,105,10000,7,6,1000,500,54,100,2,3,4,5,95,6]
#total=num[2:]
#if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
#else:
#    s=num[1]
#    s1=num[0]
#for i in total:
 #    if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#print(s1)
#    
###############################################################odddd    eveeen   prrimeeee


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

###################################################################################   length


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


###########################################################################

# a=0
# i=10
# while i>0:
#     print("enter numbeer")
#     b=int(input())
#     a=a+b
#     i=i-1
# print("average is",a/1)

#######################################################333    reverse     reverse  


#pl=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
#a=1
#rev_rse=[]
#for i in(pl):
#    rev_rse.append(pl[-a])
#    a+=1
#print(rev_rse)
################################################################    palindrome   


#x=["n","subh","i","t","i","hh","n"]
#y=[]
#a=1
#for i in x:
#    if x[-a]==i:
#        y.append(x[-a])
#    a+=1
#if x==y:
#    print("palindrome")
#else:
#    print("not palindrome")        
#####################################################################
# x=["n","k","t","i","n"]
#y=[]
# for i in range(len(x)):
#     if x[i]==x[-i-1]:
#         y.append(x[i])
# if x==y:
#     print('this is palindrome')
# else:
#     print('this is not a palindrome')

##########################################################################

#x=["n","k","t","i","n"]
#y=[]
#a=0
#while a<len(x):
#    if x[a]==x[-a-1]:
#        y.append(x[a])
#    a+=1
#if x==y:
#    print(" this is palindrome")
#else:
#    print("this is not palindrome")
#

###############################################################################################3  STRONG  PASSWORD 


#pas=input("enter password")
#if len(pas)>8 and len(pas)<16:
#    if ("A"in pas or"B" in pas or"C" in pas or"D" in pas or"E"in pas or"F" in pas or"H" in pas or "I"in pas  or "J"in pas or "K"in pas or "L"in pas or "M"in pas or "N"in pas or "O"in pas or "P"in pas or "Q"in pas or "R"in pas or "S"in pas or "T"in pas or "U"in pas or "V"in pas or "W"in pas or "X"in pas or "Y"in pas  or "Z"in pas):
#        if ("a"in pas or"b"in pas or"c"in pas or"d"in pas or"e"in pas or"f"in pas or "g"in pas or"h"in pas or"i"in pas or"j"in pas or"k"in pas or"l"in pas or"m"in pas or"n"in pas or"o"in pas or"p"in pas or"q"in pas or"r"in pas or"s"in pas or"t"in pas or"u"in pas or"v"in pas or"w"in pas in pas or"x"in pas or"y"in pas or"z"in pas):
#            if "@"in pas  or "#"in pas or "$"in pas  or "!"in pas:
#                if ("1"in pas  or "2"in pas  or "3"in pas  or "4"in pas  or "5"in pas  or "6"in pas  or "7"in pas  or "8"in pas or"9"in pas or"0"in pas):
#                    print("correct password")
#                else:
#                    print("enter number")
#            else:
#                print("not special character")
#        else:
#            print("small")           
#    else:
#        print("capital")
#else:
#    print("enter 8 to 16 character")
#
##############################################################################  list compare 


#list1 = [1,2,3,4,5,6]
#list2 = [2,3,1,0,6,7] 
#a=0
#for i in list1:
#    if i in list2:
#        continue
#    else:
#        print(i)
#
#
###################################################################   hangman game @##################



#hangman=1,2,3,4,5,6,7
#print("wel-come")
#name=input("what is yourname")
#print("hello,"+name,"time to lay hangman")
#word=["subhash","abhishek","pawan","tushar","ajay","atul","sanjay"]
#guesses=("")
#while True:
#    a=1
#    t=7
#    while t>0:
#        b=0
#        for i in word:
#            if i in guesses:
#                print(i)
#            else:
#                print("________")
#                b=+1
#        if b==0:
#            print("you won")
#            break
#        guess=input("guess the character")
#        guesses+=guess
#        if guess not in word:
#            t-=1
#            print(hangman[-a])
#            a+=1
#            print("you have",+t,"more guess")
#            if t==0:
#                print("you are lose")
#    print("do you want play: y/n")
#    again=input()
#    if again=="y":
#        print("thank you")
#        guesses="0"
#        
#    else:
#        print("good bye")
#        break   
########################################################


#hangman= ['''
#  +---+
#  |   |
#      |
#      |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
#      |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
#  |   |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|   |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
#      |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
# /    |
#      |
#=========''', '''
#  +---+
#  |   |
#  O   |
# /|\  |
# / \  |
#      |
#=========''']
#print("wel-come")
#name=input("what is yourname\n")
#print("hello,"+name,"time to lay hangman")
#word=["subhash","abhishek","pawan","navid","ajay","atul","sanjay"]
#guesses=("")
#while True:
#    a=1
#    t=7
#    while t>0:
#        b=0
#        for i in word:
#            if i in guesses:
#                print(i)
#            else:
#                print("________")
#                b=+1
#        if b==0:
#            print("you won")
#            break
#        guess=input("guess the character\n")
#        if guess in guesses:
#            print("already use this word")
#        guesses+=guess
#        if guess not in word:
#            t-=1
#            print(hangman[-a])
#            a+=1
#            print("you have",+t,"more guess")
#            print("do you help me: yes/no")
#            help=input()
#            if help=="yes":
#                for i in range(1):
#                    print("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
#                    helpp=input("you have 3 chance")
#                    if helpp=="1":
#                        print("*ajay*")
#                    elif helpp=="2":
#                        print("*pawan*")
#                    elif helpp=="3":
#                        print("*abhishek*")
#            elif help== "no":
#                print("ok")
#            
#                
#            if t==0:
#                print("you are lose")
#    print("do you want play: y/n")
#    again=input()
#    if again=="y":
#        print("thank you")
#        guesses="0"
#        
#    else:
#        print("good bye")
#        break   
#

##################################################################3


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

#################################################3  bubble  shorting    

#a=[5,1,4,2,8]
#for i in range(len(a)-1,0,-1):
#    for j in range(i):
#        if a[j]>a[j+1]:
#            b=a[j]
#            a[j]=a[j+1]
#            a[j+1]=b
#print(a)
#
#
#######################################################
#######################################banary   banary  

###################################################
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


#######################################banary   banary  
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

    
###########################################################  minimum sec minimum  --max   second max

#ntotal=num[2:]
#x=[]
#if num[0]>num[1]:
#   s=num[0]
#   s1=num[1]
#else:
#   sum=[1,200,10,80,90,105,10000,7,6,1000,500,54,100,3,4,5,95,6]
#=num[1]
#   s1=num[0]
#for i in total:
#    if i>s1:
#       if i>s:
#           s1=s
#           s=i
#       else:
#           s1=i
#    if num[0]<num[1]:
#        men=num[0]
#        secm=num[1]
#    else:
#        men=num[1]
#        secm=num[0]
#    for i in total:
#        if i<secm:
#            if i<men:
#                secm=men
#                men=i
#            else:
#                secm=i
#x.append(men)
#x.append(secm)
#x.append(s)
#x.append(s1)
#print(men,"minimum")
#print(secm,"sec minimum")
#print(x)
#print(s,"maximum")
#print(s1,"second maximum")

##########################################################  nested list  mgic squar 

#summ=0
#x=[]
#a=[
#    [4,8,3],
#    [8,3,4],
#    [3,4,8],
#]
#for i in a:
#    for j in range(len(a)):
#        ss=(i[j])
#        summ+=ss
#        x.append(ss)
#print(summ)        
#print(x)
#
###############################################################################   magic squar nested list summ

#summ=0
#x=[]
#a=[
#    [4,8,3],
#    [74,65,63,5],
#    [12,55,88,5,3],
#]
#for i in a:
#    for j in range (len(i)):
#        summ+=(i[j])
#        if j==(len(i)-1):
#            x.append(summ)
#            summ=0
#print(summ)
#print(x)

##################################
################################################ nested list to flat list and sum    
#summ=0
#x=[]
#a=[[4,5,6],[8,68,9],[555]]
#for i in a:
#    for j in range(len(i)):
#        ss=(i[j])
#        summ+=ss
#        x.append(ss)
#print(summ)        
#print(x)
###################################################  list sum and average nested list 

#summ=0
#x=[]
#y=[]
#count=0
#a=[[4,5,6],[8,68,9],[555]]
#for i in a:
#   for j in range(len(i)):
#       ss=(i[j])
#       summ+=ss
#       y.append(ss)
#       count+=1
#       if j ==(len(i)-1):
#           x.append(summ)
#           print("average",summ/count)
#           count=0
#           summ=0
#        
#print(summ)        
#print(x)
#print(y)
############################################### nested list to sum and flat list

#summ=0
#x=[]
#y=[]
#a=[[4,5,6],[8,68,9],[555]]
#for i in a:
#    for j in range(len(i)):
#        ss=(i[j])
#        summ+=ss
#        y.append(ss)
#        if j ==(len(i)-1):
#            x.append(summ)
#            summ=0
#print(summ)        
#print(x)
#print(y)
############################################################   flat list average s
    # summ=0
    # x=[]
    # count=0
    # a=[[4,5,6],[8,68,9],[555]]
    # for i in a:
    #    for j in range(len(i)):
    #        ss=(i[j])
    #        summ+=ss
    #        x.append(ss)
    #        count+=1
    # print(summ,"average",summ/count)
    # print(x)








##################################################################  magic square 
#pumm,tumm,humm,aa,summ,kumm,numm=0,0,0,0,0,0,0
#x=[]
#a=[
#    [1,1,1],
#    [1,1,1],
#    [1,1,1],
#]
#n=0
#u=2
#for i in a:
#    for ll in range(1):
#        numm+=i[aa]
#    for kk in range(1):
#        kumm+=i[1]
#    for hh in range(1):
#        humm+=i[2]
#    for dd in range(1):
#        tumm+=i[n]
#    n+=1
#    for oo in range(1):
#        pumm+=i[u]
#    u-=1
#    for j in range (len(i)):
#        summ+=(i[j])
#        if j==(len(i)-1):
#            x.append(summ)
#            summ=0
#if numm==pumm == kumm == tumm == humm:
#    print("magic square")
#else:
#    print("not magic square")
#print(x,numm,kumm,humm,tumm,pumm)

########################################################3  palindrome substring 
# 
 
# maxLength = 1
# string = ("forgeeksskeegfor")
# start = 0
# length = len(string) 

# low = 0
# high = 0
# for i in range(1, length): 
# 	low = i - 1
# 	high = i 
# 	while low >= 0 and high < length and string[low] == string[high]: 
# 		if high - low + 1 > maxLength: 
# 			start = low 
# 			maxLength = high - low + 1
# 		low -= 1
# 		high += 1
# 	low = i - 1
# 	high = i + 1
# 	while low >= 0 and high < length and string[low] == string[high]: 
# 		if high - low + 1 > maxLength: 
# 			start = low 
# 			maxLength = high - low + 1
# 		low -= 1
# 		high += 1

# print ("Longest palindrome substring is:") 
# print (string[start:start + maxLength]) 


#####################################################                second  number 47 


#a=int(input( ))
#if ((a%1000)//10)==47:
#    print("yes")
#else:
#    print("no")
#
###########################################################  fibonocci series

#xx=[]
#n=int(input("enter number"))
#x=0
#y=1
#z=0
#while z<=n:
#    print(z)
#    xx.append(z)
#    x=y
#    y=z
#    z=x+y
#b=int(input())
#print(xx[b],"index")
#


###########################################################   chocklate 

#b=1
#a=int(input())
#while b<=a:
#    if b%3==0:
#        a+=1
#    print(b)
#    b+=1



############################################################33    enagram

#inp=input("enter str")
#inp2=input("enter str")
#list1=[]
#list2=[]
#x=0
#for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
#list1.sort()
#list2.sort()
#print(list1)
#print(list2)
#if list1 ==list2 and len(inp)==len(inp2):
#    print("enagram")
#else:
#    print("no enagram")

#################################################################   without sort  enagram
#inp=input("enter str")
#inp2=input("enter str")
#list1=[]
#list2=[]
#x=0
#for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
#    for j in range(len(list1)-1):
#        for k in range(len(list1)-1):
#            if list1[k]>list1[k+1]:
#                n=list1[k]
#                list1[k]=list1[k+1]
#                list1[k+1]=n
#            if list2[k]>list2[k+1]:
#                n=list2[k]
#                list2[k]=list2[k+1]
#                list2[k+1]=n
#print(list1)
#print(list2)
#if list1 ==list2 and len(inp)==(inp2):
#    print("enagram")
#else:
#    print("no enagram")
#

###################################################################################3 enagram  


#inp=input("enter str")
#inp2=input("enter str")
#list1=[]
#list2=[]
#x=0
#for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
#    for j in range(len(list1)-1):
#        for k in range(len(list1)-1):
#            if list1[k]>list1[k+1]:
#                n=list1[k]
#                list1[k]=list1[k+1]
#                list1[k+1]=n
#            if list2[k]>list2[k+1]:
#                n=list2[k]
#                list2[k]=list2[k+1]
#                list2[k+1]=n
#x=0
#count=0
#for n in list1:
#    for m in range(1):
#        if len(list1)==len(list2):
#            if list1[x] == list2[x]:
#                continue
#            else:
#                count+=1
#        else:
#            print("no length")
#            break
#    x+=1
#if count==0 and len(inp)==len(inp2):
#    print("enagram")
#else:
#    print("no enagram")
#
#
#
#
###################################################################################################################################
################## enagram      enagram     

#a=input()
#b=input()
#c=list(a)
#d=list(b)
#d.sort()
#print(d)
#c.sort()
#print(c)
#if d==c and len(a)==len(b):
#    print("yes")
#else:
#    print("no")
#

########################################################################################################3 target  

#nums = [1,15,17,9,15,13,26,4]
#target = 30
#l = []
#x = 1
#length = len(nums) - 1
#for i in nums: 
#    l.append(nums.index(i))
#    if (target - i) in nums[x:]:
#       l.append(length - nums[::-1].index(target - i))
#       break
#    else:
#       l = []
#       x = x + 1
#print(l)
#
#
#####################################################################3



#b=0
#a=[1,15,17,9,15,13]
#total=[]
#vv=0
#list1=[]
#x=1
#for i in range(len(a)):
#    for j in range(len(a)-1):
#        if a[i]+a[j+1]==30:
#            print(a[i],a[j+1])
#    
#            
#            total.append(a[i])
#print(total)
#
#
############################################################ not univeral

# a=[1,15,17,9,15,13]
# for i in a:
#     for j in a:
#         if i+j==30:
#             print([i,j])
#             a.remove(i)
#             a.remove(j)

###############################################################  occurance 
#time=0
#z=[]
#list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
#a=1
#b=1
#for i in list1:
#    a=0
#    for j in list1:
#        if i==j and i not in z:
#            a+=1
#    if i not in z:  
#        z.append(i)
#        print(i,":",a)
#






#############################################################################################################33
###########################################33   3 sum three summm 


#a=[-1,0,1,2,-1,4]
#for i in a:
#    for j in a:
#        for k in a:
#            if i+j+k==0:
#                print([i,j,k])
#                
#                
#                a.remove(k)
#        a.remove(j)
#    a.remove(i)
#
#################################################################### modulus  %%%%%%%%%%%%

# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
# print(dividend)


#################################################     floor division       //  ///////  //

# count=0
# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
#     count+=1
# print(count)




##########################################333333333333############    oddd even kitne h 


#even=[]
#odd=[]
#counteven=0
#countodd=0
#elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
#for i in elements:
#    if i%2==0:
#        even.append(i)
#        counteven+=1
#    else:
#        odd.append(i)
#        countodd+=1
#print(counteven,"even",even)
#print(countodd,"odd",odd)
#


###################################################################################33   odd even sum


#even=[]
#odd=[]
#counteven=0
#countodd=0
#elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
#for i in elements:
#    if i%2==0:
#        even.append(i)
#        counteven+=i
#    else:
#        odd.append(i)
#        countodd+=1
#        countodd+=i
#print(counteven,"even",even)
#print(countodd,"odd",odd)
#
#############################################################################  odd even average two lis
#
#count=0
#count2=0
#even=[]
#odd=[]
#counteven=0
#countodd=0
#elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
#for i in elements:
#    if i%2==0:
#        even.append(i)
#        counteven+=i
#        count+=1
#    else:
#        odd.append(i)
#        countodd+=1
#        countodd+=i
#        count2+=1
#print("average",counteven/count,"even",even)
#print("average",countodd/count2,"odd",odd)


#########################################################################3    total sum odd even sum total average odd even average 


#cc=0
#count=0
#count2=0
#even=[]
#odd=[]
#counteven=0
#totalsum=0
#countodd=0
#elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
#for i in elements:
#    if i%2==0:
#        even.append(i)
#        counteven+=i
#        count+=1
#    else:
#        odd.append(i)
#        countodd+=i
#        count2+=1
#    totalsum+=i
#    cc+=1
#print(totalsum,"totalsum")
#print(totalsum/cc,"total average")
#print("average",counteven/count,"even",even)
#print(count,"count")
#print(counteven,"even sum")
#print("average",countodd/count2,"odd",odd)
#print(count2,"count2")
#print(countodd,"odd sum")
#
##########################################################################################33  coredpati  lakhpati  dilwale 


# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
# for i in kitna_paisa_hai:
#     if i>9999999 and i<999999999:
#         print(i,"coredpati")
#     elif i>99999 and i<9999999:
#         print(i,"lakhpati")
#     elif i>1 and i<99999:
#         print(i,"dilwale")












































































































































































