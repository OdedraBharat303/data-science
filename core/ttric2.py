a=int(input("enter value "))
sum=0
for i in range (1,a):
    
    if a%i==0:
        sum=sum+i
        
if a==sum:
    
    print("prfct")
else:
    print("not perfect")
