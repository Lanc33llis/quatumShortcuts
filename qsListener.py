# Generated from qs.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .qsParser import qsParser
else:
    from qsParser import qsParser

# This class defines a complete listener for a parse tree produced by qsParser.
class qsListener(ParseTreeListener):

    # Enter a parse tree produced by qsParser#parse.
    def enterParse(self, ctx:qsParser.ParseContext):
        pass

    # Exit a parse tree produced by qsParser#parse.
    def exitParse(self, ctx:qsParser.ParseContext):
        pass


    # Enter a parse tree produced by qsParser#expression.
    def enterExpression(self, ctx:qsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by qsParser#expression.
    def exitExpression(self, ctx:qsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by qsParser#unit.
    def enterUnit(self, ctx:qsParser.UnitContext):
        pass

    # Exit a parse tree produced by qsParser#unit.
    def exitUnit(self, ctx:qsParser.UnitContext):
        pass


    # Enter a parse tree produced by qsParser#function.
    def enterFunction(self, ctx:qsParser.FunctionContext):
        pass

    # Exit a parse tree produced by qsParser#function.
    def exitFunction(self, ctx:qsParser.FunctionContext):
        pass


    # Enter a parse tree produced by qsParser#arguments.
    def enterArguments(self, ctx:qsParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by qsParser#arguments.
    def exitArguments(self, ctx:qsParser.ArgumentsContext):
        pass



del qsParser