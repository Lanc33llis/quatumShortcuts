# Generated from qs.g4 by ANTLR 4.9.3
from antlr4 import *
from units import units
from commands import commands
if __name__ is not None and "." in __name__:
  from .qsParser import qsParser
else:
  from qsParser import qsParser

# This class defines a complete listener for a parse tree produced by qsParser.


class qsListener(ParseTreeListener):
  def __init__(self):
    super().__init__()
    self.val = 0.0
    self.stack = []

# Enter a parse tree produced by qsParser#parse.
  def enterParse(self, ctx: qsParser.ParseContext):
    self.stack.append([])

# Exit a parse tree produced by qsParser#parse.
  def exitParse(self, ctx: qsParser.ParseContext):
    if ctx.expression().NUMBER():
      self.val = float(ctx.expression().NUMBER().getText())
    elif ctx.expression().unit():
      unitCtx = ctx.expression().unit()
      self.val = float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()]
    else:
      val = 0
      for i in self.stack:
        val += i[0]
      self.val = val

# Enter a parse tree produced by qsParser#expression.
  def enterExpression(self, ctx: qsParser.ExpressionContext):
    if ctx.NUMBER() is None and ctx.ID() is None and ctx.function() is None and ctx.TEXT() is None \
    and ctx.unit() is None and ctx.ID() is None and ctx.ADDSUB() is None and ctx.MULTDIV() is None \
    and ctx.expression() and len(self.stack[0]) != 0:
      if ctx.expression(0).NUMBER():
        self.stack.append([float(ctx.expression(0).NUMBER().getText())])
      elif ctx.expression(0).unit():
        unitCtx = ctx.expression(0).unit()
        self.stack.append([float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()]])
      else:
        self.stack.append([])

# Exit a parse tree produced by qsParser#expression.
  def exitExpression(self, ctx: qsParser.ExpressionContext):
    if ctx.MULTDIV() or ctx.ADDSUB():
      leftCtx, left = ctx.expression(0), 0
      if leftCtx.MULTDIV() or leftCtx.ADDSUB():
        # left = self.stack[-1][0]
        # self.stack[-1].clear()
        left = self.stack.pop()[0]
      elif leftCtx.unit():
        unitCtx = leftCtx.unit()
        left = float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()]
      else:
        if leftCtx.NUMBER():
          left = float(leftCtx.NUMBER().getText())
        else:
          # left = self.stack.pop(0)[0]
          left = self.stack[-1].pop(0)
      rightCtx, right = ctx.expression(1), 0
      if rightCtx.MULTDIV() or rightCtx.ADDSUB():
        right = self.stack[-1][-1]
        self.stack[-1].clear()
      elif rightCtx.unit():
        unitCtx = rightCtx.unit()
        right = float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()]
      else:
        if rightCtx.NUMBER():
          right = float(rightCtx.NUMBER().getText())
        else:
          right = self.stack[-1].pop(0)
      operatorExpr = ctx.MULTDIV() or ctx.ADDSUB()
      operator = operatorExpr.getText()
      if len(self.stack) == 0:
        self.stack.append([])
      if operator == '*':
        self.stack[-1].append(left * right)
      elif operator == "/":
        self.stack[-1].append(left / right)
      elif operator == "+":
        self.stack[-1].append(left + right)
      elif operator == "-":
        self.stack[-1].append(left - right)

  # Enter a parse tree produced by qsParser#unit.
  def enterUnit(self, ctx: qsParser.UnitContext):
    pass

  # Exit a parse tree produced by qsParser#unit.
  def exitUnit(self, ctx: qsParser.UnitContext):
    pass

  # Enter a parse tree produced by qsParser#function.
  def enterFunction(self, ctx: qsParser.FunctionContext):
    pass

  # Exit a parse tree produced by qsParser#function.
  def exitFunction(self, ctx: qsParser.FunctionContext):
    if ctx.arguments():
      for arg in ctx.arguments().expression():
        if arg.NUMBER():
          self.stack[-1].append(float(arg.NUMBER().getText()))
        elif arg.unit():
          unitCtx = arg.unit()
          self.stack[-1].append(float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()])
        elif len(arg.expression()) == 1:
          t = self.stack.pop()
          if (len(self.stack) == 0):
            self.stack.append([])
          self.stack[-1].append(t[0])
    funcName = ctx.ID().getText()
    numArgs = len(ctx.arguments().expression())
    if funcName  not in commands:
      raise Exception(f'Unknown command: {funcName}')
    else:
      val = commands[funcName](*self.stack[-1][-numArgs:])
      self.stack[-1] = self.stack[-1][:-numArgs]
      self.stack[-1].append(val)

  # Enter a parse tree produced by qsParser#arguments.
  def enterArguments(self, ctx: qsParser.ArgumentsContext):
    pass

  # Exit a parse tree produced by qsParser#arguments.
  def exitArguments(self, ctx: qsParser.ArgumentsContext):
    pass

del qsParser
