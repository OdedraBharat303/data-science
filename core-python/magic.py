a=int(input("enter value "))
no=a
sum=0
rev=0

while a>0:
    
    r=a%10
    sum=sum+r  
    a=a//10
    
print("sum is :=",sum)
s=sum

while sum>0:
    
    m=sum%10
    rev=(rev*10)+m
    sum=sum//10
    
print("reverse number is:=",rev)
mul=s*rev
print("multiplication is :=",mul)

if mul==no:
    print("this is magic number")
else:
    print("this is not magic number")


    
