from fractions import Fraction

fracs = [[1, 2, 1], [1, 2, 1], [1, 2, -1]]

while fracs[0][0] <= 20:
    real_sum = sum(Fraction(i[0] * i[2], i[1]) for i in fracs)
    if sum(i[1] * i[2] for i in fracs) != 0:
        wtf_sum = Fraction(
            sum(i[0] * i[2] for i in fracs), sum(i[1] * i[2] for i in fracs)
        )
    if (
        real_sum == wtf_sum
        and not (
            Fraction(fracs[0][0], fracs[0][1]) == Fraction(fracs[2][0], fracs[2][1])
        )
        and not (
            Fraction(fracs[0][0], fracs[0][1]) == Fraction(fracs[1][0], fracs[1][1])
        )
        and not (
            Fraction(fracs[1][0], fracs[1][1]) == Fraction(fracs[2][0], fracs[2][1])
        )
    ):
        print(" ".join(f"{i[0]}/{i[1]}" for i in fracs))
    fracs[-1][-2] += 1
    for i in range(len(fracs)):
        if fracs[-i][1] >= 20:
            fracs[-i][1] = 2
            fracs[-i][0] += 1
        if fracs[-i][0] >= 20:
            fracs[-i][0] = 1
            fracs[-i - 1][1] += 1
