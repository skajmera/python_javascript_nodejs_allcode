# import csv
# def write():
#     with open ("Data.csv","w") as f:
#         Rec=csv.writer(f,delimiter=',')
#         Rec.writerow(['TID','DESTINATION','DAYS','FARE'])
#         while True:
#             id=input("enter the id")
#             country=input("enter county")
#             code=int(input("enter the number of days"))
#             price=int(input("enter price"))
#             R=[id.upper(),country.upper(),code,price]
#             Rec.writerow(R)
#             ch=input("more data")
#             if ch=="n" or ch=="N":
#                 break
            
            
# def read():
#     with open ("Data.csv","r") as f:
#         Rec=csv.reader(f)
#         for i in Rec:
#             print(i)
            
            
# def search():
#     with open ("Data.csv","r") as f:
#         Rec=csv.reader(f)
#         next(Rec)
#         for i in Rec:
#             if int(i[3])>1000 and int(i[3])<2000:
#                 print(i)
# write()
# read()
# search()



import csv
fh=open('demo.csv','w')
s=csv.writer(fh,delimiter='*')
s.writerow(['roll no-','name','age'])
lis=[]
while True:
    print('enter your details0')
    r=int(input('enter  roll no-'))
    n=input('enter your name ')
    a=int(input('enter your age'))
    stru=[r,n,a]
    lis.append(stru)
    d=input('want to add something type y/n')
    if d=='n' or d=='N':
        break
for i in lis:
    s.writerow(i)
fh.close()