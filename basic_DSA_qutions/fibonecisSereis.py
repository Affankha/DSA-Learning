# Fiboneces series    (sum of previous two elements is that some is third element, ex=n1,n2,n3,n4,n5....     n3=n1+n2, n4=n3+n2)


n1=0   #first number in a sereis
n2=1   #second number in a series

print(n1)
print(n2)

for i in range(10):     #i want to print fiboneces series upto 10
  n3=n1+n2
  print(n3)
  
  n1=n2
  n2=n3
  
  
  


#2nd method
print("2nd method")
n = 10
num1, num2 = 0, 1

print(f"Fibonacci Series: {num1}, {num2}", end="")

for i in range(2, n):
    num3 = num1 + num2
    print(f", {num3}", end="")
    num1, num2 = num2, num3
 
print()