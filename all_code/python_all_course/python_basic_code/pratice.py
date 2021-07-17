# a=int(input())
# b=0
# c=1
# while a>0:
#     d=a%10
#     b=b+d
#     c=c*d
#     a=a//10
# if b==c:
#     print("sipce number")
# else:
#     print("not spice number")

# a=int(input())
# b=((a+1)//2*a)
# print(b)

# def str_implement(a,b):
#     c=0
#     for i in a:
#         for j in b:
#             if i==j:
#                 c=len(b)
#         if b not in a:
#             print(-1)
#             break 
#     print(c)
# x=input()
# y=input()
# str_implement(x,y)


# def str_implement(a,b):
#     for i in a:
#         if b not in a:
#             print(-1)
#             break
#     else:
#         print(len(b))
# x=input()
# y=input()
# str_implement(x,y)


# def tri_patten(a):
#     i=1
#     c=0
#     s=" "
#     while i!=a+1:
#         c+=i
#         t=str(c)
#         s=s+" "+t
#         i+=1
#     print(s)
# x=int(input("enter your number: "))
# tri_patten(x)

# def indexing(a,target):
#     for i in range (len(a)):
#         if a[i]==target:
#             print(a.index(target))
#             break
#         else:
#             a.insert(i,target)
#             a.sort()
#             print(a.index(target))
#             break
# list1=[4,6,7,8,9,10]
# target=int(input())
# indexing(list1,target)


# def target_indexing(a,target):
#     l=len(a)
#     i=0
#     while i!=l:
#         if a[i]==target:
#             a.append(target)
#             break
#         else:
#             a.append(target)
#             a.sort()
#             print(a.index(target))
#             break
# list1=[4,6,7,8,9,10]
# target=int(input())
# target_indexing(list1,target)


# num=int(input("enter your num:"))
# n=num//2
# b=1
# while b<=n:
#     print((" "*(n-b)+"* "*b)+("  "*(n-b)+"* "*b))
#     b+=1

# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)

# def twopowers(number):
#     if number==1:
#         return 1
#     return 2 * twopowers(number-1)

# index=1
# while(index<10):
#     print(twopowers(index))
#     index+=1



# def pattern(number):
#     if number == 1:
#         return 1
#     else:
#         return pattern(number-1) + 3 
    
# index=1
# while(index<10):
#     print(pattern(index),end=",")
# #     index+=1

# def pattern(number):
#     if number == 1:
#         return 10
#     elif number % 2 == 0:
#         return pattern(number - 1) + 1
#     else:
#         return pattern(number - 1) * 10
# index=1
# while(index<10):
#     print(pattern(index),end=",")
#    


# def operate(num1, operator, num2):
#     if operator=='+':
#         return num1 + num2
#     elif operator=='-':
#         return num1 - num2
#     elif operator=='*':
#         return num1 * num2
#     else:
#         return num1 / num2

# def solve(question_list):
#     if len(question_list)==1:
#         return int(question_list[0])
#     elif len(question_list)==3:
#         return operate(int(question_list[0]), question_list[1], int(question_list[2]))
#     else:
#         return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 

# print(solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3']))

 
# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)

# print (hcf(120, 100))


# def factorial(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac

#     pass
# num=int(input("enter your number:"))
# print(factorial(num))

# my_file = open("people1.txt","w")
# # file_data = my_file.read()
# # print (file_data)
# my_file.write("If your are thing your are bad and I am your dad \n")
# my_file.write("Abhishek - Gurgaon \n") 
# my_file.write("Ranveer - Delhi")
# my_file.close() 

# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("<html>\n")
# students_file.write("<head>\n")
# students_file.write("<title>NavGurukul Students</title>\n")
# students_file.write("</head>\n")
# students_file.write("<body>\n")
# students_file.write("<ul>")
# for student in batch1_students:
#     students_file.write("<li>" + student + "</li>\n")
# students_file.write("</ul>\n")
# students_file.write("</body>\n")
# students_file.write("</html>\n")
# students_file.close()


# ca={}
# def f(n):
#     if n in ca:
#         return ca[n]
#     if n==1:
#         value = 1
#     if n==2:
#         value = 1
#     elif n>2:
#         v = f(n-1)+f(n-2)
#     ca[n] = value
#     return value
# for i in range(1,100):
#     print(f(i))



a=[5,6,3,2,4,3]
b=0
for i in range(len(a)):
    try:
        if a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            continue
            print(a[i])
    except Exception as e:
        print(e)