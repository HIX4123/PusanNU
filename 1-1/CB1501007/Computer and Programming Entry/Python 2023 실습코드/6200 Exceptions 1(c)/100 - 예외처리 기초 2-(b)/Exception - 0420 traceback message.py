
import traceback

def getTracebackStr(): # 오류가 난 문장의 번호를 찍어 준다.
	lines = traceback.format_exc().strip().split('\n')
	rl = [lines[-1]]
	lines = lines[1:-1]
	lines.reverse()

	for i in range(0,len(lines),2):
		rl.append('^\t%s at %s' % (lines[i].strip(),lines[i+1].strip()))

	return '\n'.join(rl)


def d(): return 1/0
def c(): return d()
def b(): return c()
def a(): return b()


try:
	print(a())
except Exception as e:
	print(getTracebackStr())

