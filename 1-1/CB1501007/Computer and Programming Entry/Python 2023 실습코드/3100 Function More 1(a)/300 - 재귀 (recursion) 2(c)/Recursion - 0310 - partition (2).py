
# 숫자 n을 m이하의 숫자의 합으로 나타내는 방법의 수
# 아래는 6을 4이하의 숫자로 표시하는 법은 9가지

# 1. 6 = 2 + 4
# 2. 6 = 1 + 1 + 4
# 3. 6 = 3 + 3
# 4. 6 = 1 + 2 + 3
# 5. 6 = 1 + 1 + 1 + 3
# 6. 6 = 2 + 2 + 2
# 7. 6 = 1 + 1 + 2 + 2
# 8. 6 = 1 + 1 + 1 + 1 + 2
# 9. 6 = 1 + 1 + 1 + 1 + 1 + 1

# 모든 경우는 m이 하나 이상  포함된 경우와 m-1 이하로만 구성된 경우로 나뉜다.

def count_partitions(n, m): #    """Count the ways to partition n using parts up to m."""
        if   n == 0:             return 1
        elif n  < 0:             return 0
        elif m == 0:             return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m-1)



print("partition(9,3)=", count_partitions(9,3))