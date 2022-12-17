
def fajl(fajlnev):
    f = open(fajlnev,"r")
    fejlec= f.readline().strip()
    sorok = f.readlines()
    f.close()
    feldolgozas(sorok)

stadion =[]
varos = []
csapat_szam= []
elso_merkozes = []
utolso_merkozes = []

def feldolgozas(sorok):
    i = 0
    while ( i< len(sorok)):
        sor = sorok[i].strip().split(';')
        stadion.append(sor[0])
        varos.append(sor[1])
        csapat_szam.append(sor[2])
        elso_merkozes.append(sor[3])
        utolso_merkozes.append(sor[4])
        i +=1
    print(f' A csapatok száma: {i}')
    j = 0
    while (j < len(sorok)):
        if (varos[j] == 'New York'):
            print(f'{stadion[j]} - {csapat_szam[j]}')
        j +=1
