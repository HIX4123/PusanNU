# 전체 파일을 하나의 문자열로 읽어 넣음

with open('rotary.txt', 'r',encoding='cp949') as file:
     dfile = file.read().replace('\n', '')



print(f"\n 입력파일 문자열(\\n 삭제 후) \n\n {dfile}")
print(f"\n 문자열 길이 ={len(dfile)}")

with open('rotary.txt', 'r',encoding='cp949') as file:
     dfile = file.read()

print(f"\n 입력파일 문자열 원본  \n\n {dfile}")
print(f"\n 문자열 길이 ={len(dfile)}")