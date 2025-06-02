from lark import Lark, Transformer


grammar = r"""

%import common.DIGIT
%ignore " "

start: exp

exp: DIGIT "+" exp
   | DIGIT "-" exp
   | DIGIT

"""

parser = Lark(grammar, parser='lalr')
string = input("DIGITE UMA EXPRESSÃO: ")

try:
    for word in string:
        if(word.isspace()):
            continue
        print(f"Em: {word}")
        print(list(parser.lex(word)))
except Exception as e:
    print("\033[031mErro de Sintaxe\033[031")

