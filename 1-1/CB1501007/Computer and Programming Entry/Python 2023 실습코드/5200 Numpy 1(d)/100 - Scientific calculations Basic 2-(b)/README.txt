basic_01.	 
  numpy ���α׷��� �̿��Ͽ� array ���� ���
  numpy ���� �����ϴ� �Լ���
  array ���� a*b(aij * bij) a dot b (marix ��)

basic_02.
  numpy sum, min, max �Լ�, matrix indexing,  slice, �ݺ������

LinearExpression
  numpy�� �̿��Ͽ� 1�� ���� ������ �� ���ϴ� ���
  (�� ������ ������ ��� ������ ������ŭ ���� ���������� ������ �ߴ� ����)
  (-> ��������п��� ���������� �ر��ϴ� ����ε�, �̺κ��� �ڼ��� ���� ���ʿ� ������ �ϳ׿�)

attendance
  attendent.inp ���Ͽ��� 1~10���л� �⼮ ��Ȳ�� ������ �⼮ ��Ȳ ǥ���ϴ� ����

phone
  ���� phone ����, ���������� i,j �߽����� L �������� Box�ȿ� �ִ� �ڵ��� ����ڸ� ǥ�����ִ� ����
  Search_Box�� ������ ���� slice�� �̿��Ͽ� �ٲپ� ǥ�� �� ���� �ֽ��ϴ�.

def search_box(i,j,p,q) :
    result = list();
    submap = phone_map[i-p:i+p,j-q:j+q]
    for k in submap :
        for l in k :
            if l!="" :
                result.append(l)
    return result
