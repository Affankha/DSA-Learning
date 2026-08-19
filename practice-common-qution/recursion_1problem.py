# print the numbers from 1 to n

def NumberPrint(n):
    if n==0:
      return
    result =n*(n+1)/2
    print(f"sum from {n} to {1}:", int(result))
    NumberPrint(n-1)    

NumberPrint(10)



# calculate power 2 3

num1 =2
num2 =5

print(2**5)  #simple method

              #using recursion

def CalculatePower(num1, num2):
    if num1 ==0:
      return 0
    elif num2==0:
      return 1
    print("The power is: ", num1**num2)
    CalculatePower(num1-1, num2-1)
    
CalculatePower(num1, num2)


# nth fibonacic number
def FibonecicNumber(n):
    if n==0:
      return
    d1=0;
    d2=1
    result =0
    result.append(d1)
    result.append(d2)
    
    print("fibonecic series are: ", list)
    
    FibonecicNumber(n-1)
FibonecicNumber(6)