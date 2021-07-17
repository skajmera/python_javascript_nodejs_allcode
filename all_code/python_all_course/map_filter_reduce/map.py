# Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

# Ready to take the test? Head onto LearnX and get your Python Certification!

# Map, Filter, Reduce
# Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.


# ########################  map reduce filter #####################3
# Map
# The map() function in python has the following syntax:

# map(func, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on. Notice the asterisk(*) on iterables? It means there can be as many iterables as possible, in so far func has that exact number as required input arguments. Before we move on to an example, it's important that you note the following:

# In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
# The number of arguments to func must be the number of iterables listed.
##########################################
# def myfunc(a):
#       return len(a)

# x = map(myfunc, ('apple', 'banana', 'cherry'))

# #convert the map into a list, for readability:
# print(list(x))


#//###################################################

# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1,2,3,4,5]

# results = dict(zip(my_strings, my_numbers))

# print(results)

#######################################  dictionary

# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1,2,3,4,5]

# results = dict(map(lambda x, y: (x, y), my_strings, my_numbers))

# print(results)


#####################################################


# numbers=["3","7","64"]
# numbers=(list(map(int,numbers)))
# numbers[2]=numbers[2]+1
# print(numbers)

############################################################
# def sq(b):
#     return b*b
# num=[2,3,4,55,2,6,5]
# squar=list(map(sq,num))
# print(squar)


###################################

# my=["subhash","ajmera"]
# py=list(map(str.upper,my))
# print(py)



##################################################

# num=[2,3,4,55,2,6,5]
# squar=list(map(lambda x: x*x,num))
# print(squar)


####################################################

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

# ############################################## filter
# Filter
# While map() passes each element in the iterable through a function and returns the result of all elements having passed through the function, filter(), first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function, "filtering" away those that are false. It has the following syntax:

# filter(func, iterable)

# The following points are to be noted regarding filter():

# Unlike map(), only one iterable is required.
# The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".
###################################################################3
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# def is_A_student(score):
#     return score > 75

# over_75 = list(filter(is_A_student, scores))

# print(over_75)

#########################################3  palindrom

# dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# palindromes = list(filter(lambda word: word == word[::-1], dromes))

# print(palindromes)

########################################################3

# list1=[1,5,6,9,8,7,5,6,65,98,56]
# def greater(num):
#     return num>5
# great=list(filter(greater,list1))
# print(great)



##########################

# list1=[1,5,6,9,8,7,5,6,65,98,56]
# def greater(num):
#     return num%2==0
# great=list(filter(greater,list1))
# print(great)  

#####################

# list1=[1,5,6,9,8,7,5,6,65,98,56]
# great=list(filter(lambda n:n%2==0,list1))
# print(great)


# ###################################################  reduce
# Reduce
# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument. It has the following syntax:

# reduce(func, iterable[, initial])
# Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the optional value that gets placed before the elements of the iterable in the calculation, and serves as a default when the iterable is empty. The following should be noted about reduce(): 1. func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and the second element in iterable. If initial is supplied, then it becomes the first argument to func and the first element in iterable becomes the second element. 2. reduce "reduces" (I know, forgive me) iterable into a single value.
###################################################################################
# from functools import reduce

# numbers = [3, 4, 6, 9]

# def custom_sum(first, second):
#     return first + second

# result = reduce(custom_sum, numbers, 10)
# print(result)


#################################################3
# from functools import reduce
# list1=[1,2,3,4]
# num=reduce(lambda x,y:x*y,list1)
# print(num)
############################################################




######################################################################
# from functools import reduce

# numbers = [3, 4, 6, 9, 34, 12]

# def custom_sum(first, second):
#     return first + second

# result = reduce(custom_sum, numbers)
# print(result)

##########################################333

# from functools import reduce 

# # Use map to print the square of each numbers rounded
# # to three decimal places
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# # Use filter to print only the names that are less than 
# # or equal to seven letters
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# # Use reduce to print the product of these numbers
# my_numbers = [4, 6, 9, 23, 5]

# # Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# filter_result = list(filter(lambda name: name, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

# print(map_result)
# print(filter_result)
# print(reduce_result)
###################################################

# from functools import reduce
 
# def do_sum(x1, x2): 
#     return x1 + x2

# print(reduce(do_sum, [1, 2, 3, 4]))


###########################################

# def do_sum(x1, x2): 
#     return x1 + x2

# def my_reduce(func, seq):
#     first = seq[0]
#     for i in seq[1:]:
#         first = func(first, i)
#     return first

# print(my_reduce(do_sum, [1, 2, 3, 4]))


##############################################################333
# import json
# g={
#         "movies": "Gol Maal",
#         "years": 1979,
#         "rating": 8.5,
#         "position": 2,
#         "link": "https://www.imdb.com/title/tt0079221/"
#     }
# f=open(r'/home/navgurukul/Desktop/tt0048473.json','w+')
# k=json.dump(g,f)
# # print(k)
# f=open(r'/home/navgurukul/Desktop/tt0048473.json','r')
# m=json.load(f)
# a=0
# while m!=None:
#     print(m[a])
#     a+=1

 
# a=[5,2,5]
# a.clear()
# print(a)

# a=[2,5,5,2,6]
# for i in range(len(a)):
#     a.remove(a[0])
# print(a)


# a=[2,5,5,2,6]
# for i in range(len(a)):
#     a.pop()
# print(a)
    
# a=[5,3,2,22,55,55]
# while len(a)>0:
#     a.pop()
# print(a)

    
# a=[5,3,2,22,55,55]
# while len(a)>0:
#     a.remove(a[0])
# print(a)



# a=[5,3,2,22,55,55]
# b=[]
# b=a.copy()
# c=0
# for i in b:
#     a.remove(i)
# print(a)


# a=[2,3,4,5,6]
# while a:
#     a.pop(-1)
# print(a)

####################################################   



# a=[5,2,5]
# a.clear()
# print(a)



# a=[2,5,5,2,6]
# for i in range(len(a)):
#     a.remove(a[0])
# print(a)


# a=[2,5,5,2,6]
# for i in range(len(a)):
#     a.pop()
# print(a)



    
# a=[5,3,2,22,55,55]
# while len(a)>0:
#     a.pop()
# print(a)

    
# a=[5,3,2,22,55,55]
# while len(a)>0:
#     a.remove(a[0])
# print(a)



# a=[5,3,2,22,55,55]
# b=[]
# b=a.copy()
# c=0
# for i in b:
#     a.pop()
# print(a)



# c=0
# a=[2,5,5,8,65,98]
# for i in a:
#     a.remove(i)
#     c+=1
#     a.remove(a[c])
#     c+=1
# print(a)
    


# a=[2,3,4,5,6]
# while a:
#     a.pop(-1)
# print(a)


# a=[2,5,5,8,65,98]
# del a[:len(a)]
# print(a)




# a=[2,3,4,2,3,4,2]
# for i in a:
#     b=1
#     for j in a:
#         if i==a[-b]:
#             a.remove(a[-b])
#         b+=1
# print(a)