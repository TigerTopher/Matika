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

# # # # # # # # # C Y A N # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def p_statement(p):
    '''statement : declaration statementTop
                | expression statementTop
                | IfThenElse statementTop
                | AssignmentHead statementTop
                | WhileLoop statementTop
                | ForLoop statementTop
                | DoWhileLoop statementTop
                | unionAdd statementTop
                | unionKeys statementTop
                | typeCastToInt statementTop
                | typecastToFloat statementTop
                | FunctionDefinition statementTop
                | FunctionCall statementTop
                | returnDec statementTop
                | stringOpStatement statementTop
                | read t_LPAREN IDENTIFIER t_RPAREN t_SEMICOLON statementTop
                | print t_LPAREN content t_RPAREN t_SEMICOLON statementTop'''              

def p_statement1(p):
    '''statement1 : declaration
                | expression
                | IfThenElse
                | AssignmentHead
                | WhileLoop
                | ForLoop
                | DoWhileLoop
                | unionAdd
                | unionKeys
                | typeCastToInt
                | typecastToFloat
                | FunctionDefinition
                | FunctionCall
                | returnDec
                | stringOpStatement
                | read t_LPAREN IDENTIFIER t_RPAREN t_SEMICOLON
                | print t_LPAREN content t_RPAREN t_SEMICOLON'''

def p_booleanValue(p):
    '''booleanValue : TRUE
                    | FALSE'''

def p_content(p):
    '''content : toPrint morePrint'''

def p_morePrint(p):
    '''morePrint : t_PLUS toPrint morePrint
                | t_EMPTY'''

def p_toPrint(p):
    '''toPrint : t_QUOTE string t_QUOTE
              | number
              | IDENTIFIER'''

def p_declaration(p):
    '''declaration : identifierDeclaration
                  | listDec
                  | unionDec'''

def p_identifierDeclaration(p):
    '''identifierDeclaration : dataType IDENTIFIER t_SEMICOLON
                            | dataType IDENTIFIER t_LBRACK CONSTANT t_RBRACK t_SEMICOLON
                            | dataType IDENTIFIER t_LBRACK CONSTANT t_RBRACK t_EQUAL expression t_SEMICOLON
                            | dataType IDENTIFIER t_EQUAL expression t_SEMICOLON'''

def p_dataType(p):
  '''dataType : INT
            | BOOLEAN
            | CHAR
            | LONG
            | FLOAT
            | DOUBLE'''
  print p[1]

def p_stringOPStatement(p):
    '''stringOpStatement : IDENTIFIER stringOP t_LPAREN string t_RPAREN t_SEMICOLON
                        | IDENTIFIER stringOp t_LPAREN IDENTIFIER t_RPAREN t_SEMICOLON'''

def p_stringOp(p):
    '''stringOp : SPLIT
                | STRIP 
                | CONCAT
                | COPY'''

def p_listDec(p):
    '''listDec : IDENTIFIER t_EQUAL list t_SEMICOLON'''

def p_list(p):
    '''list : t_LBRACK listElem t_RBRACK'''

def p_listElem(p):
    '''listElem : validListUnionValues
                | validListUnionValues t_COMMA listElem
                | t_EMPTY'''

def p_listEval(p):
    '''listEval : IDENTIFIER t_LBRACK CONSTANT t_RBRACK'''

def p_unionDec(p):
    '''unionDec : IDENTIFIER t_EQUAL uninon t_SEMICOLON'''

def p_union(p):
    '''union : t_LCURLY unionElement t_RCURLY'''

def p_unionElement(p):
    '''unionElement : string t_EQUAL validListUnionValues
                  | string t_EQUAL validListUnionValues t_COMMA unionElement
                  | t_EMPTY'''

def p_unionAdd(p):
    '''unionAdd : IDENTIFIER t_LBRACK string t_RBRACK t_EQUAL validListUnionValues t_SEMICOLON'''

def p_validListUnionValues(p):
    '''validListUnionValues : intValue
                          | longValue
                          | floatValue
                          | doubleValue
                          | charValue
                          | booleanValue
                          | stringValue
                          | listValue'''

def p_unionKeys(p):
    '''unionKeys : IDENTIFIER KEYS t_SEMICOLON'''

def p_unionEval(p):
    '''unionEval : IDENTIFIER t_ARROW string'''

def p_typeCastToInt(p):
    '''typeCastToInt : TC_INT IDENTIFIER t_SEMICOLON'''

