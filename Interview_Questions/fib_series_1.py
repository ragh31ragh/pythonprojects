n=11
num1=0
num2=1
next_num=num2
count = 1
while (count<=n):
    print(num1,end=" ")
    num1,num2=num2,next_num
    next_num = num1+num2
    count = count +1

