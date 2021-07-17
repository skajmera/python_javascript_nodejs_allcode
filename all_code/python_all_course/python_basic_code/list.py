# ##########################################
# a=[5,1,4,2,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
# print(a)

#################################################

# a="suBHasH IS SImple BOy"
# count=0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if "S"in a[j]or "U"in a[j]or "B"in a[j]or "H"in a[j]or "A" in a[j]or "C"in a[j]or"D"in a[j]or"E"in a[j]or"F"in a[j]or"G"in a[j]or"H"in a[j]or"I"in a[j]or"J"in a[j]or"K"in a[j]or"L"in a[j]or"N"in a[j]or"O"in a[j]or"P"in a[j]or"Q"in a[j]or"R"in a[j]or"T"in a[j]or"V"in a[j]or"W"in a[j]or"X"in a[j]or"Y"in a[j]or"Z"in a[j]:
#             print(a[j],"capi")
#         else:
#             print(a[j])
    

    # print(b)

#############################################################


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
#####################################################################################################

# #############################################  second max  max minimum  ############3
# num=[200,10,80,90,105,10000,7,6,1000,1,500,54,100,2,3,4,5,95,6]
# total=num[2:]
# if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
# else:
#    s=num[1]
#    s1=num[0]
# for i in total:
#     if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#     mi=num[0]
#     for i in num:
#         if i<mi:
#             mi=i






#############################################  second max    ############3
# num=[1,200,10,80,90,105,10000,7,6,1000,500,54,100,3,4,5,95,6]
# total=num[2:]
# x=[]
# if num[0]>num[1]:
#    s=num[0]
#    s1=num[1]
# else:
#    s=num[1]
#    s1=num[0]
# for i in total:
#     if i>s1:
#        if i>s:
#            s1=s
#            s=i
#        else:
#            s1=i
#     if num[0]<num[1]:
#         men=num[0]
#         secm=num[1]
#     else:
#         men=num[1]
#         secm=num[0]
#     for i in total:
#         if i<secm:
#             if i<men:
#                 secm=men
#                 men=i
#             else:
#                 secm=i
# x.append(men)
# x.append(secm)
# x.append(s)
# x.append(s1)
# print(men,"minimum")
# print(secm,"sec minimum")
# print(x)
# #print(mi,"minimum")
# print(s,"maximum")
# print(s1,"second maximum")

########################################## magig squre nested  list 
# summ=0
# x=[]
# a=[
#     [56,8,5,],
#     [65,8,6,9],
#     [96,36,55,66,55],
# ]
# for i in a:
#     for j in range(len(a)):
#         ss=(i[j])
#         summ+=ss
#         x.append(ss)
# print(summ)        
# print(x)

# #####################################################  nested list sum 
# # numm=0
# kumm=0
# summ=0
# x=[]
# a=[
#     [4,8,3],
#     [74,65,63,5],
#     [12,55,88,5,3],
# ]
# for i in a:
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# print(summ)
# print(x)
            
#######################################

# numm=0
# kumm=0
# summ=0
# aa=0
# x=[]
# y=[]
# z=[]
# humm=0
# tumm=0
# pumm=0
# g=[]
# a=[
#     [1,1,1],
#     [1,1,1],
#     [1,1,1],
# ]
# n=0
# u=2
# for i in a:
#     for ll in range(1):
#         numm+=i[aa]
#     for kk in range(1):
#         kumm+=i[1]
#     for hh in range(1):
#         humm+=i[2]
#     for dd in range(1):
#         tumm+=i[n]
#     n+=1
#     for oo in range(1):
#         pumm+=i[u]
#     u-=1
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# if numm==pumm == kumm == tumm == humm:
#     print("magic square")
# else:
#     print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)
################################################ nested list to flat list and sum    
# summ=0
# x=[]
# y=[]
# a=[[4,5,6],[8,68,9],[555]]
# for i in a:
#     for j in range(len(i)):
#         ss=(i[j])
#         summ+=ss
#         y.append(ss)
#         if j ==(len(i)-1):
#             x.append(summ)
#             summ=0
# print(summ)        
# print(x)
# print(y)
##############################################3


# pumm,tumm,humm,aa,summ,kumm,numm=0,0,0,0,0,0,0
# x=[]
# a=[
#     [8,6,5],
#     [5,6,8],
#     [6,5,8],
# ]
# n=0
# u=2
# for i in a:
#     for l4l in range(1):
#         numm+=i[aa]
#     for kk in range(1):
#         kumm+=i[1]
#     for hh in range(1):
#         humm+=i[2]
#     for dd in range(1):
#         tumm+=i[n]
#     n+=1
#     for oo in range(1):
#         pumm+=i[u]
#     u-=1
#     for j in range (len(i)):
#         summ+=(i[j])
#         if j==(len(i)-1):
#             x.append(summ)
#             summ=0
# if numm==pumm == kumm == tumm == humm:
#     print("magic square")
# else:
#     print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)

