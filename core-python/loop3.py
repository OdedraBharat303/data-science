a=int(input("enter value"))
i=1
esum=0
osum=0
ecount=0
ocount=0
while i<=a:
    if i%2==0:
        ecount=ecount+1
        print("even",i,end=",")
        esum=esum+i
        eavg=esum/ecount
    else:
        ocount=ocount+1
        print("odd",i,end=",")
        osum=osum+i
        oavg=osum/ocount
    i=i+1
print("even sum :",esum)
print("even count :",ecount)
print("even avg :=",eavg)
print("odd sum :",osum)
print("odd count :",ocount)
print("odd avg :=",oavg)

    


    
    
