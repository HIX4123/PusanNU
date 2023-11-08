from re import search

with open("genome.txt") as f:
    genome = f.read().replace("\n", "") #게놈 데이터:str

S = input().split() # 접두문자열: list[str]
E = input().split() # 접미문자열: list[str]

pattern = rf"({'|'.join(S)}).*?({'|'.join(E)})" #패턴: str

res = []  # 반환값: list[str]
while True:
    tmp = search(pattern, genome) # 패턴 검색: re.Match
    if tmp is None:
        break
    res.append(tmp.group())
    genome = genome[tmp.span()[0] + 1 :]

print(sorted(res, key=lambda seq: (len(seq), seq))[0] if res else "None")
