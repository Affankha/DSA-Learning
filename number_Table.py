# print the table a input number

n= int(input("enter any number: "))
table =[]

i=1
while i<=10:
  table.append(i*n)
  i+=1

for i in range(len(table)):
    print(table[i])



# 2nd method
print("2nd method")

i=1
while i<=10:
  print(i*n)
  i=i+1