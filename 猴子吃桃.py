n = int(input())
def F(x):
    if x==1:
        return x
    else:
        return (F(x-1)+1)*2
print(F(n))