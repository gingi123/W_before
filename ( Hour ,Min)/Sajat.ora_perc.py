import datetime


def Aktualisido()->list[int,int]:

    ora: int = datetime.datetime.now().hour
    perc: int = datetime.datetime.now().minute

    return [ora , perc]

Aktido: list[int,int] = Aktualisido()

print(f"Az aktuális idŐ: {Aktido[0]}:{Aktido[1]}")




def Ido_beker(uzi:str,min:int,max:int)->int:
    ertek = int(input(uzi))
    while ertek < min or ertek > max:
        print(f"A megadott érték nem megfelelő, {min} és {max} érték közötti értéket adjon meg!")
        ertek = int(input(uzi))

    return ertek




ora = Ido_beker("Adja meg a tanóra végét[óra]: ",0,23)
perc = Ido_beker("Adja meg a tanóra végét[perc]: ",0,59)

hatralevoido = (ora *60 + perc) - (Aktido[0]*60 + Aktido[1])

if hatralevoido > 0:
    print(f"Az órából még {hatralevoido} perc van hátra")
else:
    print("Az óra véget ért")










