import sys
from optics import commands as optics
from units import *

def hello():
  return "Hello, world!"

def exit():
  sys.exit(0)

def func1(x , y):
  return x + y

def func2(x):
  return usingMeters(x * 2)


commands = { "hello": hello, "exit": exit, **optics, "func1": func1, "func2": func2 }