# def max_of_two( x, y ):
#     if x > y:
#         return x
#     else:
#         return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))

########################   Write a Python function to sum all the numbers in a list.

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))


######################################3  Write a Python function to multiply all the numbers in a list.

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((8, 2, 3, -1, 7)))
################################################Write a Python program to reverse a string.


# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))
###################################################################  factorial 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

################################# Write a Python function to check whether a number is in a given range.

# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)


####Write a Python function to check whether a number is in a given range.

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')


##Write a Python function that takes a list and returns a new list with unique elements of the first list
# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5])) 



#Write a Python function that takes a number as a parameter and check the number is prime or not.
# def test_prime(n):
# 	    if (n==1):
# 	        return False
# 	    elif (n==2):
# 	        return True;
# 	    else:
# 	        for x in range(2,n):
# 	            if(n % x==0):
# 	                return False
# 	        return True             
# print(test_prime(13))


#Write a Python program to print the even numbers from a given list. Go to the editor Sample List
# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

############################################   perfect number 
# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))


#Write a Python function that checks whether a passed string is palindrome or not. 

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza'))
# 
# ########################### 
# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(12)



# def pascal_triangle(n):
#     trow = [1]
#     y = [0]
#     for x in range(n):
#         print(trow)
#         trow=([l+r for l,r in zip(trow+y, y+trow)])
# pascal_triangle(10) 

########################################################

# import string, sys
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
 
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 

############################################3
#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))


#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)
# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l)
		
# printValues()

#Write a Python program to execute a string containing Python code.
# mycode = 'print("hello world")'
# code = """
# def mutiply(x,y):
#     return x*y

# print('Multiply of 2 and 3 is: ',mutiply(2,3))
# """
# exec(mycode)
# exec(code)

########################################3
# =
#  Write a Python program to access a function inside a function.
# def test(a):
#         def add(b):
#                 nonlocal a
#                 a += 1
#                 print(a+b)
#         add(4)
# test(4)



####################################3

#Write a Python program to detect the number of local variables declared in a function.
# def abc():
#     x = 1
#     y = 2
#     str1= "w3resource"
#     print("Python Exercises")

# print(abc.__code__.co_nlocals)
###################################################33
# def outerFun(a, b):
#     square = a**2
#     def innerFun(a,b):
#         return a+b
#     add = innerFun(a, b)
#     return add+square

# result = outerFun(5, 10)
# print(result)



#####################3


# def calculateSum(num):
#     if num:
#         return num + calculateSum(num-1)
#     else:
#         return 0

# res = calculateSum(10)
# print(res)
###################################3



# def displayStudent(name, age):
#     print(name, age)

# displayStudent("Emma", 26)

# showStudent = displayStudent
# showStudent("Emma", 26)

###############333


# print(tuple(range(3, 31, 3)))


##############################################    list  

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# resList = list(filter(None, list1))
# print(resList)

#########################################


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

#########################################33
# list1 = [5, 10, 15, 20, 25, 50, 20]

# index = list1.index(20)
# list1[index] = 200
# print(list1)





####################################3

# list1 = [5, 20, 15, 20, 25, 50, 20]

# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list1, 20)
# print(resList)

#################################3





# def appendMiddle(s1, s2):
#   middleIndex = int(len(s1) /2)
#   print("Original Strings are", s1, s2)
#   middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
#   print("After appending new string in middle", middleThree)
  
# appendMiddle("Ault", "Kelly")
























