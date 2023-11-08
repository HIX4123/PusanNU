
#
# 삼각형의 3변의 길이가 a, b, c 가 주어진다.
# 삼각형이 되는지 ? 안되면 "No"를 return 한다.
# 된다면 직각,     둔각,   예각 삼각형인지의 여부를 돌려주는 함수를 작성
#         right , obtuse,  acute
#

def triangle(a, b, c ) :
# 여기를 채워 넣으시오.
# 제일 긴 변과 짧은 변을 먼저 찾아야겠죠?
   return ( "RIGHT")



a,b,c = eval(input( "삼각형 3변의 길이 a,b,c를 콤마로 분리하여 넣으시오:"))


answer = triangle(a,b,c)

print("삼각형의 길이=", a, b, c)
print("삼각형의 형태=", answer)






