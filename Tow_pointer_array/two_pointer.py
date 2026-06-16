''' array [2,3,4,5,6,7,]  target is 7 find two sum  
print index '''

array =[2,3,4,5,6,7]
target =7

print(array)
left =0
right=len(array)-1

while left<right :
  sum = array[left] + array[right]
  
  if( sum == target ):
     print(left, right)
     break;
   
  elif (sum<target):
     left =left+1
     
  else: 
    right -=1

   


