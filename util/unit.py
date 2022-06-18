from typing import Union
from util.units import units as unprocessedUnits
from functools import reduce

def unitBuilder(units):
  key = {v: k for k, v in units.items()}
  
  def unitFunc(num: Union[int, float]):
    if num == 0:
      return 0, key[1]
    t = abs(num)
    for k, v in key.items():
      if t >= k:
        return num / k, v
  
  return unitFunc

def build():
  units = reduce(lambda a, b: {**a, **b}, unprocessedUnits.values(), {None: 1, '': 1})

  unitToBase = {None: None, '': None} 
  unitFuncs = {None: lambda n: (n, '')}
  for baseName, subUnits in unprocessedUnits.items():
    unitToBase = {**unitToBase, **{k: baseName for k, v in subUnits.items()}}
    unitFuncs[baseName] = unitBuilder(subUnits) 

  return units, unitToBase, unitFuncs

units, unitToBase, unitFuncs = build()

def getBaseUnit(unit):
  return unitToBase[unit]

class Unit:
  def __init__(self, num: Union[int, float], unit: str):
    self.raw = num * units[unit]
    self.baseUnit = getBaseUnit(unit)
    self.num, self.subUnit = unitFuncs[self.baseUnit](self.raw)

  def to(self, type: str):
    return f"{self.raw / units[type]}{type}"

  #just trying to get the base unit in its abv. form, this is expensive ftm
  def __add__(self, other):
    baseUnit = self.baseUnit or other.baseUnit
    return Unit(self.raw + other.raw, unitFuncs[baseUnit](1)[1])
  def __sub__(self, other):
    baseUnit = self.baseUnit or other.baseUnit
    return Unit(self.raw - other.raw, unitFuncs[baseUnit](1)[1])
  def __mul__(self, other):
    baseUnit = self.baseUnit or other.baseUnit
    return Unit(self.raw * other.raw, unitFuncs[baseUnit](1)[1])
  def __truediv__(self, other):
    baseUnit = self.baseUnit or other.baseUnit
    return Unit(self.raw / other.raw, unitFuncs[baseUnit](1)[1])
  def __str__(self):
    return f"{self.num}{self.subUnit}"
