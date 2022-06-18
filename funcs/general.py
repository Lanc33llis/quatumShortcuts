import sys


def hello():
  return "Hello, world!"

def help():
  return '''
    qs is a programming language. It's built to be scientific and easy.
    hello() - Prints "Hello, world!"
    exit() - Exits the program
    malusLaw(intensity, theta) - Returns the intensity of a polarized beam at a given angle
    botpKeyGen(length) - Returns a random binary string of a given length
    botp(key, message) - Returns the XOR of a key and message
  '''
def exit():
  sys.exit(0)

def print(s: str, *args):
  for i in args:
    if isinstance(i, str):
      s = s.replace("%s", i, 1)
    elif isinstance(i, int):
      s = s.replace("%d", str(i), 1)
    elif isinstance(i, float):
      s = s.replace("%f", str(i), 1)
    else:
      s = s.replace("%s", str(i), 1)
  return s

funcs = { "hello": hello, "exit": exit, "print": print, "help": help }