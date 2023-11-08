#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-07-13
#-------------------------------------------------------------------------------

def generateParentheses(openBr, closeBr, n, s = []):
	if closeBr == n:
		print(''.join(s))
		return

	if closeBr < openBr:
		s.append(')')
		generateParentheses(openBr, closeBr+1, n, s)
		s.pop()
	if openBr < n:
		s.append('(')
		generateParentheses(openBr+1, closeBr, n, s)
		s.pop()
	return

n = int(input())
generateParentheses(0, 0, n)