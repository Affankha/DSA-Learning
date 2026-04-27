# Simple Method
n =int(input("Enter NO: "))

if n%2 == 0:
  print(True)
else:
  print(False)

#  Using Funtion
def isEven(n):
    if n % 2 == 0:
       return True
       # print(True)
    else:
        return False
      # print(False)
      
print(isEven(12))


#Through Bitwise operator
# x ko binory me connvert karenga or 1 ke sath some karenga, Even ke last me 0 aata binory me odd ke last me 1 ata 
x=91
if (x & 1) ==0:
  print("True")
else: 
  print("False")


