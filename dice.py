#print opposite faces matches on dice 
# Input: n = 2
# Output: 5
# Explanation: For dice facing number 5 opposite face will have the number 2.

n= int(input("enter any phase: "))
#first method
if(n==1):
  print(6)
elif(n==2):
  print(5)
elif(n==3):
  print(4)  

#2nd method
print("2nd method")

for phase in range(1, n):
    if(n + phase == 7):  
      print("opposite phase of", n, "is", phase)
      
#3rd method

print(7-n)      