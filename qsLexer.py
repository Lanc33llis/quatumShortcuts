# Generated from qs.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\7")
        buf.write("\5\35\n\5\f\5\16\5 \13\5\3\5\7\5#\n\5\f\5\16\5&\13\5\3")
        buf.write("\5\5\5)\n\5\3\5\6\5,\n\5\r\5\16\5-\3\6\3\6\7\6\62\n\6")
        buf.write("\f\6\16\6\65\13\6\3\7\3\7\7\79\n\7\f\7\16\7<\13\7\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\6\nE\n\n\r\n\16\nF\3\n\3\n\2")
        buf.write("\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\n\3")
        buf.write("\2//\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\f\f\17\17)")
        buf.write(")\4\2,,\61\61\4\2--//\5\2\13\f\17\17\"\"\2P\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25")
        buf.write("\3\2\2\2\5\27\3\2\2\2\7\31\3\2\2\2\t\36\3\2\2\2\13/\3")
        buf.write("\2\2\2\r\66\3\2\2\2\17?\3\2\2\2\21A\3\2\2\2\23D\3\2\2")
        buf.write("\2\25\26\7*\2\2\26\4\3\2\2\2\27\30\7+\2\2\30\6\3\2\2\2")
        buf.write("\31\32\7.\2\2\32\b\3\2\2\2\33\35\t\2\2\2\34\33\3\2\2\2")
        buf.write("\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37(\3\2\2\2 ")
        buf.write("\36\3\2\2\2!#\t\3\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2\2")
        buf.write("$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\')\7\60\2\2($\3\2\2\2")
        buf.write("()\3\2\2\2)+\3\2\2\2*,\t\3\2\2+*\3\2\2\2,-\3\2\2\2-+\3")
        buf.write("\2\2\2-.\3\2\2\2.\n\3\2\2\2/\63\t\4\2\2\60\62\t\5\2\2")
        buf.write("\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\f\3\2\2\2\65\63\3\2\2\2\66:\7)\2\2\679\n\6\2\28")
        buf.write("\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:")
        buf.write("\3\2\2\2=>\7)\2\2>\16\3\2\2\2?@\t\7\2\2@\20\3\2\2\2AB")
        buf.write("\t\b\2\2B\22\3\2\2\2CE\t\t\2\2DC\3\2\2\2EF\3\2\2\2FD\3")
        buf.write("\2\2\2FG\3\2\2\2GH\3\2\2\2HI\b\n\2\2I\24\3\2\2\2\n\2\36")
        buf.write("$(-\63:F\3\b\2\2")
        return buf.getvalue()


class qsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NUMBER = 4
    ID = 5
    TEXT = 6
    MULTDIV = 7
    ADDSUB = 8
    SPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ID", "TEXT", "MULTDIV", "ADDSUB", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NUMBER", "ID", "TEXT", "MULTDIV", 
                  "ADDSUB", "SPACE" ]

    grammarFileName = "qs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


