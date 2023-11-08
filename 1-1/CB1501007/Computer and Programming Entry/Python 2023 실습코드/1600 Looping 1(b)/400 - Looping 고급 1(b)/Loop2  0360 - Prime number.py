#for loop


N = int(input("검사한 숫자 N:"))

code = "Yes"
for i in range(2, N) :
    if N%i == 0 :
        print(N, "은 솟수가 아닙니다.")
        print("\n", i,"으로 나누어짐")
        code= "No"
        break ;


if code == "Yes" :      print(N, "은 소수입니다")
else :                  print(N, "은 소수가 아닙니다. ")

