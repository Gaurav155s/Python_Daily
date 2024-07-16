def reverse_string (s):
  reversed_string = ''

  for i in range(len(s) - 1, -1, -1):
    reversed_string += s[i]
  return reversed_string
  


print(reverse_string("hello"))
