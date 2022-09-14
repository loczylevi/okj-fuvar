class Fuvar:
    def __init__(self,sor):
        taxi_id,indulas,utazas_ido,megtett_tav,viteldij,borravalo,fizetes_mod = sor.strip().split(";")
        self.taxi_id = int(taxi_id)
        self.indulas = indulas
        self.utazas_ido = int(utazas_ido)
        self.megtett_tav = float(megtett_tav.replace(',','.'))
        self.viteldij = float(viteldij.replace(',','.'))
        self.borravalo = float(borravalo.replace(',','.'))
        self.fizetes_mod = fizetes_mod
        
with open("fuvar.csv","r",encoding="UTF-8") as f:
    fejlec = f.readline()
    lista =  [Fuvar(sor) for sor in f]
    
print(f"3.feladat: {len(lista)} fuvar")

hany_fuvar = len([sor for sor in lista if sor.taxi_id == 6185])

bevetel = sum([sor.viteldij for sor in lista if sor.taxi_id == 6185])

bevetel = str(bevetel).replace('.',',') # finomitás

print(f"4.feladat: {hany_fuvar} fuvar alatt: {bevetel}$")

bankkartya = len([sor for sor in lista if sor.fizetes_mod == "bankkártya"])
keszpenz = len([sor for sor in lista if sor.fizetes_mod == "készpénz"])
ismeretlen = len([sor for sor in lista if sor.fizetes_mod == "ismeretlen"])
free = len([sor for sor in lista if sor.fizetes_mod == "ingyenes"])
vitatott = len([sor for sor in lista if sor.fizetes_mod == "vitatott"])

print(f"""5.feladat:
       bankkártya: {bankkartya} fuvar
       készpénz: {keszpenz}
       vitatott: {vitatott}
       ingyenes: {free}
       ismeretlen: {ismeretlen}""")


ossz_megtett_tav = sum([sor.megtett_tav * 1.6 for sor in lista])

eredmeny = round(ossz_megtett_tav,2)

finomit = str(eredmeny).replace('.',',')

print(f"6.feladat: {finomit}km")

leghosszab = 0
taxi_id = ""
megtett_tav = ""
viteldij = ""

# nem tudtam máshogy megoldani tudom hogy csunya ez van ༼ つ ◕_◕ ༽つ
for sor in lista:
    if sor.utazas_ido > leghosszab:
        leghosszab = sor.utazas_ido
        taxi_id = sor.taxi_id
        megtett_tav = sor.megtett_tav
        viteldij = sor.viteldij
        
megtett_tav = str(megtett_tav).replace('.',',')
viteldij = str(viteldij).replace('.',',')
        
print(f"""7. feladat: Leghosszabb fuvar:
        Fuvar hossza: {leghosszab} másodperc
        Taxi azonositó: {taxi_id}
        Megtett távolság: {megtett_tav}
        Viteldíj: {viteldij}$""")

x = [str(sor.utazas_ido) for sor in lista][0]
# utazas ido és viteldij egy nullaval tobb megtett tavolsag nulla
tarolo = []
with open("hibak.txt","w",encoding="UTF-8") as f2:
    for sor in lista:
        if str(sor.utazas_ido)[-1] == "0" and str(sor.viteldij)[-1] == "0" and sor.megtett_tav == 0:
            tarolo.append(sor)
    tarolo.sort(key=lambda x:x.indulas) #reverse=True
    f2.write(fejlec)
    for sor in tarolo:
        # taxi_id,indulas,utazas_ido,megtett_tav,viteldij,borravalo,fizetes_mod
        f2.write(f"{sor.taxi_id};{sor.indulas};{sor.utazas_ido};{sor.megtett_tav};{sor.viteldij};{sor.borravalo};{sor.fizetes_mod}\n")
    
    