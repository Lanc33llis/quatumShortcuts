from halo import Halo
from commands import execCommand

spinner = Halo(spinner="dots", color="white")

def main():
  while True:
    print(">", end=" ")
    command = input()

    if command == "":
      continue
    with spinner:
      result = execCommand(command)
    print(f">> {result}")
main()