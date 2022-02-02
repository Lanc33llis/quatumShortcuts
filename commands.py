import sys
from optics import commands as optics

def hello():
  return "Hello, world!"

def exit():
  sys.exit(0)

commands = {"hello": hello, "exit": exit, **optics}