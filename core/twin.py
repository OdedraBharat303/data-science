a=int(input("enter value "))
sum=0
num=1
while a>0:
    r=a%10
    sum=sum+r
    num=num*r
    a=a//10
print("sum",sum)
print("num",num)
if sum==num:
    print("twin")
else:
    print("not twin")
