
"""
pickle 프로토콜과 JSON (JavaScript Object Notation) 간에는 근본적인 차이가 있습니다:
• JSON은 텍스트 직렬화 형식(유니코드 텍스트를 출력하지만,
  대개는 utf-8 으로 인코딩됩니다)인 반면, pickle은 바이너리 직렬화 형식입니다.
• JSON은 사람이 읽을 수 있지만, 피클은 그렇지 않습니다.
• JSON은 상호 운용이 가능하며 파이썬 생태계 외부에서 널리 사용되는 반면,
 피클은 파이썬으로만 한정됩니다.
• JSON은, 기본적으로, 파이썬 내장형 일부만 표시할 수 있으며 사용자 정의 클래스는 표시할 수 없습니다;
  피클은 매우 많은 수의 파이썬 형을 나타낼 수 있습니다
  그 중 많은 것들은 파이썬의 인트로스펙션 기능을 영리하게 사용하여 자동으로;
  복잡한 경우는 특정 객체 API 를 구현해서 해결할 수 있습니다);
• pickle과 달리, 신뢰할 수 없는 JSON의 역 직렬화는 그 자체로 임의 코드 실행 취약점을 만들지는 않습니다.

"""

import pickle


number_of_data = int(input('갯수 : '))
data = []

for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

file = open('./data/important', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()


