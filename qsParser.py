# Generated from qs.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'\13")
        buf.write("\3\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\5\5\61\n\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\7\68\n\6\f\6\16\6;\13\6\3\6\2\3\4\7\2\4\6")
        buf.write("\b\n\2\2\2A\2\f\3\2\2\2\4\30\3\2\2\2\6+\3\2\2\2\b-\3\2")
        buf.write("\2\2\n\64\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2")
        buf.write("\2\17\20\b\3\1\2\20\31\5\b\5\2\21\22\7\3\2\2\22\23\5\4")
        buf.write("\3\2\23\24\7\4\2\2\24\31\3\2\2\2\25\31\5\6\4\2\26\31\7")
        buf.write("\t\2\2\27\31\7\b\2\2\30\17\3\2\2\2\30\21\3\2\2\2\30\25")
        buf.write("\3\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2\31%\3\2\2\2\32\33")
        buf.write("\f\t\2\2\33\34\7\n\2\2\34$\5\4\3\n\35\36\f\b\2\2\36\37")
        buf.write("\7\13\2\2\37$\5\4\3\t !\f\7\2\2!\"\7\6\2\2\"$\5\4\3\b")
        buf.write("#\32\3\2\2\2#\35\3\2\2\2# \3\2\2\2$\'\3\2\2\2%#\3\2\2")
        buf.write("\2%&\3\2\2\2&\5\3\2\2\2\'%\3\2\2\2()\7\7\2\2),\7\b\2\2")
        buf.write("*,\7\7\2\2+(\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-.\7\b\2\2.\60")
        buf.write("\7\3\2\2/\61\5\n\6\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3")
        buf.write("\2\2\2\62\63\7\4\2\2\63\t\3\2\2\2\649\5\4\3\2\65\66\7")
        buf.write("\5\2\2\668\5\4\3\2\67\65\3\2\2\28;\3\2\2\29\67\3\2\2\2")
        buf.write("9:\3\2\2\2:\13\3\2\2\2;9\3\2\2\2\b\30#%+\609")
        return buf.getvalue()


class qsParser ( Parser ):

    grammarFileName = "qs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "KEYWORD", "NUMBER", "ID", "TEXT", "MULTDIV", "ADDSUB", 
                      "SPACE" ]

    RULE_parse = 0
    RULE_expression = 1
    RULE_unit = 2
    RULE_function = 3
    RULE_arguments = 4

    ruleNames =  [ "parse", "expression", "unit", "function", "arguments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    KEYWORD=4
    NUMBER=5
    ID=6
    TEXT=7
    MULTDIV=8
    ADDSUB=9
    SPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(qsParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(qsParser.EOF, 0)

        def getRuleIndex(self):
            return qsParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = qsParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
            self.state = 11
            self.match(qsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(qsParser.FunctionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(qsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(qsParser.ExpressionContext,i)


        def unit(self):
            return self.getTypedRuleContext(qsParser.UnitContext,0)


        def TEXT(self):
            return self.getToken(qsParser.TEXT, 0)

        def ID(self):
            return self.getToken(qsParser.ID, 0)

        def MULTDIV(self):
            return self.getToken(qsParser.MULTDIV, 0)

        def ADDSUB(self):
            return self.getToken(qsParser.ADDSUB, 0)

        def KEYWORD(self):
            return self.getToken(qsParser.KEYWORD, 0)

        def getRuleIndex(self):
            return qsParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = qsParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 14
                self.function()
                pass

            elif la_ == 2:
                self.state = 15
                self.match(qsParser.T__0)
                self.state = 16
                self.expression(0)
                self.state = 17
                self.match(qsParser.T__1)
                pass

            elif la_ == 3:
                self.state = 19
                self.unit()
                pass

            elif la_ == 4:
                self.state = 20
                self.match(qsParser.TEXT)
                pass

            elif la_ == 5:
                self.state = 21
                self.match(qsParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = qsParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 24
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 25
                        self.match(qsParser.MULTDIV)
                        self.state = 26
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = qsParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 27
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 28
                        self.match(qsParser.ADDSUB)
                        self.state = 29
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = qsParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        self.match(qsParser.KEYWORD)
                        self.state = 32
                        self.expression(6)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(qsParser.NUMBER, 0)

        def ID(self):
            return self.getToken(qsParser.ID, 0)

        def getRuleIndex(self):
            return qsParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = qsParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unit)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(qsParser.NUMBER)
                self.state = 39
                self.match(qsParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(qsParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(qsParser.ID, 0)

        def arguments(self):
            return self.getTypedRuleContext(qsParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return qsParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = qsParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(qsParser.ID)
            self.state = 44
            self.match(qsParser.T__0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << qsParser.T__0) | (1 << qsParser.NUMBER) | (1 << qsParser.ID) | (1 << qsParser.TEXT))) != 0):
                self.state = 45
                self.arguments()


            self.state = 48
            self.match(qsParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(qsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(qsParser.ExpressionContext,i)


        def getRuleIndex(self):
            return qsParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = qsParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.expression(0)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==qsParser.T__2:
                self.state = 51
                self.match(qsParser.T__2)
                self.state = 52
                self.expression(0)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




