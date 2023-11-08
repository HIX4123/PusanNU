# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
# 먼저 다음 2개를 미리 INSTALL 해야 한다.  ply 와 lex
# 중간에 좀 error가 나지만 무시하고 처리해야 한다.
# https://fwani.tistory.com/17 [FWANI's 코딩로그]


import ply.lex as lex

# List of token names.   This is always required
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'EQUL',
'ID',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUL    = r'='
t_ignore_COMMENT = r'\#.*'

reserved = {'for':'FOR', 'if' : 'IF', 'then' : 'THEN',
             'else' : 'ELSE', 'while' : 'WHILE', 'do':'DO' }


# A regular expression rule with some action code
def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# 리턴값을 무시
def t_COMMENT(t):
    r'\#.*'
    pass # ignore_ prefix 사용


def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)


t_ignore  = ' \t' # A string containing ignored characters (spaces and tabs)


def t_error(t): # Error handling rule
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)

# ------------ 수행을 해보자. ------------

lexer = lex.lex()  # Build the lexer


data = '''          # Test it out
3 + book23*( 10 ) / 324
tomboy23 =
goodwill = 45 * 6
+  3446 - banana
+ -20 *2
'''

# Give the lexer some input
lexer.input(data)

while True:
 tok = lexer.token()
 if not tok: break      # No more input
 print(tok)  # tok.type, tok.value, tok.lineno, tok.lexpos
 #print(tok.type)
 #print(tok.lexpos)