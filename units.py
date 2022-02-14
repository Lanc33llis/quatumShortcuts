class unit:
  def __init__(self, num: float, unitType: str, unitName: str):
    self.num = num
    self.unitType = unitType
    self.raw = num * units[unitType] if unitType else num
    self.unitName = unitName
  def __str__(self):
    return f"{self.num}{self.unitType if self.unitType != None else ''}"
  def absStr(self):
    return f"{abs(self.num)}{self.unitType if self.unitType != None else ''}"
  def __add__(self, other):
    if self.unitName != other.unitName:
      return [self, other]
    if self.unitType in meters:
      return usingMeters(self.raw + other.raw)
    elif self.unitType == None:
      return unit(self.num + other.num, None, None)
    else:
      return [self, other]
  def __sub__(self, other):
    if self.unitName != other.unitName:
      return [self, other]
    if self.unitType in meters:
      return usingMeters(self.raw - other.raw)
    elif self.unitType == None:
      return unit(self.num - other.num, None, None)
    else:
      return [self, other]
  def __mul__(self, other):
    if self.unitName != other.unitName:
      return [self, other]
    if self.unitType in meters:
      return usingMeters(self.raw * other.raw)
    elif self.unitType == None:
      return unit(self.num * other.num, None, None)
    else:
      return [self, other]
  def __truediv__(self, other):
    if self.unitName != other.unitName:
      return [self, other]
    if self.unitType in meters:
      return usingMeters(self.raw / other.raw)
    elif self.unitType == None:
      return unit(self.num / other.num, None, None)
    else:
      return [self, other]

def unitBuilder(key, unitName):
  def built(num):
    if num == 0:
      return unit(0, key[1], unitName)
    t = abs(num)
    if t >= 1:
      return unit(num, key[1], unitName)
    for k, v in key.items():
      if t > k:
        return unit(num/k, v, unitName)
  return built

usingMeters = unitBuilder({
    1: 'm',
    .1: 'dm',
    0.01: 'cm',
    0.001: 'mm',
    1e-6: 'um',
  }, 
  "meters"
)

def getUnitName(unit: str):
  if unit in meters:
    return "meters"

meters = {
  'm': 1,
  'dm': .1,
  'cm': 0.01,
  'mm': 0.001,
  'µm': 1e-6,
}
  
units = {
  **meters,
}
