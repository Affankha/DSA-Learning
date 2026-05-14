#check num is prime  (that no. should be divisible by "ownself" and by "one")


num =int(input("enter number: "))


for i in range(2, int(num**0.5)+1):
  if num % i ==0:
    print(num, "Is not a prime number");
    break;
  else:
    print(num, "IS a Prime number")
    break;
    
    
    
    
    
#2nd method  using math function
import math

#num already taking input

for i in range(2, int(math.sqrt(num))+1):
    if num % i ==0:
      print(num, "Is not a prime number");
      break
    else:
        print(num, "IS a Prime number")