#############################################################3


# i = 10
# a = []
# while i>0:
#   num = input()
#   a.append(num)
#   i = i-1
# # reverse elements of a
# a.reverse()
# #copied to new list
# b = a
# #again back to initial order
# a.reverse()
# print(a)


# count=1
# a=[0,1,1,0,0,0,1]
# for i in range(len(a)-1,0,-1):
#    for j in range(i):
#        if a[j]>a[j+1]:
#            b=a[j]
#            a[j]=a[j+1]
#            a[j+1]=b
#            count+=1
# print(a,count)


# s=["daadvaaa"]
# counter = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         temp = s[i:j]
#         if temp == temp[::-1]:
#             counter+=1
# print(temp)
# print(counter)

# def longestPalSubstr(string): 
# 	maxLength = 1

# 	start = 0
# 	length = len(string) 

# 	low = 0
# 	high = 0
# 	for i in range(1, length): 
# 		low = i - 1
# 		high = i 
# 		while low >= 0 and high < length and string[low] == string[high]: 
# 			if high - low + 1 > maxLength: 
# 				start = low 
# 				maxLength = high - low + 1
# 			low -= 1
# 			high += 1
# 		low = i - 1
# 		high = i + 1
# 		while low >= 0 and high < length and string[low] == string[high]: 
# 			if high - low + 1 > maxLength: 
# 				start = low 
# 				maxLength = high - low + 1
# 			low -= 1
# 			high += 1

# 	print ("Longest palindrome substring is:") 
# 	print (string[start:start + maxLength]) 

# 	return (maxLength) 
 
# string = ("forgeeksskeegfor")
# print ("Length is: " + str(longestPalSubstr(string))) 
##########################################################################
# This code is contributed by BHAVYA JAIN 


# a=[[1,2,3],[4,5,6]]
# i = 0
# while i<len(a):
#   j = 0
#   while j < len(a[i]):
#     print (a[i][j])
#     j = j+1
#   i = i+1



# a = [1,2,3,3,2,1,]
# i = 0
# mid = (len(a))/2
# same = True
# while i<mid:
#   if a[i] != a[len(a)-i-1]:
#     print ("No")
#     same = False
#     break
#   i = i+1
# if same == True:
#   print ("Yes")


# a = [1,2,3,2,1,3,12,12,32]
# i = 0
# while i < len(a):
#   j = i+1
#   while j < len(a):
#     if a[i] == a[j]:
#       del(a[j])
#     j=j+1
#   i = i+1
# print (a)

#python way
# a = [1,2,3,2,1,3,12,12,32]
# a = list(set(a))
# print (a)

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


########################################


# a=int(input( ))
# if ((a%1000)//10)==47:
#     print("yes")
# else:
#     print("no")
# b=1
# a=int(input())
# while b<=a:
#     if b%3==0:
#         a+=1
#     print(b)
#     b+=1
# b=0
# a=[1,15,17,9,15,13]
# total=[]
# for i in a:
#     for j in range(len(a)-1):
#         if a[b]+a[j+1]==30:
#             print(a[b])
#             total.append(a[j+1])
        

#     b+=1
# print(total)

# a=[1,15,17,9,15,13]
# total=[]
# b=0
# for i in a:
#     for j in range(len(a)-1):
#         if i+a[j+1]==30:
#             print(i)
#             total.append(a[j+1])
#             a.pop(i)
#     b+=1
# print(total)
# b=0
# a=[1,15,17,9,15,13]
# total=[]

# for i in range(len(a)):
#     for j in range(len(a)-1):
#         print(j)
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[j+1])

# print(total)

# nums = [1,15,17,9,15,13]
# target = 
# l = []
# x = 1
# length = len(nums) - 1
# for i in nums: 
#     l.append(nums.index(i))
#     if (target - i) in nums[x:]:
#        l.append(length - nums[::-1].index(target - i))
#        break
#     else:
#        l = []
#        x = x + 1
# print(l)


# nums = [1,15,17,9,15,13,26,4]
# target = 30
# l = []
# x = 1
# length = len(nums) - 1
# for i in nums: 
#     l.append(nums.index(i))
#     if (target - i) in nums[x:]:
#        l.append(length - nums[::-1].index(target - i))
#        break
#     else:
#        l = []
#        x = x + 1
# print(l)


# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[i])
# print(total)

