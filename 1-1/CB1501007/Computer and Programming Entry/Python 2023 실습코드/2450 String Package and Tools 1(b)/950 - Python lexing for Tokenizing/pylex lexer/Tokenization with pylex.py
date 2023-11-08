# 생각보다 편하군... 2022
# 먼저 다음 2개 ply 와 lex를 미리 INSTALL 해야 한다.
# 중간에 좀 error가 나지만 무시하고 처리해야 한다.


import ply.lex as lex

# List of simple token names.   항상 필요하다.
tokens = (
'DCOL',
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'LBRACE',
'RBRACE',
'RPAREN',
'EQUL',
'ID',
'COLON',
'SEMICOL',
'LESS',
'GTE',
'DOT',
'COMMA'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUL    = r'='
t_COLON   = '\:'
t_SEMICOL = r'\;'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LESS    = r'\<'
t_GTE     = r'\>'
t_DOT     = r'\.'
t_DCOL    = r'\:\:'
t_COMMA   = r'\,'
t_ignore_COMMENT = r'\#.*'

reserved = {'for':'FOR', 'if' : 'IF', 'then' : 'THEN',
             'else' : 'ELSE', 'while' : 'WHILE', 'do':'DO',
             'def':'DEF' }


# 특정한 A regular expression과 일치한 token을 찾았을 때의 동작
def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# comment 문장은 모두 pass를 이용하여
def t_COMMENT(t):
    r'\/\/.*'
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
template<typename T>
std::vector<T> slice(std::vector<T> const &v, int m, int n) {
    auto first = v.cbegin() + m;
    auto last = v.cbegin() + n + 1;

    // comment example

    std::vector<T> vec(first, last);
    return vec;
}

'''

# Give the lexer some input
lexer.input(data)

while True:
 tok = lexer.token()
 if not tok: break      # No more input
 print(tok)  # tok.type, tok.value, tok.lineno, tok.lexpos
 #print(tok.type)
 #print(tok.lexpos)