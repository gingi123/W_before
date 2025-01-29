def unit_change(celsius: int) -> list[float, float]:
    kelvin: float =  celsius + 273.15
    fahrenheit: float = celsius * (9  / 5) + 32
    return [fahrenheit, kelvin]