# xx=[]
# n=int(input("enter number"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     xx.append(z)
#     x=y
#     y=z
#     z=x+y
# b=int(input())
# print(xx[b],"index")
# b=1
# a=int(input())
# while b<=a:
#     if b%3==0:
#         a+=1
#     print(b)
#     b+=1


##############################
# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i])
#             total.append(a[i])
# print(total)

# a="educatiohn"
# b="duecation"
# for i in a:
#     for j in range(len(a)-1):
#         if i in b:
#             print("yes")
#         else:
#             print("no")
#             break

############################################3

# a=input()
# b=input()
# c=list(a)
# d=list(b)
# d.sort()
# #print(d)
# c.sort()
# #print(c)
# if d==c and len(a)==len(b):
#     print("yes")
# else:
#     print("no")




# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# if list1==list2:
#     print("enagram")
# else:
#     print("no enagram")
# print(list1,list2)
        

# for i in range(len(list1)-1):
#     for j in range(len(list1)-1):
#         if list1[j]>list1[j+1]:
#             n=list1[j]
#             list1[j]=list1[j+1]
#             list1[j+1]=n
# print(list1)

# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# x=0
# count=0
# for n in list1:
#     for m in range(1):
#         if len(list1)==len(list2):
#             if list1[x] == list2[x]:
#                 continue
#             else:
#                 count+=1
#         else:
#             print("no length")
#             break
#     x+=1
# if count==0 and inp==inp2:
#     print("enagram")
# else:
#     print("no enagram")


# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
###########################################################################3
# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#     list1.append(i)
#     list2.append(inp2[x])
#     x+=1
#     for j in range(len(list1)-1):
#         for k in range(len(list1)-1):
#             if list1[k]>list1[k+1]:
#                 n=list1[k]
#                 list1[k]=list1[k+1]
#                 list1[k+1]=n
#             if list2[k]>list2[k+1]:
#                 n=list2[k]
#                 list2[k]=list2[k+1]
#                 list2[k+1]=n
# print(list1)
# print(list2)
# if list1 ==list2 and inp==inp2:
#     print("enagram")
# else:
#     print("no enagram")





##############################################3




# inp1=input()
# inp2=input()
# if len(inp1)<len(inp2):
#     for i in inp1:
#         if i in inp2:
#             print(i)
# elif len(inp1) == len(inp2):
#     for i in inp1:
#         if i in inp2:
#             print(i)
# else:
#     for i in inp2:
#         if i in inp1:
#             print(i)



# inp1=input()
# inp2=input()
# counter1=0
# for i in inp1:
#     if i in inp2:
#         counter1+=1
    
# if counter1 == len(inp2):
#     print("yes")
# else:
#     print('NO')

# b=0
# a=[1,15,17,9,15,13]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[i]+a[j+1]==30:
#             print(a[i],a[j+1])
#             # a.remove(a[i])
#             # a.remove(a[j+1])
#             total.append(a[i])
# #print(total)


# a="educatiohn"
# b="duecation"
# for i in a:
#     for j in range(len(a)-1):
#         if i in b:
#             print("yes")
#         else:
#             print("no")
#             break




# a=[1,15,17,9,15,13]
# for i in a:
#     for j in a:
#         if i+j==30:
#             print([i,j])
#             a.remove(i)
#             a.remove(j)


# a=[-1,0,1,2,-1,4]
# for i in a:
#     for j in a:
#         for k in a:
#             if i+j+k==0:
#                 print([i,j,k])
                
                
#                 a.remove(k)
#         a.remove(j)
#     a.remove(i)


# a=[-1,0,1,2,-1,4]
# for i in a:
#     for j in a:
#         for k in a:
#             print(i,j,k)
#             if i+j+k==0:
#                 #print([i,j,k])
                
                
#                 a.remove(k)
#         a.remove(j)
#     a.remove(i)

# quotint=0
# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
#     quotint+=1
# print(dividend)


# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
# print(dividend)



# count=0
# dividend=int(input())
# divisor=int(input())
# while(dividend>=divisor):
#     dividend-=divisor
#     count+=1
# print(count)

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



# summ=0
# x=[]
# y=[]
# count=0
# a=[[4,5,6],[8,68,9],[555]]
# for i in a:
#    for j in range(len(i)):
#        ss=(i[j])
#        summ+=ss
#        y.append(ss)
#        count+=1
#        if j ==(len(i)-1):
#            x.append(summ)
#            print("average",summ/count)
#            count=0
#            summ=0
        
# print(summ)        
# print(x)
# print(y)


