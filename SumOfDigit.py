a=int(input("Enter number"))
while a >= 10:
    a = sum(int(digit) for digit in str(a))
print(a)