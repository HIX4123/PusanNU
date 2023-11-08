import re

f = open("genome.txt", "r")  # dna 파일 받기
dna = f.read().replace("\n", "")
f.close()
dna_list = []  # 찾은 dna들을 넣을 파일

starting_markers = input().split()
ending_markers = input().split()

pattern = (
    "("
    + "|".join(starting_markers)
    + ")"
    + ".*?"
    + "("
    + "|".join(ending_markers)
    + ")"
)  # dna 패턴

while True:
    dna_match = re.search(pattern, dna)
    if dna_match == None:
        break
    dna_list.append(dna_match.group())
    dna = dna[dna_match.span()[0] + 1 :]

if dna_list == []:  # 찾은 dna 출력
    print("None")
else:
    shortest_sequence = sorted(dna_list, key=lambda seq: (len(seq), seq))[0]
    print(shortest_sequence)
