import datetime
                                                                            # 19:00   ora vége 
                                                                            # 17:50    aktuális 


def Aktualisido()->list[int,int]:

    ora: int = datetime.datetime.now().hour
    perc: int = datetime.datetime.now().minute

    return [ora , perc]

Aktido: list[int,int] = Aktualisido()

print(f"Az aktuális idŐ: {Aktido[0]}:{Aktido[1]}")


def ido_beker2(uzenet:str,min:int,max:int):
    szam:int = -1
    while szam < min or szam > max:
        szam = int(input(uzenet))
        if szam < min or szam > max:
            print(f"A megadott érték nem megfelelő, {min} és {max} Közötti értéket adjon meg!")
    return szam


ora: int  = ido_beker2("Adja meg a tanóra végét[óra]: ",0,23)
perc: int = ido_beker2("Adja meg a tanóra végét [perc]: ",0,59)


hatralevo:int = (ora * 60 + perc) - (Aktido[0] * 60 + Aktido [1])
if hatralevo < 0:
    print("Az óra már végetért")
else:
    print(f"A tanóra végéig hátralévő idő: {hatralevo}")



