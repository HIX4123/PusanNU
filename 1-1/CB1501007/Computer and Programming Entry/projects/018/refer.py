from re import findall
from sys import stdin

foo = sorted(
    set(range(1, int(stdin.readline()) + 1))  # 레퍼런스 리스트 생성
    ^ {
        int(j)
        for i in findall(
            r"\[[0-9, ]+\]", "".join(stdin.read().splitlines())
        )  # 레퍼런스 형식에 맞는 텍스트를 모두 찾아
        for j in i[1:-1].split(",")  # 숫자 추출
    }
)

print(0 if not foo else "\n".join(map(str, foo)))
