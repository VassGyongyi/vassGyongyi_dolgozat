#feladat 1
def beker():
    szam = int(input())
    while(szam % 2 != 0):
        szam = int(input('Ez nem páros! PÁROS számot kérek!: '))
    return szam

def harom_beker():
    i = 1
    lista =[]
    while(i < 4):
        print(f'Kérem az {i}. páros számot! ')
        szam = beker()
        lista.append(szam)
        i += 1
    return lista

def feldolgoz():
    lista = harom_beker()
    i=0
    seged = lista[0]
    index = 0
    while(i<len(lista)):
        if (seged > lista[i]):
            seged = lista[i]
            index = i
        i += 1
    print(f'{index+1}. lépésben adta meg a legkisebb számot, melynek értéke: {seged}')

