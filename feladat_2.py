import random
def veletlen(db):
    i = 1
    lista= []

    while(i <= db):
        vel = (int(random.random()*110)-40)
        lista.append(vel)
        i += 1
    print(lista)
    return lista
def ketjegy(lista):
    i = 0
    ketto = 0
    ketto_szam = ''
    while(i<len(lista)):
        if((lista[i]<100 and lista[i]> 9) or lista[i]< -9):
            ketto += 1
        i +=1
    print(f'Kétjegyű számok: {ketto} darab.')
    return ketto

def osszeg_paros(lista):
    i = 0
    paros_ossz = 0
    while (i != len(lista)):
        if (lista[i] % 2 == 0):
            paros_ossz += lista[i]
        i += 1
    print(f'A páros számok összege: {paros_ossz}')
    return paros_ossz

def osszeg_paratlan(lista):
    i = 0
    paratlan_ossz = 0
    while (i != len(lista)):
        if (lista[i] % 2 != 0):
            paratlan_ossz += lista[i]
        i += 1
    print(f'A páratlan számok összege: {paratlan_ossz}')
    return paratlan_ossz

def hasonlit(lista):
    paros_osszeg=osszeg_paros(lista)
    paratlan_osszeg = osszeg_paratlan(lista)
    if (paros_osszeg==osszeg_paratlan):
        print('A páros és páratlan számok összege egyenlő.')
    elif paros_osszeg > paratlan_osszeg:
        print(f'páros számok összege {paros_osszeg} > páratlan számok összege {paratlan_osszeg}')
    else:
        print(f'páratlan számok összege {paratlan_osszeg} > páros számok összege {paros_osszeg}')


def meghivas():
    lista= veletlen(13)
    ketjegy(lista)
    osszeg_paros(lista)
    osszeg_paratlan(lista)
    hasonlit(lista)
