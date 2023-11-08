customer_data = {}


# 두 집합의 유사도를 계산하는 함수
def calculate_similarity(set1, set2):
    return len(set1 & set2) / (len(set1 | set2) + 1)


# 입력; 딕셔너리 {고객: {제품}}
while True:
    try:
        tmp = list(map(str, input().split()))
        customer_data.setdefault(tmp[0], set()).update(set(tmp[1:]))
    except:
        break

# 유사도 DB
similarity_data = []
keys = sorted(customer_data)
for index, value1 in enumerate(keys):
    for value2 in keys[index + 1 :]:
        similarity_data.append(
            [
                [value1, value2],
                calculate_similarity(set1=customer_data[value1], set2=customer_data[value2]),
            ]
        )

# 데이터 정렬 및 출력
similarity_data.sort(key=lambda x: -x[1])
for i in similarity_data:
    if i[1] == similarity_data[0][1]:
        print(*i[0])
