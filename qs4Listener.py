# Generated from qs.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
	from .qsParser import qsParser
else:
	from qsParser import qsParser

import inspect

from util.unit import *
from funcs.functions import functions
from vars.var import *

# This class defines a complete listener for a parse tree produced by qsParser.
class qsListener(ParseTreeListener):
	def __init__(self):
		super().__init__()
		self.val = None
		self.stack = []

	# Enter a parse tree produced by qsParser#parse.
	def enterParse(self, ctx:qsParser.ParseContext):
		pass

	# Exit a parse tree produced by qsParser#parse.
	def exitParse(self, ctx:qsParser.ParseContext):
		self.val = self.stack.pop()

	# Enter a parse tree produced by qsParser#expression.
	def enterExpression(self, ctx:qsParser.ExpressionContext):
		pass

	# Exit a parse tree produced by qsParser#expression.
	def exitExpression(self, ctx:qsParser.ExpressionContext):
		if ctx.TEXT():
			self.stack.append(ctx.TEXT().getText().strip("'"))

		elif ctx.ID():
			if UserDefinedVars.has(ctx.ID().getText()):
				self.stack.append(UserDefinedVars.get(ctx.ID().getText()))
			else:
				self.stack.append(ctx.ID().getText())

		elif ctx.KEYWORD():
			keyword = ctx.KEYWORD().getText()
			if keyword == "=":
				val = self.stack.pop()
				name = self.stack.pop()
				self.stack.append(UserDefinedVars.put(name, val))
			elif keyword == "to":
				dstUnit = self.stack.pop()
				srcUnit = self.stack.pop()
				self.stack.append(srcUnit.to(dstUnit))

		elif ctx.MULTDIV():
			right = self.stack.pop()
			left = self.stack.pop()
			operator = ctx.MULTDIV().getText()
			if operator == "*":
				result = left * right
			elif operator == "/":
				result = left / right
			self.stack.append(result)
		elif ctx.ADDSUB():
			right = self.stack.pop()
			left = self.stack.pop()
			operator = ctx.ADDSUB().getText()
			if operator == "+":
				result = left + right
			elif operator == "-":
				result = left - right
			self.stack.append(result)	

	# Enter a parse tree produced by qsParser#unit.
	def enterUnit(self, ctx:qsParser.UnitContext):
		pass

	# Exit a parse tree produced by qsParser#unit.
	def exitUnit(self, ctx:qsParser.UnitContext):
		val = float(ctx.NUMBER().getText())
		unit = ctx.ID().getText() if ctx.ID() else None
		self.stack.append(Unit(val, unit))

	# Enter a parse tree produced by qsParser#function.
	def enterFunction(self, ctx:qsParser.FunctionContext):
		pass

	# Exit a parse tree produced by qsParser#function.
	def exitFunction(self, ctx:qsParser.FunctionContext):
		funcName = ctx.ID().getText()
		if funcName in functions:
			func = functions[funcName]
			lenArgs = len(inspect.getfullargspec(func).args)
			varArgs = inspect.getfullargspec(func).varargs
			if lenArgs == 0:
				self.stack.append(func())
			else:
				args = self.stack.pop()
				if len(args) != lenArgs and not varArgs:
					raise Exception(f"Function {funcName} expects {len(func.args)} arguments, but got {len(args)}")
				if varArgs:
					self.stack.append(func(*args[:lenArgs], *args[lenArgs:]))
				else:
					self.stack.append(func(*args))


	# Enter a parse tree produced by qsParser#arguments.
	def enterArguments(self, ctx:qsParser.ArgumentsContext):
		pass

# Exit a parse tree produced by qsParser#arguments.
	def exitArguments(self, ctx:qsParser.ArgumentsContext):
		args = []
		for i in range(len(ctx.expression())):
			e = self.stack.pop()
			args.append(e.raw if isinstance(e, Unit) else e)
		args.reverse()
		self.stack.append(args)

del qsParser