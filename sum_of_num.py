m=int(input("Enter starting number: "))
n=int(input("Enter end number: "))
sum=0
for i in range (m,n+1,1):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)