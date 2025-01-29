from temperature_calc import *


min: int = -40
max: int = 50
uzi = "Adja meg a celsius adatot: "



def temp_input(celsius:float,min:int,max:int,uzi:str)->None:
    while celsius < min or celsius > max:
        print(f'A megadott érték nem megfelelő, {min} és {max} közötti értéket adjon meg!')
        celsius:float = float(input(uzi))
    Listacska =  unit_change(celsius)
    print(f"A bekért hőfok: {celsius:.1f}")
    print(f"A megadott celsius érték átváltva {Listacska[0]} fahrenheit és {Listacska[1]} kelvin! ")
    

def Main():
    
    celsius:float = float(input(uzi))
    temp_input(celsius,min,max,uzi)
    
    


Main()






