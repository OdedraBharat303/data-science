a=int(input("enter value "))
no=a
rev=0
while a>0:
    r=a%10
    rev=(rev*10)+r
    a=a//10
print("rev",rev)
if no==rev:
    print("pelindrom")
else:
    print("not pelindrom")
