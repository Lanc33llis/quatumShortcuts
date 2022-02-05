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
	
	def push(self, e):
		self.stack.append(e)
	
	def pop(self, i=0):
		self.stack.pop(i)

	def stackLength(self):
		return len(self.stack)

	# Enter a parse tree produced by qsParser#parse.
	def enterParse(self, ctx: qsParser.ParseContext):
		pass

	# Exit a parse tree produced by qsParser#parse.
	def exitParse(self, ctx: qsParser.ParseContext):
		pass

	# Enter a parse tree produced by qsParser#expression.
	def enterExpression(self, ctx: qsParser.ExpressionContext):
		print(ctx.getText())
		pass

	# Exit a parse tree produced by qsParser#expression.
	def exitExpression(self, ctx: qsParser.ExpressionContext):
		# print(self.stack)
		if ctx.NUMBER() is not None:
			self.push(float(ctx.NUMBER().getText()))
		if ctx.MULTDIV() is not None or ctx.ADDSUB() is not None:
			operator = (ctx.MULTDIV() or ctx.ADDSUB()).getText()
			val =0
			if operator == '+':
				val = sum(self.stack)
			elif operator == '-':
				val = self.stack[0] - sum(self.stack[1:])
			elif operator == '*':
				val = 1
				for i in self.stack:
					val *= i
			elif operator == '/':
				val = self.stack[0] / sum(self.stack[1:])
			else:
				raise Exception(f'Unknown operator: {operator}')
			self.stack.clear()
			self.push(val)
		pass

	# Enter a parse tree produced by qsParser#unit.
	def enterUnit(self, ctx: qsParser.UnitContext):
		pass

	# Exit a parse tree produced by qsParser#unit.
	def exitUnit(self, ctx: qsParser.UnitContext):
		unit = ctx.ID().getText()
		if unit not in units:
			raise Exception(f'Unknown unit: {unit}')
		else:
			self.push(float(ctx.NUMBER().getText()) * units[unit])
		pass

	# Enter a parse tree produced by qsParser#function.
	def enterFunction(self, ctx: qsParser.FunctionContext):
		pass

	# Exit a parse tree produced by qsParser#function.
	def exitFunction(self, ctx: qsParser.FunctionContext):
		funcName = ctx.ID().getText()
		if funcName  not in commands:
			raise Exception(f'Unknown command: {funcName}')
		else:
			val = commands[funcName](*self.stack)
			self.stack.clear()
			self.push(val)

	# Enter a parse tree produced by qsParser#arguments.
	def enterArguments(self, ctx: qsParser.ArgumentsContext):
		pass

	# Exit a parse tree produced by qsParser#arguments.
	def exitArguments(self, ctx: qsParser.ArgumentsContext):
		pass

	def enterPrecedence(self, ctx: qsParser.PrecedenceContext):
		pass

	def exitPrecedence(self, ctx: qsParser.PrecedenceContext):
		pass

del qsParser
