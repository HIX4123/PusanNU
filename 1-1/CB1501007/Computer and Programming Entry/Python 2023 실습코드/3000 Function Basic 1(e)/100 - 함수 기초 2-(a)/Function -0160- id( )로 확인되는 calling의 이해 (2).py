# mutable 개체는 변화가 반영됨. 예를 들어 list
# immutable 개체는 변화가 반영되지 않음, 단일 변수, tuple (  ) 등등
# Python에서는 원칙적으로 call by reference가 없음니다요.
#
#
def myfunc( a, b  ):        # 숫자는 값만 넘겨준다. Call by Value.. Vale
   a = a + 100              # 함수안에서 아무리 바꾸로 고쳐도 원 변수는 고정
   b = b*5                  # 함수에서의 변화는 그 값만 변동, 데이터는 불변
   return ( (a,b))          # how about return( a,b )

def herfunc( L ) :          # 리스트는 넘겨준 상황에서 원 데이터를 수정한다.
    x= L.pop(0)             # 앞의 원소를 꺼내서
    L.append(x)             # 제일 뒤에 넣어준다.
    return( len(L) )        # 이런 방식을 call by reference 라고 부른다.
                            # 함수 내에서의 변화가 실제를 변화시킴

def ref_demo(x):            # 아주 중요한 내용.
    print("In ref_demo(), x=",x," id=",id(x))
    x=42
    print("In ref_demo(), after x= 42")
    print("In ref_demo(), x=",x," id=",id(x))


x,y=10, 20
mlist= [5,6,7,8,9,10]
print("Before", x,y)
print("myfunc(a,b)=", myfunc(x,y))
print("after", x,y)


print("L before", mlist)
print("herfunc( L )=", herfunc( mlist ))
print("L after", mlist)


x= 23
print("outside=", x, id(x))
ref_demo(x)
print("outside=",x, id(x))
#error를 만들어 봅시다.
#so = 678
#me = "computer"
#they = "good"
#q = myfunc( x )
#q = myfunc( me, they )



