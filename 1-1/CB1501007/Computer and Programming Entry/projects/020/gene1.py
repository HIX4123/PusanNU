from re import search, split


# s로 시작하고 e로 끝나는 모든 문자열 추출
def find_units(genome, pattern):  # -> list[str]
    res = []
    while True:
        tmp = search(pattern, genome)
        if tmp:
            res.append(tmp.group())
            genome = genome[tmp.span()[0] + 1 :]
        else:
            break
    return res


# main
with open("genome.txt", "r") as f:
    genome = f.read().replace("\n", "")  # 게놈 데이터:str

S = split(r"[, ]+", input())  # 시작 유닛:list[str]
E = split(r"[, ]+", input())  # 끝 유닛:list[str]

pattern = rf"({'|'.join(S)}).*?({'|'.join(E)})"

sol = sorted(
    find_units(genome, pattern), key=lambda x: (len(x), x)
)  # 시작 유닛과 끝 유닛을 조합하여 모든 유닛을 추출하고, 길이와 알파벳 순으로 정렬: list[str]

print(sol[0] if sol else "None")
