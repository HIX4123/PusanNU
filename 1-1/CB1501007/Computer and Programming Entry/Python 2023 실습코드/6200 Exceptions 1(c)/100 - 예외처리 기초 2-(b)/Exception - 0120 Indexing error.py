
def calc(values):
    sum = None
    # try...except...else
    try:
       sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print('인덱스에러')
    except Exception as err:
        print((str(err)))
    else:
        print('에러없음')
    finally:
        print(sum)

# 테스트
calc([1, 2, 3, 6]) # 출력: 에러없음 6
calc([1, 2])       # 출력: 인덱스에러 None
