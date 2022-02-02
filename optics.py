import math

def PBS(basis: str, intensity: float, polarization: str):
  try:
    intensity = float(intensity)
  except ValueError:
    return f"Invalid intensity: {intensity}"
  modes = ["H", "V", "D", "A"]
  if polarization not in modes:
    return f"Invalid polarization: {polarization}"
  if basis not in ["+", "X"]:
    return f"Invalid basis: {basis}"
  b, p = basis, polarization
  if b == "+":
    if p == "H":
      return (intensity, 0)
    elif p == "V":
      return (0, intensity)
    else:
      return (intensity / 2, intensity / 2)
  else:
    if p == "D":
      return (intensity, 0)
    elif p == "A":
      return (0, intensity)
    else:
      return (intensity / 2, intensity / 2)

def malusLaw(intensity: float, theta: float):
  return intensity * math.cos( theta )**2

commands = { "PBS": PBS, "malusLaw": malusLaw }