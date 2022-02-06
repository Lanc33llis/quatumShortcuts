class unit:
  def __init__(self, num: float, unitType: str, unitName: str):
    self.num = num
    self.unitType = unitType
    self.raw = num * units[unitType] if unitType else num
    self.unitName = unitName
  def __str__(self):
    return f"{self.num}{self.unitType if self.unitType != None else ''}"

def usingMeters(num):
  key = {
    1: 'm',
    .1: 'dm',
    0.01: 'cm',
    0.001: 'mm',
    1e-6: 'um',
  }
  t = abs(num)
  if t >= 1:
    return unit(num, "m", "meters")
  for k, v in key.items():
    if t > k:
      return unit(num, v, "meters")

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
