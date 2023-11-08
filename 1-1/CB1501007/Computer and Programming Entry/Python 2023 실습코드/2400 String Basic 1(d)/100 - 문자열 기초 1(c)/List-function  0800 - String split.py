
# 하나의 입력라인에서 token을 분리해내는 방법, string의 method()인 split을 이용

myline1 = "This is a simle statement for testing\n"
myline2 = " Summer $ time $ Killer movie $ Killerbee "

mylist = myline1.split()
print("Default split=", mylist)

mylist = myline1.split(' ')
print("Blank split=", mylist)


mylist = myline2.split('$')
print(mylist)
print("원소의 갯수는 = ", len(mylist))
print("마지막 원소는 = ", mylist[-1])

print("list( ) 함수 사용해보기")
astring = "Don't cry for me Argentina"
argen = list(astring)  # 하나의 문자열을 분절된 리스트로 만드는 방법
print(argen, '문자의 갯수 = ', len(argen))

# 문자열에서 단어별로 split()하는 방법에 대하여 매뉴얼을 이용해서 찾아보자.