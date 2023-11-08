# 가독성을 고려하지 않고 토큰 압축에 중점을 둔 코드입니다.
# 가독성을 개선한 코드는 최초 제출한 코드에 있습니다.
# 이 아래에도 각주로 달아놓겠습니다.

import itertools

print(*[block.count(1) for block in list(itertools.zip_longest(*[[1]*i for i in list(map(int, input().split()))]))], 0)



# from itertools import zip_longest

# #main
# tile_shape = list(map(int, input().split()))#입력

# #1. tile_shape의 숫자들로 타일 모양의 리스트 생성
# #2. zip_longest 클래스로 길이에 상관없이 전치행렬 변환
# #3. 빈 공간은 0으로 채움
# tile_blocks = list(zip_longest(*[[1]*i for i in tile_shape], fillvalue=0))

# # 각 줄의 합 출력
# print(*[sum(block) for block in tile_blocks], 0)
