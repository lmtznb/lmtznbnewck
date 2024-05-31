def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

num = 5
result = factorial(num)
print(f"the factorial of{num} is {result}")