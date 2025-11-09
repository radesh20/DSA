#Find GCD (HCF) of two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
print("GCD of",a,"and",b,"is",gcd(a,b))