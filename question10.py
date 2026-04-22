num=int(input("Enter your 3-digit numbers : "))
a=num%10
num=num//10


b=num%10
num=num//10

c=num%10
num=num//10

sum=a+b+c
print("The sum of digits is ", sum)