#-*- coding: cp949 -*-
# Console���� standard input���� �а� standard output���� ���
#
#
# �����
# DOS cmd ��忡��
# > python mystdin.py
# �� �����ϸ� �ȴ�.
# > python stdin.py < data.txt
#
# ���� �ٸ� ȭ�� xxx.txt�� stndard output ����� ��������
# > python stdin.py < data.txt > xxx.txt
#

import sys
buffer = []
while True:
    userinput = sys.stdin.readline().rstrip('\n')
    print "your input=", userinput
    if userinput == 'quit':
        break
    else:
        buffer.append(userinput)