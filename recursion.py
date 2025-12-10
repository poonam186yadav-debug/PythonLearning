def  factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("ENTER UR NUMBER: "))
print(f"factorial of this number is {factorial(n)}")