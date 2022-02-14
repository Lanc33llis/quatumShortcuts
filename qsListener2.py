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
      self.val = f'{unitCtx.NUMBER().getText()}{unitCtx.ID().getText()}'
    else:
      unitKey = {
      }
      unitFunctions = {
        "units": lambda x: unit(x, None, None),
        "meters": usingMeters,
      }
      for i in self.stack:
        for e in i:
          if isinstance(e, unit):
            raw, unitType, unitName = e.raw, e.unitType, e.unitName
            if unitName == None or unitName == '':
              unitKey["units"] += (raw)
            elif unitType in units:
              if not hasattr(unitKey, unitName):
                unitKey[unitName] = raw
              else:
                unitKey[unitName] += (raw)
          else:
            if not hasattr(unitKey, "units"):
              unitKey["units"] = float(e)
            else:
              unitKey["units"] += (float(e))

      s = ""
      for key, value in unitKey.items():
        result = unitFunctions[key](value)
        if result.raw == 0:
          continue
        if len(s) == 0:
          s += f'{result}'
        else:
          raw = result.raw if isinstance(result, unit) else result
          if raw < 0:
            s += f' - {result.absStr() if isinstance(result, unit) else abs(result)}'
          else:
            s += f' + {result}'
      if s == "":
        s = "0"
        # print(unitFunctions[key](value))
      self.val = s
      # metersSum = []
      # for i in self.stack:
      #   there = re.compile(r'\s*([\-]?\d+.?\d+)\s*([a-zA-Z]*)')
      #   thematch = there.match(i[0])
      #   if thematch:
      #     number, unit = thematch.gr6oups()
      #     if unit in units:
      #       if unit in meters:
      #         metersSum.append(float(number) * units[unit])
      # self.val = usingMeters(sum(metersSum))

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
  # undoubtedly this will be a mess to debug in the future, but it works for now
  def exitExpression(self, ctx: qsParser.ExpressionContext):
    if ctx.MULTDIV() or ctx.ADDSUB():
      leftCtx, left = ctx.expression(0), 0
      if leftCtx.MULTDIV() or leftCtx.ADDSUB():
        # left = self.stack[-1][0]
        # self.stack[-1].clear()
        left = self.stack.pop()[0]
      elif leftCtx.unit():
        unitCtx = leftCtx.unit()
        left = unit(float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()], unitCtx.ID().getText(), getUnitName(unitCtx.ID().getText()))
      else:
        if leftCtx.NUMBER():
          left = float(leftCtx.NUMBER().getText())
        else:
          # left = self.stack.pop(0)[0]
          left = self.stack[-1].pop(0)
          # if isinstance(left, unit):
          #   left = left.raw
      rightCtx, right = ctx.expression(1), 0
      if rightCtx.MULTDIV() or rightCtx.ADDSUB():
        right = self.stack[-1][-1]
        self.stack[-1].clear()
      elif rightCtx.unit():
        unitCtx = rightCtx.unit()
        right = unit(float(unitCtx.NUMBER().getText()) * units[unitCtx.ID().getText()], unitCtx.ID().getText(), getUnitName(unitCtx.ID().getText()))
      else:
        if rightCtx.NUMBER():
          right = float(rightCtx.NUMBER().getText())
        else:
          right = self.stack[-1].pop(0)
          # if isinstance(right, unit):
          #   right = right.raw
      operatorExpr = ctx.MULTDIV() or ctx.ADDSUB()
      operator = operatorExpr.getText()
      if len(self.stack) == 0:
        self.stack.append([])
      if isinstance(left, unit) and isinstance(right, unit) and left.unitType == right.unitType:
        if operator == '*':
          self.stack[-1].append(unit(left.raw * right.raw, left.unitType, left.unitName))
        elif operator == "/":
          self.stack[-1].append(unit(left.raw / right.raw, left.unitType, left.unitName))
        elif operator == "+":
          self.stack[-1].append(unit(left.raw + right.raw, left.unitType, left.unitName))
        elif operator == "-":
          self.stack[-1].append(unit(left.raw - right.raw, left.unitType, left.unitName))
      elif isinstance(left, float) and isinstance(right, float):
        if operator == '*':
          self.stack[-1].append(left * right)
        elif operator == "/":
          self.stack[-1].append(left / right)
        elif operator == "+":
          self.stack[-1].append(left + right)
        elif operator == "-":
          self.stack[-1].append(left - right)
      else:
        self.stack[-1] += [left, right if operator == '+' else right if isinstance(right, unit) else -right]

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
    argCtx = ctx.arguments()
    if argCtx:
      for arg in argCtx.expression():
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
    numArgs = len(argCtx.expression()) if argCtx else 0
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
