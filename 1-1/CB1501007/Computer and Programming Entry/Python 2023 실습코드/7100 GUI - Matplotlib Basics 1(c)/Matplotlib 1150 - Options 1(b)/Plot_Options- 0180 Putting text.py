import numpy
import matplotlib.pyplot as plot

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)

X = numpy.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

box = {
	'facecolor' : '.75',
	'edgecolor' : 'r',
    'boxstyle'  : 'round'
}

plot.text(-0.5, -0.20, 'Backward minimum', bbox = box)
plot.text(-0.7,  8.40, '코로나 지긋지긋해' )

plot.plot(X, Y, c = 'k')
plot.show()
