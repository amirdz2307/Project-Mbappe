import random
class Karakter:
    def __init__(self, navn:str, alder:int, kjønn:str, land:str, liv:int):
        self._navn=navn
        self._alder=alder 
        self._kjønn=kjønn
        self._land=land
        self._liv=liv

    def __str__(self):
            return f"navn: {self._navn}, alder: {self._alder}, kjønn: {self._kjønn}, land: {self._land}, liv: {self._liv}"


#ting å fylle inn for å lage en krakter
    def Opprett_karakter(self):
        navn= input("navn ")
        alder = int(input("alder: "))
        kjønn = input("kjønn: ")
        land = input("land: ")
        

        return Karakter(navn, alder, kjønn, land, 100)


#spillregler
    def spillbeskrivelse(self):
     return """
    Spillbeskrivelse:

    1. Max 10 runder
    2. Starter med 100 liv
    3. Tap = -100p, likt = 0p, vinn = +100p
    4. Saks > papir
    5. Papir > stein
    6. Stein > saks
    """

    def start(self):
        input("Trykk ENTER for å sette i gang!")
        print(self.spillbeskrivelse())
        input("Trykk ENTER for å starte spillet")


    def velg_handling(self):
        valg = input("velg stein, saks eller papir: ")


        while valg not in ["stein", "saks", "papir"]:
          valg = input("velg stegn, saks eller papir: ")

         
        return valg     

#PC-karakteren
class Drage(Karakter):
    def __init__(self, navn, alder, kjønn, land, liv, farge):
        super().__init__(navn, alder, kjønn, land, liv)
        self._farge = farge


    def velg_handling(self):
        valg = ["stein", "saks", "papir"]
        return random.choice(valg)
    

    


spiller = Karakter("", 0, "", "", 100)
drage = Drage("drage", 1000, "drage", "fantasiverden", 100, "rød")

spiller = spiller.Opprett_karakter()
print("hei " + spiller._navn + "!")

spiller.start()
spill = 0

#hva begge krakterene velger
while spill < 10:
    spiller_valg = spiller.velg_handling()
    print("Du valgte: ", spiller_valg)

    drage_valg = drage.velg_handling()
    print("drage valgte: ", drage_valg)


    #hva som skjer når spilleren vinner
    if spiller_valg == "stein" and drage_valg == "saks":
        spiller._liv += 100
        drage._liv -= 100
        print(spiller._navn, "vant og har", spiller._liv, "poeng! Drage poeng:", drage._liv)

    elif spiller_valg == "saks" and drage_valg == "papir":
        spiller._liv += 100
        drage._liv -= 100
        print(spiller._navn, "vant og har", spiller._liv, "poeng! Drage poeng:", drage._liv)

    elif spiller_valg == "papir" and drage_valg == "stein":
        spiller._liv += 100
        drage._liv -= 100
        print(spiller._navn, "vant og har", spiller._liv, "poeng! Drage poeng:", drage._liv)

        #hva som skjer når daragen vinner
    elif spiller_valg == "stein" and drage_valg == "papir":
        drage._liv += 100
        spiller._liv -= 100
        print(drage._navn, "vant og har", drage._liv, "poeng! Spiller poeng:", spiller._liv)

    elif spiller_valg == "papir" and drage_valg == "saks":
        drage._liv += 100
        spiller._liv -= 100
        print(drage._navn, "vant og har", drage._liv, "poeng! Spiller poeng:", spiller._liv)

    elif spiller_valg == "saks" and drage_valg == "stein":
        drage._liv += 100
        spiller._liv -= 100
        print(drage._navn, "vant og har", drage._liv, "poeng! Spiller poeng:", spiller._liv)


    #hva som skjer når det blir uavgjort
    elif spiller_valg == "stein" and drage_valg == "stein":
        print("Uavgjort! Spiller poeng:", spiller._liv, "Drage poeng:", drage._liv)

    elif spiller_valg == "papir" and drage_valg == "papir":
        print("Uavgjort! Spiller poeng:", spiller._liv, "Drage poeng:", drage._liv)

    elif spiller_valg == "saks" and drage_valg == "saks":
        print("Uavgjort! Spiller poeng:", spiller._liv, "Drage poeng:", drage._liv)


    spill += 1



print("spillet er ferdig")

if spiller._liv > drage._liv:
    print("gratulerer", spiller._navn, ", DU VANT!")
    print("Du vant med", spiller._liv - drage._liv, "poeng mer enn dragen!")

elif drage._liv > spiller._liv:
    print("drage vant! uflaks!")
    print("Dragen vant med", drage._liv - spiller._liv, "poeng mer enn deg!")

else:
    print("Uavgjort!")
    print("Begge endte med", spiller._liv, "poeng.")















    






