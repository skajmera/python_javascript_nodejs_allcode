# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# #  'id3': 
# #     {'name': ['Sara'], 
# #     'class': ['V'], 
# #     'subject_integration': ['english, math, science']
# #    },
# #  'id4': 
# #    {'name': ['Surya'], 
# #     'class': ['V'], 
# #     'subject_integration': ['english, math, science']
# #    },
# # }

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)


# import json
# a='{"s":1,"a":2}'
# print(a)
# print(type(a))
# a=json.loads(a)
# print(a)
# print(type(a))
# a=json.dumps(a)
# print(a)
# print(type(a))



# import json

# a={"lalalala": 3}
# mystring = json.dumps(a)
# print(mystring)


# Q.1 Json data ko python object main convert karne ka program likho?.
# import json
# a='{"Name":"Ram","Class":"IV", "Age":9 }'
# a=json.loads(a)
# print(a)



#Write a Python program to convert JSON data to Python object
# import json
# json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
# python_obj = json.loads(json_obj)
# print("\nJSON data:")
# print(python_obj)
# print("\nName: ",python_obj["Name"])
# print("Class: ",python_obj["Class"])
# print("Age: ",python_obj["Age"]) 


#Q.2 Python object ko json data main convert karne ka program likho?
# import json
# a={"name": "David",
#      "class":"I",
#      "age": 6  
#  }
# a=json.dumps(a)
# print(a)


#Q.3 Python object ko json string mai convert karne ka program likho?+
# import json
# a={"name":"subhsh",
#    "class":"high"}
# a=json.dumps(a)
# print(a)
#Write a Python program to convert Python object to JSON data.
# import json
# import json

# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# print(type(python_obj))
# file =open("subhash.json","w+")
# json.dump(python_obj,file)
# file.close()
# file = open('subhash.json',"r")
# s=json.load(file)
# file.close()
# print(s)
# 4

# Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
# import json
# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# print("Original String:")
# print(j_str)
# print("\nJSON data:")
# print(json.dumps(j_str, sort_keys=True,indent=4))


# import json

# with open('states.json') as f:
#   state_data= json.load(f)

# for state in state_data['states']:
#   del state['area_codes']

# with open('new_states.json', 'w') as f:
#   json.dump(state_data, f, indent=2)




# rishabh - meerut
# imtiyaz - delhi
# nilima - cochin
# rati - shimla
# ayishah - delhi
# raghu - shimla
# naseer - kanpur
# karthikeyan - delhi
# salma - jaipur
# pankaj - delhi
# brijesh - delhi
# govind - delhi
# puneet - shimla
# siddhi - delhi
# suman - jaipur
# rajeev - shimla
# mohinder - delhi
# rajendra - jaipur
# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - raipur
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - tokyo

# my_file = open("hdeepesh.txt",'w+')
# with open("hi.txt", "w+") as my_file:
#   
#   my_file.close()
# with open("hi.txt", "r") as my_file:
#   # my_file.write("deepesh - rangwani")
#   data = my_file.read()
#   print(data)
#   print(len(data))
#   my_file.close()

  
# my_file = open("hdeepesh.txt",'w+')
# file_data = my_file.read()
# print (file_data)
# my_file.close()


# import json

# a='{"name":"subhash"}'
# b=json.l
# print(b)


# import json

# dict1 =[
#   "emp1", {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#   },
#   "emp2", {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#   },
# ]

# f=open("subhash.json",'w')
# json.dump(dict1,f,indent=4)
# f.close()





# my_file = open("people.txt",'a')
# my_file.write("rishabh - meerut\nimtiyaz - delhi\nnilima - cochin\nrati - shimla\nayishah - delhi\nraghu - shimla\npankaj - delhi")
# my_file.write("\nsk-ajmera")
# my_file.close()
# my_file = open("people.txt",'r')
# p=my_file.()
# print(p)



# 1. Write a Python program to read an entire text file.
# def file_read(fname):
#         txt = open(fname)
#         print(txt.read())

# file_read('people.txt')


#2. Write a Python program to read first n lines of a file. 
# a=open("people.txt",'r')
# print(a.readlines(2))



#3. Write a Python program to append text to a file and display the text
# myfile=open("abc.txt","a")
# myfile.write("Python Exercises\n")
# myfile.write("Java Exercises")
# txt = open("abc.txt",'r')
# print(txt.read())

