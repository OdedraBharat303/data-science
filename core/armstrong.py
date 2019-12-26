a=int(input("enter value "))
no=a
arm=0
while a>0:
    r=int(a%10)
    arm=arm+(r*r*r)
    a=a//10
print("arm",arm)
print("no",no)
if no==arm:
    print("armstrong")
else:
    print("not armstrong")
