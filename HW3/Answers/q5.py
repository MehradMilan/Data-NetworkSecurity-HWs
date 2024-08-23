q = 288918539521089348336793240678493497771
a = 3
aXA = 12782377710547948619020211758683185425
aXB = 183364455173249021598006044125891817111

for i in range(1, q):
    Y = pow(a, i, q)
    if Y == aXB:
        print("Shared key: ", aXA ** i % q)
        break
    elif Y == aXA:
        print("Shared key: ", aXB ** i % q)
        break
