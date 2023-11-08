from cProfile import run

def main():
    from sys import stdin

    input_s = stdin.readline

    # input
    length, C = map(int, input_s().split())
    p = [int(input_s()) for _ in range(length)]

    for active in range(2**length - 1, -1, -1):
        unhashed_active = list(map(int, f"{active:b}".zfill(length)))
        chosen, unchosen = [], []
        for i, j in zip(p, unhashed_active):
            if j == 1:
                chosen.append(i)
            else:
                unchosen.append(i)
        price = sum(chosen)
        lower_limit = C - min(unchosen, default=1)
        if C >= price > lower_limit:
            print(*(i + 1 for i, j in enumerate(unhashed_active) if j == 1))


if __name__ == '__main__':
    run("main()", sort="tottime")

