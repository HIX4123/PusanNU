import numpy
import matplotlib.pyplot as plot

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)

plot.rcParams['axes.unicode_minus'] = False   # 음수 - r기호를 처리, 없으면 warning이 남.

X = numpy.linspace(-4, 4, 120)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plot.title(' 한글을 사용하려면 위와 같이 정의해야 함.', color="blue")
plot.xlabel('이것이 무엇이냐')
plot.ylabel('무궁화 꽃이 피었습니다.', color='r', fontsize=12)

#plot.plot(X, Y, marker="x", c = 'k') # 갯수가 작으면 marker 표시
plot.plot(X, Y, c = 'k')
plot.show()
