import math
n = input()
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p1=0
p2=0
p3=0
pi=0
for i in range(int(n)):
    p1 += abs(x[i]-y[i])
    p2 += abs(x[i]-y[i])**2
    p3 += abs(x[i]-y[i])**3
    if pi < abs(x[i]-y[i]):
        pi = abs(x[i]-y[i])
p2 = math.sqrt(p2)
p3 = p3**(1/3)

print(p1)
print(p2)
print(p3)
print(pi)
