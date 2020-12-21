import sys
import ply.lex as lex
#----------------------------------From :https://www.itread01.com/p/512197.html-----------------------------------------
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'for' : 'FOR'
 }
 
tokens = ('NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN','SQUARE','ROOT','MORE','LESS','ID','RBRACKET','LBRACKET','SEMICOLON')


tokens = ['NAME',
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'EQUALS',
'LPAREN',
'RPAREN',
'SQUARE',
'ROOT',
'MORE',
'LESS',
'ID',
'SPACE',
'RBRACKET',
'LBRACKET',
'SEMICOLON'] + list(reserved.values())

t_SEMICOLON =r';'
t_MORE      =r'>'
t_LESS      =r'<'
t_PLUS      =r'\+'
t_MINUS     =r'-'
t_TIMES     =r'\*'
t_DIVIDE    =r'/'
t_SPACE     =r'\ '
t_EQUALS    =r'\='
t_RBRACKET  =r'\['
t_LBRACKET  =r'\]'
t_LPAREN    =r'\('
t_RPAREN    =r'\)'
t_NAME      =r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SQUARE    =r'\^'
t_ROOT      =r'\*\*'

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')# Check for reserved words
     return t
#----------------------------------End from---------------------------------------

def t_IF(t):
    r'if'
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value=int(t.value)
    except ValueError:
        print("Integer value too large %s" % t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno+= t.value.count("\n")

def t_error(t):
    print("Illegal charater '%s'" % t.value[0] )
    t.lexer.skip(1)
    
lexer = lex.lex()
lexer.input('-5')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)