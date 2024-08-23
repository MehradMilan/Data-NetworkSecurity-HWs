from math import gcd

n1 = 882389665577830838482125131852013816279695311
n2 = 726247788835915752041026275800104626981008161
e1 = 65537
e2 = 5

p = gcd(n1, n2)

q1 = n1 // p
q2 = n2 // p

phi1 = (p - 1) * (q1 - 1)

d1 = pow(e1, -1, phi1)

phi2 = (p - 1) * (q2 - 1)

d2 = pow(e2, -1, phi2)

print("PRIVATE KEY 1: ", d1)
print("PRIVATE KEY 2: ", d2)