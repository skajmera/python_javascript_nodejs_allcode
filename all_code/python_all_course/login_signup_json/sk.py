import json
def login():
    print("wel-come my login page")
    gmail=input("gmail")
    password=input("password")
    txt=open("dict11.json",'r')
    x=txt.read()
    x=json.loads(x)
    txt.close()
    if gmail==x['gmail']:
        if password==x['password']:
            print("successful")   
        else:
            print("password wrong")
            print(x)
    else:
        print("gmail id not match")
        print(x)