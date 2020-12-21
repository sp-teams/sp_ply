import ply.yacc as yacc
import math as mt
from mylex import tokens
###
'''
expression  :表達式
term        :項
factor      :因子
const       :常數
integer     :整數
-----------------------------------------------------------------------------------------
Grammar                             Action                                              |
 --------------------------------    --------------------------------------------       |
 expression0 : expression1 + term    expression0.val = expression1.val + term.val       |
             | expression1 - term    expression0.val = expression1.val - term.val       |
             | term                  expression0.val = term.val                         |
                                                                                        |
 term0       : term1 * factor        term0.val = term1.val * factor.val                 |
             | term1 / factor        term0.val = term1.val / factor.val                 |
             | factor                term0.val = factor.val                             |
                                                                                        |
 factor      : NUMBER                factor.val = int(NUMBER.lexval)                    |
             | ( expression )        factor.val = expression.val                        |
                                                                                        |
-----------------------------------------------------------------------------------------

NUMBER --> factor --> term --> expression
'''
###
def p_expression_PLUS_UND_MINUS(p):
    ''' expression  :   expression PLUS term
                    |   expression MINUS term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    
def p_number_MINUS_NUMBER(p):
    '''expression   :   expression MINUS expression
                    |   MINUS expression'''
    if (len(p)==3):
            p[0] = -p[2]
    elif (len(p)==4):
        p[0] = p[1] - p[3]

def p_term_TIMES_UND_DIVIDE(p):
    ''' term    :   term TIMES factor
                |   term DIVIDE factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1] 

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    '''factor   :   LPAREN expression RPAREN
                |   LESS expression MORE'''
    if p[1] == '<' and p[3] == '>':
        p[0] = p[2]
    elif p[1] == '(' and p[3] == ')':
        p[0] = p[2]

def p_error(p):
    print("Syntax error in input !")

def p_square(p):
    'term : term SQUARE factor'
    p[0] = mt.pow(p[1],p[3])

def p_root(p):
    'term : term ROOT factor'
    p[0]=mt.pow(p[1],1/p[3])

def p_for(p):
    p[1]=='<' or '>' or '='
    p[0]==p[2]
    ## if p[1]=='<' and p[0]<p[3]






parser = yacc.yacc()


while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    