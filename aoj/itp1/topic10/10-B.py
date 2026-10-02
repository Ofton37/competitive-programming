import math
a,b,C = map(float,input().split())
rad = math.radians(C)
S = a*b*math.sin(rad)/2
h = b*math.sin(rad)
c = math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(rad)))
L = a+b+c
print(S)
print(L)
print(h)
