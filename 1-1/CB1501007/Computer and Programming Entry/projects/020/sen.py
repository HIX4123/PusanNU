import sys

f = open("genome.txt", "r")
genome = f.read().replace("\n", "")
f.close()

S = sys.stdin.readline().split()
E = sys.stdin.readline().split()
SiIndex = []
EiIndex = []
ans = "None"

for i in range(len(S)):
    for j in range(len(genome)):
        if len(genome) - len(S[i]) < j:
            break
        isExist = True
        for k in range(len(S[i])):
            if genome[j + k] != S[i][k]:
                isExist = False
                break

        if isExist:
            SiIndex.append((j, j + len(S[i])))

for i in range(len(E)):
    for j in range(len(genome)):
        if len(genome) - len(E[i]) <= j:
            break
        isExist = True
        for k in range(len(E[i])):
            if genome[j + k] != E[i][k]:
                isExist = False
                break

        if isExist:
            EiIndex.append((j, j + len(E[i])))

for i in range(len(SiIndex)):
    for j in range(len(EiIndex)):
        if SiIndex[i][1] > EiIndex[j][0]:
            continue
        isExist = True
        left = SiIndex[i][0] + 1
        right = EiIndex[j][1] - 1

        for k in range(len(SiIndex)):
            if i == k:
                continue
            if left <= SiIndex[k][0] and SiIndex[k][1] <= right:
                isExist = False
                break

        for k in range(len(EiIndex)):
            if j == k:
                continue
            if left <= EiIndex[k][0] and EiIndex[k][1] <= right:
                isExist = False
                break

        if isExist:
            check = genome[left - 1 : right + 1]
            if ans == "None":
                ans = check[:]
            elif len(ans) > len(check):
                ans = check[:]
            elif len(ans) == len(check):
                if ans > check:
                    ans = check
print(ans)
