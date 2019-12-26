a=int(input("enter value : "))
b=int(input("enter value : "))

print("enter-1 : for addition")
print("enter-2 : for substraction")
print("enter-3 : for multiplication")
print("enter-4 : for devision")

ch=int(input("enter your choice  :"))

if ch==1:
    print("sum = :",(a+b))
elif ch==2:
    print("sub = :",(a-b))
elif ch==3:
    print("mul = :",(a*b))
elif ch==4:
    print("div = :",(a/b))
else:
    print("enter valid choice between 1 to 4  :")

