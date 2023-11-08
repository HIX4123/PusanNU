import matplotlib.pyplot as pl

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)



#You can change the x and y ranges displayed on your plot by:

pl.xlim(0, 10)  # 최고값 설정
pl.ylim(0, 140)


X = range(10)
Y = [x ** 2 for x in X]

pl.plot(X, Y)
pl.xlabel('여기에 레이블을 표시')
pl.ylabel( 'y축은 여기에 놓습니다.')
pl.title( '한글이 되는지 봅시다.')

pl.show()
