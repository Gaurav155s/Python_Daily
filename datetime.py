import random
cn=random.randrange(1,50)
userinput=int(input("enter no:"))

if cn>userinput:
    print(cn)
    print("cn is gretaer than you no.")

elif userinput>cn:
    print(cn)
    print("user input greter than cn no")

else:
    print("both no. are equal")

