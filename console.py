from halo import Halo
from antlr4 import *

from qsLexer import qsLexer
from qsParser import qsParser
from qsListener3 import qsListener

spinner = Halo(spinner="dots", color="white")

def main():
  print('''
  _____Quantum Shortcuts_____
  ___________________________
  -Custom Parser with ANTLR4-
  ___________________________
  ____Various Quantum Math___
  _________Functions_________
  ___________________________
  _______Version: 0.1.0______
  ___________________________
  ''')
  while True:
    print(">", end=" ")
    inputStream = InputStream(input())

    result = 0
    with spinner:
      lexer = qsLexer(inputStream)
      stream = CommonTokenStream(lexer)
      parser = qsParser(stream)
      tree = parser.parse()
      listener = qsListener()
      walker = ParseTreeWalker()
      walker.walk(listener, tree)
      result = listener.val
    print(f">> {result}")
main()