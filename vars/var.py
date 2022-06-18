from typing import Union
from util.unit import *

class Var(Unit):
  def __init__(self, varName: str, val: Union[int, float], unit: str):
    super().__init__(val, unit)
    self.name = varName

class VarManager:
  def __init__(self, vars: dict = {}):
    self.vars = vars

  def put(self, varName: str, val):
    if isinstance(varName, Var):
      varName = varName.name
    if isinstance(val, str):
      self.vars[varName] = val
    else:
      self.vars[varName] = Var(varName, val.raw, val.subUnit)
    return val

  def get(self, varName: str):
    return self.vars[varName]

  def rm(self, varName: str):
    del self.vars[varName]

  def has(self, varName: str):
    return varName in self.vars

UserDefinedVars = VarManager()