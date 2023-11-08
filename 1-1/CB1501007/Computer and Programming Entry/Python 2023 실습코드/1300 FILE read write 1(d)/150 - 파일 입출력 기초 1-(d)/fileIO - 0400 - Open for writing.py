print ("------------실험 1--------------")
myfile = open("XXX.out", "w",encoding='cp949')
print(( "1. 일본 "),      file = myfile)  # 줄 맞추기가 중요함.
print(("2. 대한민국 "),   file = myfile)
print(("3. 독일"),        file = myfile)
print(("4. 핀란드 "),     file = myfile)
myfile.close();             # 열어본 화일은 반드시 닫아 주어야 합니다.

print("------------실험 2--------------")
myfile = open("XXX.out", "a",encoding='cp949')  # w를  a로 바꾸어 봅시다. append, write
print(" a. Reopen and Rewrite",    file=myfile)
print(" b. Happy Birthday To You", file=myfile)
myfile.close();

print("------------실험 3--------------")
leftfile  = open("seoul.inp",encoding='cp949')
rightfile = open("pusan.inp",encoding='cp949')
wholeft   = leftfile.readline()
whoright  = rightfile.readline()
print(wholeft, whoright)

leftfile.close()         # 이것이 없으면 화일이 저장이 안됩니다. 끝내기 작업
rightfile.close()        # 이것이 없으면 화일이 저장이 안됩니다. 끝