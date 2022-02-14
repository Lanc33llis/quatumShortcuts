# Generated from qs.g4 by ANTLR 4.9.3
from antlr4 import *
from units import *

from commands import commands
if __name__ is not None and "." in __name__:
  from .qsParser import qsParser
else:
  from qsParser import qsParser

# This class defines a complete listener for a parse tree produced by qsParser.


class qsListener(ParseTreeListener):
  def __init__(self):
    super().__init__()
    self.val = None
    self.stack = []

# Enter a parse tree produced by qsParser#parse.
  def enterParse(self, ctx: qsParser.ParseContext):
    self.stack.append([])

# Exit a parse tree produced by qsParser#parse.
  def exitParse(self, ctx: qsParser.ParseContext):
    types = {}
    usingKey = {
      "meters": usingMeters,
      "watts": usingWatts,
    }

    for ctx in self.stack:
      for unit in ctx:
        if unit.unitName in types:
          types[unit.unitName] += unit.raw
        else:
          types[unit.unitName] = unit.raw

    self.val = ""
    for unit in types:
      self.val += f"{usingKey[unit](types[unit]) if unit is not None else types[unit]} "

# Enter a parse tree produced by qsParser#expression.
  def enterExpression(self, ctx: qsParser.ExpressionContext):
    pass

# Exit a parse tree produced by qsParser#expression.
  # undoubtedly this will be a mess to debug in the future, but it works for now
  def exitExpression(self, ctx: qsParser.ExpressionContext):
    if ctx.MULTDIV() or ctx.ADDSUB():
      operatorCtx = ctx.MULTDIV() or ctx.ADDSUB()
      operator = operatorCtx.getText()
      right, left = self.stack[-1].pop(), self.stack[-1].pop()
      if operator == "*":
        result = left * right
      elif operator == "/":
        result = left / right
      if operator == "+":
        result = left + right
      elif operator == "-":
        result = left - right
      self.stack[-1] += [result] if not isinstance(result, list) else result
  # Enter a parse tree produced by qsParser#unit.
  def enterUnit(self, ctx: qsParser.UnitContext):
    pass

  # Exit a parse tree produced by qsParser#unit.
  def exitUnit(self, ctx: qsParser.UnitContext):
    self.stack[-1].append(unit(float(ctx.NUMBER().getText()), ctx.ID().getText() if ctx.ID() else None, getUnitName(ctx.ID().getText()) if ctx.ID() else None))

  # Enter a parse tree produced by qsParser#function.
  def enterFunction(self, ctx: qsParser.FunctionContext):
    self.stack.append([])

  # Exit a parse tree produced by qsParser#function.
  def exitFunction(self, ctx: qsParser.FunctionContext):
    funcName = ctx.ID().getText()
    if funcName in commands:
      result = commands[funcName](*self.stack.pop())
    self.stack[-1].append(result)


  # Enter a parse tree produced by qsParser#arguments.
  def enterArguments(self, ctx: qsParser.ArgumentsContext):
    pass

  # Exit a parse tree produced by qsParser#arguments.
  def exitArguments(self, ctx: qsParser.ArgumentsContext):
    pass

del qsParser
