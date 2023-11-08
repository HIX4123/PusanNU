
def try_to_change_string_reference(the_string):
    print('받은 문자열= ', the_string)
    the_string = '비올 때는 파전에 막걸리'
    print('set to', the_string)

This = '부산 갈매기 너는 누구냐?'

print('함수 호출 이전 This =', This)
try_to_change_string_reference( This)
print('함수 호출 이후 This =', This)