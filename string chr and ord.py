w=115
print(type(w),chr(w))
y=ord('K')
print(type(y),y)

t="welcome {} to {} world".format("hello", "hi")
print(t)
t="welcome {1} to {0} world".format("hello", "hi")
print(t)
t="welcome {a:^10} to {b} world".format(a=50, b="hi")
print(t)