def p_typeCastToFloat(p):
    '''typecastToFloat : TC_FLOAT IDENTIFIER t_SEMICOLON'''

def p_WhileLoop(p):
    '''WhileLoop : WHILE Condition t_COLON Body'''

def p_Body(p):
    '''Body : statementMore'''

def p_statementMore(p):
    '''statementMore : indent statementMoreCont
                    | END'''

def p_statementMoreCont(p):
    '''statementMoreCont : statement1 statementMore'''

def p_ForLoop(p):
    '''ForLoop : for t_LPAREN AssignmentHead Condition Increment t_RPAREN Body'''

def p_DoWhileLoop(p):
    '''DoWhileLoop : DO t_COLON Body WHILE Condition t_SEMICOLON'''

def p_Increment(p):
    '''Increment : t_SEMICOLON Operand Options'''

def p_Options(p):
    '''Options : Iterator
              | AssignmentOperator Operand'''

def p_IfThenElse(p):
    '''IfThenElse : IF Condition t_COLON Body addElif'''

def p_addElif(p):
    '''addElif : addElif2
              | FI
              | ELSE t_COLON Body'''

def p_addElif2(p):
    '''addElif2 : elifClause addElif'''

def p_elifClause(p):
    '''elifClause : ELIF Condition t_COLON Body'''

def p_Condition(p):
    '''Condition : RelationExpression
                | t_LPAREN Condition Compound Condition t_RPAREN
                | t_LPAREN NOT Condition t_RPAREN'''

def p_Operand(p):
    '''Operand : IDENTIFIER
              | CONSTANT
              | booleanValue'''

def p_Compound(p):
    '''Compound : AND
              | OR'''

def p_Iterator(p):
    '''Iterator : t_PLUSPLUS
              | t_MINUSMINUS
              | t_EMPTY'''

def p_AssignmentHead(p):
    '''AssignmentHead : t_BAR IDENTIFIER AssignmentOption t_BAR t_SEMICOLON'''

def p_AssignmentOption(p):
    '''AssignmentOption : t_EQUAL AssignmentOptionChain
                      | AssignmentOperator AssignmentOptions2'''

def p_AssignmentOptions2(p):
    '''AssingmentOptions2 : CONSTANT
                        | ArithmeticExpression'''

def p_AssignmentOptionChain(p):
    '''AssignmentOptionsChain : listEval
                              | Function
                              | unionEval
                              | AssignmentOptions2'''

def p_AssignmentOperator(p):
    '''AssignmentOperator : t_PLUSEQUAL
                        | t_MINUSEQUAL
                        | t_MULTEQUAL
                        | t_DIVEQUAL
                        | t_MODEQUAL'''

def p_expression(p):
    '''expression : ArithmeticExpression
                  | listEval
                  | list
                  | union
                  | RelationExpression'''

def p_RelationExpression(p):
    '''RelationExpression : t_LPAREN Operand RelationOperator Operand t_RPAREN'''

def p_ArithmeticExpression(p):
    '''ArithmeticExpression : t_LESSTHAN Operand ArithmeticOperator Operand t_GREATERTHAN'''

def p_ArithmeticOperator(p):
    '''ArithmeticOperator : t_PLUS
                          | t_MINUS
                          | t_MULT
                          | t_DIV
                          | t_MOD'''

def p_RelationOperator(p):
    '''RelationOperator : t_EQUALEQUAL
                        | t_EQUAL
                        | t_LESSTHAN
                        | t_GREATERTHAN
                        | t_GREATEREQ
                        | t_LESSEREQ
                        | t_NOTEQ'''

def p_FunctionDefinition(p):
    '''p_FunctionDefinition : dataType Function t_COLON Body'''

def p_Function(p):
    '''Function : IDENTIFIER t_LPAREN Parameter t_RPAREN'''

def p_Parameter(p):
    ''' Parameter : dataType IDENTIFIER
                  | dataType IDENTIFIER t_COMMA Parameter
                  | t_EMPTY'''

def p_FunctionCall(p):
    ''' FunctionCall : IDENTIFIER t_LPAREN FunctionCallParameter t_RPAREN t_SEMICOLON'''

def p_FunctionCallParameter(p):
    '''FunctionCallParameter : IDENTIFIER
                            | IDENTIFIER t_COMMA p_FunctionCallParameter
                            | t_EMPTY'''

def p_returnDec(p):
    '''returnDec : RETURN CONSTANT t_SEMICOLON
                | RETURN IDENTIFIER t_SEMICOLON
                | RETURN expression t_SEMICOLON'''


 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
