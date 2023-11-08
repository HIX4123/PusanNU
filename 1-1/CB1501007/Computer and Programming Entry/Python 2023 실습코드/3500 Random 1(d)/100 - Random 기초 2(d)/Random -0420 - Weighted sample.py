#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

import numpy as np
import random

# weights는 입력 원소 순서대로의 weight
def weighted_sample(weights, sample_size): #   중복없이 weighted sampling을 한다.

    totals = np.cumsum(weights)
    sample = []
    for i in range(sample_size):
        rnd = random.random() * totals[-1]
        idx = np.searchsorted(totals,rnd,'right')
        sample.append(idx)
        totals[idx:] -= weights[idx]
    return sample



mw= [ 10, 5, 7, 9, 2, 1, 23]
d = list("abcdefg")

ans = weighted_sample (mw , 5)
print(ans)
