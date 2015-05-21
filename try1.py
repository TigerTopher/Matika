# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

def p_statementAug(p):
  'statementAug : statementTop'

def p_statementTop(p):
  '''statementTop : END
                  | statement'''

def p_statement(p):
    '''statement : declaration statementTop
                | expression statementTop'''

def p_expression(p):
  '''expression : ArithmeticExpression
                | RelationExpression'''
#                 | listEval
#                 | list
#                 | union
#                 | RelationExpression'''

def p_booleanValue(p):
  '''booleanValue : TRUE 
                  | FALSE'''

def p_Iterator(p):
  '''Iterator : PLUSPLUS
              | MINUSMINUS
              | '''

def p_ArithmeticExpression(p):
  'ArithmeticExpression : LESSTHAN Operand ArithmeticOperator Operand GREATERTHAN'

def p_RelationExpression(p):
  '''RelationExpression : LPAREN Operand ArithmeticOperator Operand RPAREN '''

def p_Compound(p):
  '''Compound : AND
              | OR '''

def p_Operand(p):
  '''Operand : IDENTIFIER
             | CONSTANT
             | booleanValue'''

def p_ArithmeticOperator(p):
  '''ArithmeticOperator : PLUS
                        | MINUS
                        | MULT
                        | DIV
                        | MOD'''

#def p_list(p):
#    '''listEval : LBRACK listElem RBRACK '''

#def p_listElem(p):
#  '''listElem : validListUnionValues
#              | validListUnionValues , listElem
#              | None '''


#def p_listEval(p):
#  '''listEval : IDENTIFIER LBRACK CONSTANT RBRACK '''

#def p_listDec(p):
#  '''listDec : IDENTIFIER = list SEMICOLON'''

def p_declaration(p):
    '''declaration : identifierDeclaration'''

def p_identifierDeclaration(p): 
  'identifierDeclaration : dataType IDENTIFIER SEMICOLON'
  print p[2]

#def p_union(p):
#  '''union : { unionElement }'''


  
def p_dataType(p):
  '''dataType : INT
            | BOOLEAN
            | CHAR
            | LONG
            | FLOAT
            | DOUBLE'''
  print p[1]





# Error rule for syntax errors
def p_error(p):
    if p:
         print("Syntax error of type: ", p.type, " with token value: ", p.value, "in ", p.lineno, p.lexpos)
         # Just discard the token and tell the parser it's okay.
         #parser.errok()
    print "ERROR"

# Build the parser
parser = yacc.yacc()


while True:
  try:
    s = raw_input('calc > ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s, tracking=True)
  print(result)