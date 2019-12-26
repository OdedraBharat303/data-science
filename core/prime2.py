a=int(input("enter value"))
count=0
for i in range(1,a+1):
    if a%i==0:
        
        count=count+1
        print("count",count)
        c=count
        
    elif c>2:
        print("not prime")
else:
    print("prime")

        
