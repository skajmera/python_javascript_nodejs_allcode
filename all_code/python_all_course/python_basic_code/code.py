# aa=add_numbers(20, 40)
# bb=add_numbers(560, 23)
# a = 1234
# b = 12
# cc=add_numbers(a, b)
# print(aa)
# print(bb)
# print(cc)
# dd=add_numbers(20, 40) / add_numbers(5, 1)
# print(dd)

###################################################################
# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4=add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4)) 
#################################################################

# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20) 
# print(sum6)

#########################################

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu) 
####################################################
# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
#     return food
#     print ("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday")) 




###############################################333333
# def calculate(num1,num2):
#     return num1+
# number1=calculate(5,6)
# print(number1)



# n1=float(input())
# opr=input()
# n2=float(input())
# if opr=="+":
#     print(n1+n2)
# elif opr=="-":
#     print(n1-n2)
# elif opr=="*":
#     print(n1*n2)
# else:
#     print(n1/n2)

################################################333
# def add(n1,n2):
#     return n1+n2
# def subtract(n1,n2):
#     return n1-n2
# def multiply(n1,n2):
#     return n1*n2
# def divide(n1,n2):
#     return n1/n2
# inp=float(input("number"))
# opr=input("operation")
# inp2=float(input("enter num."))
# v1=add(inp,inp2)
# v2=subtract(inp,inp2)
# v3=multiply(inp,inp2)
# v4=divide(inp,inp2)
# if opr=="+":
#     print(v1)
# elif opr=="-":
#     print(v2)
# elif opr=="*":
#     print(v3)
# else:
#     print(v4)

##################################################3

# def add(n1,n2):
#     return n1+n2
# def subtract(n1,n2):
#     return n1-n2
# def multiply(n1,n2):
#     return n1*n2
# def divide(n1,n2):
#     return n1/n2
# inp=float(input("number"))
# inp2=float(input("enter num."))
# add1=add(inp,inp2)
# substract1=subtract(inp,inp2)
# multiply1=multiply(inp,inp2)
# divide1=divide(inp,inp2)

#####################################
# def add(n1,n2):
#     print(n1+n2)
# def subtract(n1,n2):
#     print (n1-n2)
# def multiply(n1,n2):
#     print(n1*n2)
# def divide(n1,n2):
#     print(n1/n2)
# add(4,5)
# subtract(8,2)
# multiply1=multiply(4,5)
# divide(54,
# 6)



# def add(n1,n2):
#     return n1+n2
# def subtract(n1,n2):
#     return n1-n2
# def multiply(n1,n2):
#     return n1*n2
# def divide(n1,n2):
#     return n1/n2
#inp=float(input("number"))
#inp2=float(input("enter num."))
# add1=add(inp,inp2)
# substract1=subtract(inp,inp2)
# multiply1=multiply(inp,inp2)
# divide1=divide(inp,inp2)

##############################################

# new=[]
# def list1(l1,l2):
#     for i in range(len(l1)):
#         ss=(multiply(l1[i],l2[i]))
#         new.append(ss)
#     return new
# print(list1([5, 10, 50, 20], [2, 20, 3, 5]))

# ##########################################################





# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()

# f1() 

def fun(inp):
    if inp<70:
        print("ok")
    else:
        c=0
        while inp>70:
            if inp%5==0:
                c+=1

            inp-=1
    print(c)
    if c!=12:
        print("limit")
    else:
        print("susspend")

inp=int(input())
fun(inp)
        




# def fun(n):
#     key1=[]
#     value1=[]
#     for i in range(1,n+1):
#         b=i**2
#         key1.append(i)
#         value1.append(b)
#     a=dict(zip(key1,value1))
#     print(a)
# n=int(input())
# fun(n)

# def fun(n):
#     key1=[]
#     value1=[]
# a=[1,2,3,4,5]
# b={}
# for i in range(5):
#     b[i]=b[i]
#     print(b)
#     b=i**2
#     key1.append(i)
#     value1.append(b)
#     ict(key1,value1)
#     print(a)

# fun(10)
#  a=d
# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number//=10
#     return sum
# num=int(input())
# print(sumofdigits(num))


#################################333
# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)
#         else:
#             Print(far)
# distance(20,30)





# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")
###################################################3  logical test
# aas="  "
# inp=int(input())
# b=0
# for i in range(1,inp):
#     b=b+i
#     # aas.append(b)
#     aas=aas+ " " +str(b)
# print(aas)
# g=aas
# print(tuple(g))


#########################################################

# a=[100,155,66,3]
# a.sort()
# tar=int(input())
# rr=len(a)
# for i in range(len(a)):
#     for j in range (len(a)):
#         if a[i]==tar:
#             ss=a.index(a[i])
#         elif a[i]>tar:
#             a.insert(i,tar)
#             ss=a.index(a[i])
#         elif a[i]<tar:
#             a.insert(rr,tar)
#             ss=a.index(tar)
# print(ss) 

##########################################################
# a=input("enter")
# b=input("enter")
# count=0
# l1=[]
# dd=len(b)
# for i in a:
#     for j in b:
#         if i==j:
#             ll.append(i)
#             count+=1

# if count==dd:
#     print("true",count)
# else:
#     print("not",count)

# n=int(input())
# for row in range(n):
#     for col in  range(n+1):
#         if(row==0 and col%n/2!=0)or(row==(n+1)-n) and (col%n/2==0)or(row-col==n/2)or(row+col==n+2):
#             print("*",end="")
#         else:
#             print(end="")
#     print(n)







