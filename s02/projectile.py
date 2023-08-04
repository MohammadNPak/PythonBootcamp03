import math

v0 = float(input())
alpha = float(input())
alpha = math.radians(alpha)

G = 9.8
R = math.pow(v0, 2)*math.sin(2*alpha)/G
print(R)