# pumm,tumm,humm,aa,summ,kumm,numm=0,0,0,0,0,0,0
# x=[]
# a=[
#    [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# n=0
# u=2
# for i in a:
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
# if numm==pumm == kumm == tumm == humm:
#    print("magic square")
# else:
#    print("not magic square")
# print(x,numm,kumm,humm,tumm,pumm)
###################################################3

# a=1
# total=int(input())
# b=1
# while a<total:
#     b=1
#     while b<=10:
#         if a%b==0:
#             if b==10:
#                 print(a,"devide h")
#                 break
#         else:
#             break
#         b+=1
#     a=a+1

# even=[]
# odd=[]
# counteven=0
# countodd=0
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# for i in elements:
#     if i%2==0:
#         even.append(i)
#         counteven+=1
#     else:
#         odd.append(i)
#         countodd+=1
# print(counteven,"even",even)
# print(countodd,"odd",odd)


# cc=0
# count=0
# count2=0
# even=[]
# odd=[]
# counteven=0
# totalsum=0
# countodd=0
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# for i in elements:
#     if i%2==0:
#         even.append(i)
#         counteven+=i
#         count+=1
#     else:
#         odd.append(i)
#         countodd+=i
#         count2+=1
#     totalsum+=i
#     cc+=1
# print(totalsum,"totalsum")
# print(totalsum/cc,"total average")
# print("average",counteven/count,"even",even)
# print(count,"count")
# print(counteven,"even sum")
# print("average",countodd/count2,"odd",odd)
# print(count2,"count2")
# print(countodd,"odd sum")




# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
# for i in kitna_paisa_hai:
#     if i>9999999 and i<999999999:
#         print(i,"coredpati")
#     elif i>99999 and i<9999999:
#         print(i,"lakhpati")
#     elif i>1 and i<99999:
#         print(i,"dilwale")




# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
# for i in kitna_paisa_hai:
#     if i>9999999 and i<999999999:
#         print(i,"coredpati")
#     elif i>99999 and i<9999999:
#         print(i,"lakhpati")
#     elif i>1 and i<99999:
#         print(i,"dilwale")
# x=[]
# y=[]
# time=0
# z=[]
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 

# for i in list1:
#     d=list1.index(i)
#     for j in list1:
#         if i==j:
#             x.append(j)
#             c=list1.index(j)
#             list1.pop(c)s
# print(x)
# a=1
# b=1
# for i in list1:
#     a=0
#     for j in list1:
#         if i==j and i not in z:
#             a+=1
#     if i not in z:  
#         z.append(i)
#         print(i,":",a)
        


 # print(j)


#    for j in a:
#        for k in a:
#            if i+j+k==0:
#                print([i,j,k])
               
               
#                a.remove(k)
# for i in a:
#     if i<=0:
#         print(i)
    #    a.remove(j)
#    a.remove(i)//
# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
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
# print(list1)
# print(list2)
# if list1 ==list2 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")





# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
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
# x=0
# count=0
# for n in list1:
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
# if count==0 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")



# inp=input("enter str")
# inp2=input("enter str")
# list1=[]
# list2=[]
# x=0
# for i in inp:
#    list1.append(i)
#    list2.append(inp2[x])
#    x+=1
# list1.sort()
# list2.sort()
# print(list1)
# print(list2)
# if list1 ==list2 and len(inp)==len(inp2):
#    print("enagram")
# else:
#    print("no enagram")





# time=0
# z=[]
# list1 = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
# a=1
# b=1
# for i in list1:
#     a=0
#     for j in list1:
#         if i==j and i not in z:
#             a+=1
#     if i not in z:  
#         z.append(i)
#         print(i,":",a)
#######################################################3



# b=0
# a=[1,15,17,12,13,15]
# total=[]
# vv=0
# list1=[]
# x=1
# for i in a:
#    for j in         if i+j ==30 and i not in list1:
#            print(i,j)
#            total.append(i)
#     # if i not in list1:
#     #     list1.append(i)
# print(total)

# x=[]
# a=["hello","guys"]
# for i in a:
#     for j in range(1,len(i)+1):
#         x.append(i[-j])
# print(x)


# aa=int(input())
# i=0
# a=1
# n=0
# b=0
# while n<=aa:
#     n+=1
#     print(b)
#     i=a
#     a=b
#     b=i+a
# for i in range(1,26,):
#     if i%5==0:
#         print(i)

# counter=520
# a=1
# while a<=counter:
#     counter=520-500
#     print(a)
#     a+=1

# a=1
# sum=0
# count=0

# while a<=100:
#     if a%2==0:
#         print(sum,"even")
#         sum=sum+a
#     else:
#         count+=a
#     a+=1
    
# print(count,"odd")
  
print("suraj"*100,end=" ")



















