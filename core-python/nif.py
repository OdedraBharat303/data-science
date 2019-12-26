a=int(input("enter number :"))
b=int(input("enter number :"))
c=int(input("enter number :"))
d=int(input("enter number :"))

if a>b:
    if a>c:
         if a>d:
            print("a is max")
         else:
            print("d is max")
    elif c>d:
        print("c is max")
    else:
        print("d is max")
elif b>c:
    if b>d:
        print("b is max")
    else:
        print("d is max")

elif c>d:
    print("c is max")
else :
    print("d is max")
