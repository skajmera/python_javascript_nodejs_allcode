import json
from ak import signup
from sk import login
inp=int(input("1. login  2. signup"))
if inp==1:
    login()
elif inp==2:
    signup()
