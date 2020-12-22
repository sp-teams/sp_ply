import ply.yacc as yacc
import math as mt
from mylex import tokens

#
#expression  :表達式
#term        :項
#factor      :因子
#const       :常數
#integer     :整數
#-----------------------------------------------------------------------------------------
#Grammar                             Action                                              |
# --------------------------------    --------------------------------------------       |
# expression0 : expression1 + term    expression0.val = expression1.val + term.val       |
#             | expression1 - term    expression0.val = expression1.val - term.val       |
#             | term                  expression0.val = term.val                         |
#                                                                                        |
# term0       : term1 * factor        term0.val = term1.val * factor.val                 |
#             | term1 / factor        term0.val = term1.val / factor.val                 |
#             | factor                term0.val = factor.val                             |
#                                                                                        |
# factor      : NUMBER                factor.val = int(NUMBER.lexval)                    |
#             | ( expression )        factor.val = expression.val                        |
#                                                                                        |
#-----------------------------------------------------------------------------------------
#
#NUMBER --> factor --> term --> expression
#
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

def p_statement(p):
    'statement    :   expression'
    p[0]=p[1]

def p_if(p):
    '''if_statement     :   IF LPAREN expression RPAREN SPACE statement 
                        |   IF LPAREN expression RPAREN statement
                        |   IF LPAREN expression RPAREN statement SPACE ELSE SPACE statement
                        |   IF LPAREN expression RPAREN SPACE statement SPACE ELSE SPACE statement'''
    p[0]=p[3]
#--------------------------------------------
    if (len(p) == 7):
        if p[0] != 0 :
            p[0]=p[6]
        elif p[0] == 0 :
            print("Your condition less than 0 and the sentence didn't have else statement")
#--------------------------------------------
    elif(len(p) == 6):
        if p[0] != 0 :
            p[0]=p[5]
        elif p[0] == 0 :
            print("Your condition less than 0 and the sentence didn't have else statement")
#--------------------------------------------
    elif (len(p) == 11):
        if p[0] != 0 :
            p[0]=p[6]
        elif p[0] == 0 :
            p[0]=p[10]
#--------------------------------------------
    elif (len(p) == 10):
        if p[0] != 0 :
            p[0]=p[5]
        elif p[0] == 0 :
            p[0]=p[9]
#--------------------------------------------

#def p_for(p):
#    '''for_statement    :   FOR LPAREN  RPAREN '''

def p_answer(p):
    'term : if_statement'
    p[0]=p[1]

def p_end(p):
    '''end : SEMICOLON'''
    return p[0]

parser = yacc.yacc()


while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)