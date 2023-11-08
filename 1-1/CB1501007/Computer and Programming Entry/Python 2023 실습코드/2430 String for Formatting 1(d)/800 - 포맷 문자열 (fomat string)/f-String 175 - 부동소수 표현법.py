#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-12
#-------------------------------------------------------------------------------

# 문장안에서 { }를 사용하려면 double로 사용해야 한다.

val = 1234.567890123

print(f'1. {val:.2f}')
print(f'2. {val:.5f}')
print(f'3. {val:.8f}')
print(f'4. {val:5.2f}')
print(f'5. {val:7.3f}')
print(f'6. {val:10.5f}')

print("\n exponent 숫자 출력하기\n")

val = .567890123e+6  # scientific 표기법(notation)

print(f'1. {val:.2f}')
print(f'2. {val:.5f}')
print(f'3. {val:.8f}')
print(f'4. {val:5.2f}')
print(f'5. {val:7.3f}')
print(f'6. {val:10.5f}')


print("\n scientific notation\n ")
print(f'1. {val:.2}')
print(f'2. {val:.5}')
print(f'3. {val:.8}')
print(f'4. {val:5.2}')
print(f'5. {val:7.3}')
print(f'6. {val:10.5}')