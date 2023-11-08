
# scatterplot.py
import numpy as np
import pylab as pl
import matplotlib

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)


pl.title( '한글이 되는지 봅시다.')
pl.xlabel('여기에 레이블을 표시')
pl.ylabel( 'y축은 여기에 놓습니다.')



x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 최고값을 설정할 수 있다.
#pl.ylim(0, 40)
#pl.xlim( (0, 10))  # 최고값 설정

pl.plot(x, y, '-go') # 빨간색 동그라미. ro, 파란색 x는 'bx'
pl.show()

