import sys
from antlr4 import *

from qsLexer import qsLexer
from qsParser import qsParser
from qsListener2 import qsListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = qsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = qsParser(stream)
    tree = parser.parse()
    listener = qsListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.val)
if __name__ == '__main__':
    main(sys.argv)