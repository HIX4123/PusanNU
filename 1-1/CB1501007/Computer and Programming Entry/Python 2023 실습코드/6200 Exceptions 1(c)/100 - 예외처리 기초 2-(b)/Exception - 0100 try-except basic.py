"""
예외 처리는 이 네 개만 알면 된다.

    try : 에러 발생 가능성이 있는 코드 실행
    except : 에러 발생 시 (생략 가능, 여러개 사용 가능)
    else : 에러가 발생하지 않았을 경우 실행 (생략 가능)
    finally : 항상 실행 (생략 가능)

그리고 위에서 설명한 에러 종류들을 직접 명시해서
except ValueError: , except NameError: 이런 식으로 써도 되지만,
어떤 에러가 발생할지 모르겠을 때는 최종적으로 except Exception:
    이라고 해서 이런저런 에러를 무조건 다 잡아버릴 수도 있다.
    except Exception as e: 라고 쓰고 print(e)로 출력하면 에러
    내용을 확인할 수도 있다.
"""

try:
    raise NameError('NameError') # NameError를 강제로 발생 시켰습니다!!

except NameError:
    print('Error!!!')                        # NameError 처리
    raise
