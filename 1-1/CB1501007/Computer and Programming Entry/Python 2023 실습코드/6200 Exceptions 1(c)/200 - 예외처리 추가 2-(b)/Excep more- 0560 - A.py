
import sys


myl = [ 13, ['a', 'b', 'x'], 45, 65, -23, 50, -33, 7, "Great", 99]

for this in range(len(myl)) :
    print("myl[",this,"]=", myl[this])


index= [ 5, 4, 8, 19, -2, 7, 4, 13]

for k in index :
    try :
        print("myl[",k,"]=", myl[k])
    except IndexError :
        print("Oh,", k, "번째에서 범위가 벗어났네요")
        xxx = eval(input( "어떻게 할까요 ? 3을 선택하면 바로 중단, 아니면 계속"))
        print(xxx)
        if xxx == 3 :
            print("심한 오류때문에 중단합니다.")
            sys.exit(1)


