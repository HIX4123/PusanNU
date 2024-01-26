---
marp: true
theme: default
class: invert
paginate: true
---

# **숫자 야구 Solver 제작**

2023년 KEEPER 기술문서
14기생 권민규

## **목차**

1. 목적
2. 계획 및 일정

---

## **목적**

- 숫자 야구 문제를 내는 알고리즘 문제와 그 해답만 익히 알려짐
- 문제를 내는 것이 아닌 문제를 푸는 것에 집중
- 스트라이크, 볼 등의 분기점 고려 최적의 알고리즘 제작

---

## **계획 및 일정**

- ~중간발표: 핵심 알고리즘 정리 및 구현
- ~최종발표: UI 구성 및 결과물 제작

---

## 핵심 알고리즘 정리 및 구현

- 원래 알고리즘적 측면에서 유리한 매커니즘보다는 사람이 숫자 야구를 푸는 방식에 가깝게 알고리즘을 구현하는 것이 목적이었음
  - 기계의 측면에서는 숫자가 6자리라고 해도 비교적 빠르게 초 단위로 순회하며 필터링을 해도 문제없음
  - 하지만 사람에게는 불가능한 일이므로 사용 가능한 숫자를 거르거나 여러 힌트를 연계해 자릿수를 추측하는 등의 휴리스틱한 방법을 사용
  - 이러한 접근을 구체화하여 알고리즘으로 표현해보고자 하는 것이 당초의 목적이었으나
  - 과도한 분기와 스파게티로 못 써먹을 코드가 되어 통상적인 방법으로 재작성
  
---

## 핵심 알고리즘 정리 및 구현

```python
def main():
    attempts = []
    candidate = create_candidates()

    print("Welcome to the number baseball game solver!")
    print("Is it 0123?")

    while True:
        input_string = input("Enter result: ")
        if input_string == "show-all-available":
            print(*candidate)
            continue
        elif input_string == "yes":
            print("I knew it!")
            break

        attempt = {"attempt": candidate[0], "result": input_string.upper()}
        attempts.append(attempt)

        candidate = [
            cand
            for cand in candidate
            if compare(cand, attempt["attempt"]) == attempt["result"]
        ]

        if len(candidate) == 1:
            print(f"The number must be {candidate[0]}")
            break
        elif len(candidate) == 0:
            print("No number is possible")
            break
        else:
            print(f"How about {candidate[0]}?")
```
