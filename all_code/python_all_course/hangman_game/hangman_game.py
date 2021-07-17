
hangman= ['''
+---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''', '''
+---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
+---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
+---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
+---+
 |   |
 O   |
     |
     |
     |
=========''', '''
+---+
 |   |
     |
     |
     |
     |
=========''']
print("wel-come")
name=input("what is yourname\n")
print("hello,"+name,"time to lay hangman")
word="subhash"
guesses=("")
while True:
   a=1
   t=7
   while t>0:
       b=0
       for i in word:
           if i in guesses:
               print(i)
           else:
               print("________")
               b=+1
       if b==0:
           print("you won")
           break
       guess=input("guess the character\n")
       if guess in guesses:
           print("already use this word")
       guesses+=guess
       if guess not in word:
           t-=1
           print(hangman[-a])
           a+=1
           print("you have",+t,"more guess")
           print("do you help me: yes/no")
           help=input()
           if help=="yes":
               for i in range(1):
                   print("(1st chance press : 1), (2nd chance press: 2) and (3rd chance press: 3)")
                   helpp=input("you have 3 chance")
                   if helpp=="1":
                       print("*b*")
                   elif helpp=="2":
                       print("*h*")
                   elif helpp=="3":
                       print("*a*")
           elif help== "no":
               print("ok")
           
               
           if t==0:
               print("you are lose")
   print("do you want play: y/n")
   again=input()
   if again=="y":
       print("thank you")
       guesses="0"
       
   else:
       print("good bye")
       break   
