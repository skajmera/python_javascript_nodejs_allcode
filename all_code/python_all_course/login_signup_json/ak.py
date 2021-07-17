import json
from sk import *
def signup():
    name=input("name")
    gmail=input("gmail")
    age=input("age")
    password=input("password")
    txt=open("dict11.json",'w')
    dic={"name":name,"gmail":gmail,"age":age,"password":password}
    json.dump(dic,txt)
    txt.close()
    login()
