import math

def map_hours(hours) -> int:
    return math.ceil(hours)

def ratio(e_to_r) -> int:
    return math.ceil(e_to_r * 100)

def gender(sex) -> int:
    if sex.lower() == 'male':
        return 0
    elif sex.lower() == 'female':
        return 1
    else:
        return -1

def map_device(device):
    if device.lower() == 'smartphone':
        return 0
    elif device.lower() == 'laptop':
        return 1
    elif device.lower() == 'tv':
        return 2
    elif device.lower() == 'tablet':
        return 3
    else:
        return 4
    
def place(city) -> int:
    if city.lower() == 'urban':
        return 0
    elif city.lower() == 'rural':
        return 1

def map_impact(impact:str) -> int:
    cleaned = impact.strip().lower()
    items = [item.strip() for item in cleaned.split(',')]
    if 'poor sleep' in items:
        if len(items) == 1:
            return 1
        else:
            return 2
    else:
        return 3

def limit_encoded(limit:bool) -> int:
  return 1 if (limit) else 0

def addiction_map(addiction:str) -> int:
  if addiction.lower() == 'highest_addiction':
    return 0
  elif addiction.lower() == 'average_addiction':
    return 1
  elif addiction.lower() == 'low_addiction':
    return 2
  elif addiction.lower() == 'lowest_addiction':
    return 3
