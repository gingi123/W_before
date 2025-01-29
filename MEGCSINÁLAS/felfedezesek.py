class Felfedezes:

    def __init__(self,sor:str):
        rawdata = sor.strip().split(";")
        self.ev = int(rawdata[0])
        self.nev = rawdata[1]
        self.vegyjel = rawdata[2]
        self.rendszam = int(rawdata[3])
        self.felfedezo = rawdata[4]





