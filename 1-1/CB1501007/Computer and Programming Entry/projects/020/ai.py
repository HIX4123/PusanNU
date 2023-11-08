import re


def find_units(genome, pattern):
    res = []
    index = 0
    while True:
        tmp = re.search(pattern, genome[index:])
        if tmp:
            res.append(tmp.group())
            index += tmp.start() + 1
        else:
            return res


with open("genome.txt") as f:
    genome = f.read().replace("\n", "")

S = re.split(r"[, ]+", input())
E = re.split(r"[, ]+", input())

pattern = rf"({'|'.join(S)}).*?({'|'.join(E)})"

sol = sorted(find_units(genome, pattern), key=lambda seq: (len(seq), seq))

print(sol[0] if sol else "None")
