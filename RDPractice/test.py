n=10
num1 = 0
num2 = 1
next_num = num2
count = 1
while (count <= n):
  count = count + 1
  print(next_num)
  num1,num2 = num2,next_num
  next_num = num1 + num2

