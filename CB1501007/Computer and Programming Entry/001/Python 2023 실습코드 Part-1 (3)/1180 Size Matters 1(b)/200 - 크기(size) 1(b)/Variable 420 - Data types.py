
# List의 기초에 대하여 배웁니다. 교재 p.67
# --------- 자료형의 변경 (아주 중요함) -------------

print("형 변경 실험합니다")
a = "banana"
print("(1) ", a, type(a))
a = 1289
print("(2) ",a, type(a))  # Python의 형의 변경은 자유롭다, 그러나 Tuple은 곤란하다.


L = ['c', 'o', 'm', 'e', 'd', 'y']
print(L, type(L))

print("type({})= ",     type({}))
print("type(345)= ",    type(345))
print("type(345.0)= ",  type(345.0))
print("type('345')=",   type('345'))
print('type("345")=',   type("345"))
print("type([1,2,3])=", type([1,2,3]))
print("type((1,2,3))=", type((1,2,3,4,5)))


