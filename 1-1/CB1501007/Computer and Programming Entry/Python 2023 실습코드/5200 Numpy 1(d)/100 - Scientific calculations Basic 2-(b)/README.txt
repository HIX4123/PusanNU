basic_01.	 
  numpy 프로그램을 이용하여 array 생성 방법
  numpy 에서 제공하는 함수들
  array 연산 a*b(aij * bij) a dot b (marix 곱)

basic_02.
  numpy sum, min, max 함수, matrix indexing,  slice, 반복문사용

LinearExpression
  numpy를 이용하여 1차 연립 방정식 해 구하는 방법
  (맨 마지막 셈플의 경우 미지수 개수만큼 식을 넣지않으면 오류가 뜨는 예제)
  (-> 선형대수학에서 연립방정식 해구하는 방법인데, 이부분은 자세히 설명 할필요 없을듯 하네요)

attendance
  attendent.inp 파일에서 1~10번학생 출석 현황을 읽은후 출석 현황 표시하는 예제

phone
  과제 phone 예제, 예제에서는 i,j 중심으로 L 범위안의 Box안에 있는 핸드폰 사용자를 표시해주는 예제
  Search_Box를 다음과 같이 slice를 이용하여 바꾸어 표현 할 수도 있습니다.

def search_box(i,j,p,q) :
    result = list();
    submap = phone_map[i-p:i+p,j-q:j+q]
    for k in submap :
        for l in k :
            if l!="" :
                result.append(l)
    return result
