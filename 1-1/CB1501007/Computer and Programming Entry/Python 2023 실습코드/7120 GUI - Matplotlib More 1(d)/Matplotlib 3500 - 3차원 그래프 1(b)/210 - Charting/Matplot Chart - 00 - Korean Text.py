import matplotlib.pyplot as pl

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)



#You can change the x and y ranges displayed on your plot by:

pl.xlim(0, 10)  # �ְ� ����
pl.ylim(0, 140)


X = range(10)
Y = [x ** 2 for x in X]

pl.plot(X, Y)
pl.xlabel('���⿡ ���̺��� ǥ��')
pl.ylabel( 'y���� ���⿡ �����ϴ�.')
pl.title( '�ѱ��� �Ǵ��� ���ô�.')

pl.show()
