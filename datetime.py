# import random
# cn=random.randrange(1,50)
# userinput=int(input("enter no:"))
#
# if cn>userinput:
#     print(cn)
#     print("cn is gretaer than you no.")
#
# elif userinput>cn:
#     print(cn)
#     print("user input greter than cn no")
#
# else:
#     print("both no. are equal")
#

# x=int(input("enter no."))
# y=int(input("enter 2nd no.:"))
#
# if x>y:
#     print(x,"x greter than y", y)
#
# elif y>x:
#     print(y,"Y greater than x", x)
#
# else:
#     print(x,y,"both x and y equal")


#
# day=int(input("enter no. for day"))
#
# if day==1:
#     print("Sunday")
#
# elif day==2:
#     print("Monday")
#
# elif day==3:
#     print("Tuesday")
#
# elif day==4:
#     print("Wednesday")
#
# elif day==5:
#     print("Thursday")
#
# elif day==6:
#     print("Friday")
#
# elif day==7:
#     print("Saturday")
#
# else:
#     print("Wrong day")


m=int(input("enter no.:"))
n=int(input("enter no.:"))

# p=100
# k=5
h=int(input("enter choice no."))
if h==1:
    print("Plus=", m+n)

elif h==2:
    print("substraction=",m-n)

elif h==3:
    print("Divide=",m/n)

elif h==4:
    print("average =", (m+n)/2)

elif h==5:
    print("mulitply=",m*n)

else:
    print("all", m+n,m-n,m*n,m/n,(m+n)/2)
