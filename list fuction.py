# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # # del a[0:10]
# # # # print(a)
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # a.pop(5)
# # # print(a)
# #
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # print(a.pop(6))
# # # print(a)
# #
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # # print(a.pop(8))
# # # # print(a)
# # # #
# # # # a.pop(7)
# # # # print(a,"pop single  ")
# # # a.remove(40)#value delete krne k liye
# # # print(a)
# #
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # a.clear()
# # # print(a)
# #
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # a[6]=1000
# # # print(a)
# #
# # # a=[10,20,30,40,50,60,70,80,90,100]
# # # a.append(a)
# # # print(a)
# # #
# # a=[]
# # for b in range(2,21,+2):
# #
# #     print(b)
# # #
# # # # print("blank")
# # # # for c in range(1,16):
# # # #     a.append(c)
# # # # print(a)
# # # k=[i for i in range(1,107) if i%2==0]
# # # print(k)
# #
# # a=[10,20,30,40,50,60,70,80,90,100]
# # # del a[0:25]
# # # print(a)
# # #
# # # a.pop(6)
# # # print(a.pop(8))
# # # a.remove(70)
# # # a.clear()
# # a[0:5]=1000, 2000, 3000, 4000, 5000
# # print("update=",a)
# # list =["Gaurav", "Rahul","Meenu","Pooja","Mummy","Babu"]
# # new = [1000, 2000, 3000]
# # list [2:5] = new
# # print(list)
# #
# # a=[10,20,30,40,50,60,70]
# # a.insert(4,"lucky")
# # print(a)
# #
# # a=[10,20,30,40,50,60,70]
# # a.append("100lucky")
# # print(a)
# #
# # a=[10,20,30,40,50,60,70]
# # p=[1,2,3,4,"lucky",[100,200,300]]
# # c=[1000,2000,300]
# # a.append(p)
# #
# # a.append(c)
# #
# # print(a)
# #
# #
# # a=[10,20,30,40,50,60,70]
# # n=[80,90,"Rahul",'Lucky',[500,600]]
# # a.extend(n)
# # print(a)
# #
# # a=[10,20,30,10,40,10,50,1000,60,10,70]
# # b=a.count(10)
# # print(b)
# # m=max(a)
# # print(m)
# # min=min(a)
# # print(min)
# #
# #
# # a="lucky", "tinku", "meenu", "pooja"
# # print(max(a))
# #
# # a="lucky","Gaurav", "tinku", "meenu", "pooja"
# # # print(min(a))
# # min=min(a)
# # print(min)
# #
# # a=[10,20,2,9,25,30,6,8,1,3,9,10,40,10,50,1000,60,10,70]
# # j=sorted(a)
# # print(j)
# #
# # a.reverse()
# # print(a)
# #
# # b=["Hello", "world"]
# # b.reverse()
# # print(b)
# import distutils.command.upload
#
# # a=[10,20,30,40,50,60]
# # b=[50,60,70,80,90,100]
# # c=[1,2,3,4,5,6,]
# #
# # for d,e,f in zip(a,b,c):
# #     print(d,e,f)
#
# # a=input("enter value:")
# # print(a)
# #
# # b=a.split():
# #     print(b)
# # d={'name':'Gaurav',
# #    'Age': 35,
# #     'Address': 'M P colony'
# # }
# #
# # # print(d['Age'],d['name'])
#
# # h={'name':'rahul',
# #    'Age': 40,
# #    'Qualification':'MCA'
# #
# #    }
# # for l in h:
# # 	print(l,h[l])
#
# #
# # k={"name":"Rahul",
# #    "Age":50,
# #    "city":"Bikaner",
# #    "State":"Rajasthan"
# #
# # }
# # for p in k:
# #     print(p,k[p],type(k))
# #
# # print(k["name"],k["Age"],k["city"])
# #
# # print(k)
#
#
# h={"name": "Gaurav",
#    "Age":35,
#    "city":"Bikaner",
#    'Phone no':8233574700,
# }
#
# # print(h,type(h))
# # print(h["name"],h["Age"],h["city"],h["Phone no"])
#
# # for y in h:
# #     print(y,"=",h[y])
#
# # g=h.get('city')
# # print(g)
# #
# # for o in h.keys():
#     # print(o)
#
# # for u in h.values():
# #     print(u)
#
# # for a,b in h.items():
# #     print(a, b)
#
# # del h["Age"],h["city"]
# # print(h)
#
# # a=h.pop("name")
# # print(a, h)
#
# h.clear()
# print(h)

# h={"name": "Gaurav",
#    "Age":35,
#    "city":"Bikaner",
#    'Phone no':8233574700,
# }
# a=h.pop("name")
# print(a, h)
# h.clear()
# print(h)

t=(10,20,50,30,40,50,60,10,50,40,10,50)
# mi=min(t)
# print(mi)         # output 10
# ma=max(t)
# print(ma)         # output 60
# c=t.count(50)
# print(c)          # output 4
# s=sum(t,30)       #+30 will add default in sum value
# print(s)          # output 420 the add 30 more 450
# i=t.index(60)
# print(i)          # output 6 index value
# a=t[7]
# print(a)           # output 10 index value

# # for b in t:
# #    print(b)            # output iterate value 10,20,30,40,50,60,40
# b=len(t)
# print(b)                # output 12 length of tuple
# for f in range(b):
#     # print(f)               # f for index value
#     print(f,t[f])


# s={10,20,30,40,50}
# s.add(100)
# print(s)
# print(s.pop())
# print(s)
# s.remove(40)
# print(s)
# s.discard(30)
# print(s)
# s.clear()
# print(s)
s={10,20,30,40,50}
l=[40,50,60,70,80,90,100]
s.update(l)
# print(s)
#
# for b in s:
#     print(b)

p=len(s)
print(p)
for c in range(p):
    print(c)