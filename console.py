from halo import Halo
from commands import commands
import time

spinner = Halo(spinner="dots", color="white")

def syntaxCheck(s: str):
  s = s.strip()
  leftParen = s.find("(")
  rightParen = s.find(")")
  if leftParen == -1 or rightParen == -1:
    return False, None
  if leftParen > rightParen:
    return False, None
  name = s[:leftParen]
  argsStr = s[leftParen + 1 : rightParen]
  args = argsStr.split(",")
  for i, arg in enumerate(args):
    arg = arg.strip()
    try:
      arg = int(arg)
    except ValueError:
      pass
    try:
      arg = float(arg)
    except ValueError:
      pass
    args[i] = arg
  return name, args

def main():
  while True:
    print(">", end=" ")
    command = input()

    if command == "":
      continue
  
    commandName, args = syntaxCheck(command)

    if commandName is False:
      print(">> Invalid syntax")
      continue

    if commandName in commands:
      try:
        with spinner:
          results = ""
          if args[0] == "":
            results = commands[commandName]()
          else:
            results = commands[commandName](*args)
      except Exception as e:
        print(f'>> Error: {e}')
        continue
      print(f'>> {command}: {results}')
    else:
      print(">> Unknown command")
main()