#Write a Python program to read a file line by line and store it into a list.
# f=open("abc.txt",'r') 
# content_list = f.readlines()
# print(content_list)


# Write a Python program to read a file line by line store it into a variable.
# def file_read(fname):
#         with open (fname, "r") as myfile:
#                 data=myfile.readlines()
#                 print(data)
# file_read('abc.txt')



# Write a Python program to assess if a file is closed or not.
# f = open('abc.txt','r')
# print(f.closed)
# f.close()
# print(f.closed)

# def lis(a):
#       txt=open("file-question3.txt",'w')
#       for i in a:
#             txt.writelines(i)
#             txt.write("\n")
# a=["adfsd","dsf","j","t"]
# lis(a)
# import json
# # a={"1":1,"2":2}
# txt=open("riyaz.json","r")
# # k=json.dump(a,txt)5-=56776
# k=json.load(txt)
# print(k)




# a={"name":"ajmera","age":22}
# import json
# txt=open("parmiya.json",'r')
# print(json.load(txt))
# txt.close()


# txt=open("parmeshwar.json",'r')
# print(txt.read())
# txt.close()


# s="subhash-ajmera\n"
# b="tushaar-freind"
# si=open("sig.txt",'w')
# si.write(s)
# si.write(b)
# si.close()
# si=open("sig.txt",'r')
# print(si.read())
# si.close()
# a={"name":"inp1","age":"inp2"}
# m=open("new.txt",'w')
# m.write(a)
# m.close()
# m=open("new.txt",'r')
# print(m.read())
# m.close()




# import json
# inp=input('''1. log in page
#            2. sign up page''')
# if inp=="2":
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=input("password")
#     dict1={"name":name,"gmail":gmail,"age":age,"password":password}
#     txt=open("dict1.json",'w')
#     json.dump(dict1,txt)
#     txt.close()
# else:
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=("password")
#     txt=open("dict1.json",'w')
#     if name==txt:
#         if gmail==txt:
#             if age==txt:
#                 if password==txt:
#                     print("successful")
#                     txt.close() 

# import json
# inp=input('''1. log in page
# 2. sign up page''')
# if inp=="2":
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=input("password")
#     dict2={"name":name,"gmail":gmail,"age":age,"password":password}
#     txt=open("dict2.json",'a')
#     json.dump(dict2,txt)
#     txt.close()
# else:
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=input("password")
#     txt=open("dict2.json",'r')
#     x=txt.read()
#     if name in x:
#         if gmail in x:
#             if age in x:
#                 if password in x:
#                     print("successful")
#                     txt.close()
#                 else:
#                     print("password wrong")
#             else:
#                 print("age not correct")
#         else:
#             print("gmail id not match")
#     else:
#         print("name is not define")
       
       
# import json
# inp=input('''1. log in page
# 2. sign up page''')
# if inp=="2":
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=input("password")
#     dict2={"name":name,"gmail":gmail,"age":age,"password":password}
#     txt=open("dict2.json",'a')
#     json.dump(dict2,txt)
#     txt.close()
# else:
#     name=input("name")
#     gmail=input("gmail")
#     age=input("age")
#     password=input("password")
#     txt=open("dict2.json",'r')
#     x=txt.read()
#     if name in x:
#         if gmail in x:
#             if age in x:
#                 if password in x:
#                     print("successful")
#                     txt.close()
#                 else:
#                     print("password wrong")
#             else:
#                 print("age not correct")
#         else:
#             print("gmail id not match")
#     else:
#         print("name is not define")


# import requests
# from bs4 import BeautifulSoup
# url="https://codewithharry.com"

# import json
# import json
# def aa(inp):
#     if inp=="2":
#         name=input("name")
#         gmail=input("gmail")
#         age=input("age")
#         password=input("password")
#         txt=open("dict11.json",'a')
#         dic={"name":name,"gmail":gmail,"age":age,"password":password}
#         json.dump(dic,txt)
#         txt.close()
# inp=input('''1. log in page             
# 2. sign up page''')
# aa(inp)


# import json
# from ak import*
# from sk import*
# inp=input("1. login  2. signup")
# aa(inp)
# login(inp)









