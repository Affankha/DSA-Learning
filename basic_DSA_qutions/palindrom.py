#check the given string is palindrom (we can read string both side and it will same ex:madam, civic, racecar, level, kayak, radar, 121, 12321, 3553,    sentence= A man, a plan, a canal:panama,          2nd Sentence: Too hot to hoot)


x="level"
reverseX =x[::-1]

if(reverseX == x):
  print("it is palindrom")
else:
  print("is not Palindrom")  
  
print(reverseX)

print(x==x[::-1])  # ans in boolean formate