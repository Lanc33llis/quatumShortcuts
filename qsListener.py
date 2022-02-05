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
		val = 0
		for i in self.stack:
			val += i[0]
		self.val = val

	# Enter a parse tree produced by qsParser#expression.
	def enterExpression(self, ctx: qsParser.ExpressionContext):
		if ctx.NUMBER() is None and ctx.ID() is None and ctx.function() is None and ctx.TEXT() is None \
		and ctx.unit() is None and ctx.ID() is None and ctx.ADDSUB() is None and ctx.MULTDIV() is None \
		and ctx.expression() is not None:
			self.stack.append([])
			return
		pass

	# Exit a parse tree produced by qsParser#expression.
	def exitExpression(self, ctx: qsParser.ExpressionContext):
		print(ctx.getText(), self.stack)
		if ctx.NUMBER() is not None:
			self.stack[-1].append(float(ctx.NUMBER().getText()))
		if ctx.MULTDIV() is not None or ctx.ADDSUB() is not None:
			operator = (ctx.MULTDIV() or ctx.ADDSUB()).getText()
			val = 0
			if len(self.stack) > 1 and len(self.stack[-1]) == 1:
				if operator == '+':
					val = self.stack[-2][0] + self.stack[-1][0]
				elif operator == '-':
					val = self.stack[-2][0] - self.stack[-1][0]
				elif operator == '*':
					val = 1
					for i in self.stack:
						val *= i[0]
				elif operator == '/':
					val = self.stack[-2][0] / self.stack[-2][0]
				else:
					raise Exception(f'Unknown operator: {operator}')
			else:
				if operator == '+':
					val = sum(self.stack[-1])
				elif operator == '-':
					val = self.stack[-1][0] - sum(self.stack[-1][1:])
				elif operator == '*':
					val = 1
					for i in self.stack[-1]:
						val *= i
				elif operator == '/':
					val = self.stack[-1][0] / sum(self.stack[-1][1:])
				else:
					raise Exception(f'Unknown operator: {operator}')
				self.stack[-1].clear()
				self.stack[-1].append(val)

	# Enter a parse tree produced by qsParser#unit.
	def enterUnit(self, ctx: qsParser.UnitContext):
		pass

	# Exit a parse tree produced by qsParser#unit.
	def exitUnit(self, ctx: qsParser.UnitContext):
		unit = ctx.ID().getText()
		if unit not in units:
			raise Exception(f'Unknown unit: {unit}')
		else:
			self.stack[-1].append(float(ctx.NUMBER().getText()) * units[unit])
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
			val = commands[funcName](*self.stack[-1])
			self.stack[-1].clear()
			self.stack[-1].append(val)

	# Enter a parse tree produced by qsParser#arguments.
	def enterArguments(self, ctx: qsParser.ArgumentsContext):
		pass

	# Exit a parse tree produced by qsParser#arguments.
	def exitArguments(self, ctx: qsParser.ArgumentsContext):
		pass

del qsParser
