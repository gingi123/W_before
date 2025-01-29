from felfedezesek import *

New_list:list[Felfedezes] = []


def Fajlolvas()->None :
    f = open("felfedezesek.csv","r",encoding="utf-8")
    f.readline()

    for sor in f:
        New_list.append(Felfedezes(sor))
    
    f.close()


def Kereses(vegyjel:str)->Felfedezes:
    while len(vegyjel) < 1 or len(vegyjel) > 2 or not vegyjel.isalpha():
        print("Csak betűk adhatók meg és a bevitt érték csak 2 karakter hosszú lehet!")
        vegyjel = input("3.feladat: Adjon meg egy vegyjelet: ")

    
    for item in New_list:
        if item.vegyjel.upper() == vegyjel.upper():   
            return item
            
    else:
        return None


def Legkisnagy()-> int:
    max:int = 0
    for i in range(len(New_list)-1):
        if New_list[i+1].ev - New_list[i].ev > max:
            max =  New_list[i+1].ev - New_list[i].ev
    return max


def Statisztia()->dict[int,int] :
    New_dict:dict[int,int] = {}
    for item in New_list:
        if item.ev not in New_dict:
            New_dict[item.ev] = 1
        else:
            New_dict[item.ev] += 1
    return New_dict        


def Main()->None:
    Fajlolvas()
    print(f"2. feladat: Elemek száma: {len(New_list)} db")
    vegyjel = input("3.feladat: Adjon meg egy vegyjelet: ")
    Megtalaltelem = Kereses(vegyjel)
    if Megtalaltelem is not None:
        print("4.feladat: keresés")
        print(f"\tAz elem vegyjele: {Megtalaltelem.vegyjel}")
        print(f"\tAz elem neve: {Megtalaltelem.nev}")
        print(f"\tRendszáma: {Megtalaltelem.rendszam}")
        print(f"\tFelfedezés éve: {Megtalaltelem.ev}")
        print(f"\tFelfedező:: {Megtalaltelem.felfedezo}")
    else:
        print("Nincs ilyen elem az adatforrásban!")
    Maxev = Legkisnagy()
    print(f"6.feladat: {Maxev} év volt a leghosszabb időszak két elem felfedezése között.")
    Uj_dict = Statisztia()
    for key,value in Uj_dict.items():
        if value > 3:
            print(f"\t{key}: {value} db")
Main()

















