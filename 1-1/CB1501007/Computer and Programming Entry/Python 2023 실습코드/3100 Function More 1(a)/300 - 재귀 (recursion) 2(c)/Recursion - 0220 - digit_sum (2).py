

def sum_digits(n): # 양의 정수의 모든 숫자의 총합 구하기
        if n < 10:
            return n
        else:
            all_but_last = n // 10
            last         =  n % 10
            return sum_digits(all_but_last) + last




print("3456700의 digit 합= ", sum_digits( 3456700 ))
print("100000100의 digit 합= ", sum_digits( 100000100 ))
