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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\5\5!\n\5\3\6\7\6$\n\6\f\6\16\6\'\13\6")
        buf.write("\3\6\7\6*\n\6\f\6\16\6-\13\6\3\6\5\6\60\n\6\3\6\6\6\63")
        buf.write("\n\6\r\6\16\6\64\3\7\3\7\7\79\n\7\f\7\16\7<\13\7\3\b\3")
        buf.write("\b\7\b@\n\b\f\b\16\bC\13\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\6\13L\n\13\r\13\16\13M\3\13\3\13\2\2\f\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\n\3\2//\3\2\62;\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\5\2\f\f\17\17))\4\2,,\61\61\4")
        buf.write("\2--//\5\2\13\f\17\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2")
        buf.write("\2\2\5\31\3\2\2\2\7\33\3\2\2\2\t \3\2\2\2\13%\3\2\2\2")
        buf.write("\r\66\3\2\2\2\17=\3\2\2\2\21F\3\2\2\2\23H\3\2\2\2\25K")
        buf.write("\3\2\2\2\27\30\7*\2\2\30\4\3\2\2\2\31\32\7+\2\2\32\6\3")
        buf.write("\2\2\2\33\34\7.\2\2\34\b\3\2\2\2\35\36\7v\2\2\36!\7q\2")
        buf.write("\2\37!\7?\2\2 \35\3\2\2\2 \37\3\2\2\2!\n\3\2\2\2\"$\t")
        buf.write("\2\2\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&/\3\2")
        buf.write("\2\2\'%\3\2\2\2(*\t\3\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.\60\7\60\2\2/+\3\2\2")
        buf.write("\2/\60\3\2\2\2\60\62\3\2\2\2\61\63\t\3\2\2\62\61\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\f\3\2")
        buf.write("\2\2\66:\t\4\2\2\679\t\5\2\28\67\3\2\2\29<\3\2\2\2:8\3")
        buf.write("\2\2\2:;\3\2\2\2;\16\3\2\2\2<:\3\2\2\2=A\7)\2\2>@\n\6")
        buf.write("\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2")
        buf.write("CA\3\2\2\2DE\7)\2\2E\20\3\2\2\2FG\t\7\2\2G\22\3\2\2\2")
        buf.write("HI\t\b\2\2I\24\3\2\2\2JL\t\t\2\2KJ\3\2\2\2LM\3\2\2\2M")
        buf.write("K\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\13\2\2P\26\3\2\2\2\13")
        buf.write("\2 %+/\64:AM\3\b\2\2")
        return buf.getvalue()


class qsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    KEYWORD = 4
    NUMBER = 5
    ID = 6
    TEXT = 7
    MULTDIV = 8
    ADDSUB = 9
    SPACE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "KEYWORD", "NUMBER", "ID", "TEXT", "MULTDIV", "ADDSUB", "SPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "KEYWORD", "NUMBER", "ID", "TEXT", 
                  "MULTDIV", "ADDSUB", "SPACE" ]

    grammarFileName = "qs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


