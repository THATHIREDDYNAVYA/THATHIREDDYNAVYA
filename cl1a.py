a=[1,2]
b=[3,-6]
def dot(a,b):
    dp=0
    for i in range (0,len(a)):
        for j in range (0,len(b)):
            if i==j:
                dp = dp + a[i]*b[j]
    return dp
print(dot(a,b))
