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
    for k, v in key.items():
      if t >= k:
        return unit(num/k, v, unitName)
  return built

meters = {
  'Ym': 1e24,
  'Zm': 1e21,
  'Em': 1e18,
  'Pm': 1e15,
  'Tm': 1e12,
  'Gm': 1e9,
  'Mm': 1e6,
  'km': 1e3,
  'hm': 1e2,
  'dam': 1e1,
  'm': 1,
  'dm': 1e-1,
  'cm': 1e-2,
  'mm': 1e-3,
  'µm': 1e-6,
  'nm': 1e-9,
  'pm': 1e-12,
  'fm': 1e-15,
  'am': 1e-18,
  'zm': 1e-21,
  'ym': 1e-24,
}
usingMeters = unitBuilder(dict((v,k) for k,v in meters.items()), "meters")

watts = {
  'YW': 1e24,
  'ZW': 1e21,
  'EW': 1e18,
  'PW': 1e15,
  'TW': 1e12,
  'GW': 1e9,
  'MW': 1e6,
  'kW': 1e3,
  'hW': 1e2,
  'daW': 1e1,
  'W': 1,
  'dW': 1e-1,
  'cW': 1e-2,
  'mW': 1e-3,
  'µW': 1e-6,
  'nW': 1e-9,
  'pW': 1e-12,
  'fW': 1e-15,
  'aW': 1e-18,
  'zW': 1e-21,
  'yW': 1e-24,
}
usingWatts = unitBuilder(dict((v,k) for k,v in watts.items()), "watts")


def getUnitName(unit: str):
  if unit in meters:
    return "meters"
  elif unit in watts:
    return "watts"
  
units = {
  **meters,
  **watts,
}
