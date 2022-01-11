import random

jatekVege = 0
jatekosMegallt = 0
gepMegallt = 0

def ujJatek():
    initJatek()


def initJatek():
    pakli = generalas()
    jatekosLapok = []
    gepLapok = []

    for i in range(2):
        jatekosLapok.append(huzas(pakli))
        gepLapok.append(huzas(pakli))

    print('A lapjaid: ', jatekosLapok)

    global jatekVege
    while jatekVege != 1:
        if jatekosMegallt != 1 and jatekVege != 1:
            jatekosKor(jatekosLapok, pakli)
        if gepMegallt != 1 and jatekVege != 1:
            gepKor(gepLapok, pakli)
        if jatekosMegallt == 1 and gepMegallt == 1:
            terites(jatekosLapok, gepLapok)
            jatekVege = 1

def jatekosKor(jatekosLapok, pakli):
    jatekosErtek = ertek(jatekosLapok)
    global jatekVege
    if jatekosErtek < 16:
        print('A lapjaid értéke (',jatekosErtek,') kevesebb mint 16. Nyomj meg egy gombot a húzáshoz.')
        input()
        jatekosLapok.append(huzas(pakli))
        jatekosErtek = ertek(jatekosLapok)
        print('Lapot húzol.')
        print('Lapjaid:', jatekosLapok)
        if jatekosErtek > 21:
            print('Besokaltál. A gép nyert.')
            jatekVege = 1
    else:
        dontes = ''
        global jatekosMegallt
        while (dontes != 'N' or dontes != 'Y') and jatekosMegallt != 1:
            dontes = input('A lapjaid értéke: {} Szeretnél még húzni? Y/N\n'.format(jatekosErtek))
            dontes = dontes.upper()
            if dontes == 'N':
                print('Megálltál.')
                jatekosMegallt = 1
            if dontes == 'Y':
                jatekosLapok.append(huzas(pakli))
                jatekosErtek = ertek(jatekosLapok)
                print('Lapot húzol')
                print('Lapjaid:', jatekosLapok)
                if jatekosErtek > 21:
                    print('Besokaltál. A gép nyert.')
                    jatekVege = 1
                    return


def  gepKor(gepLapok, pakli):
    print('A gép köre...')
    gepErtek = ertek(gepLapok)
    if gepErtek < 16:
        print('A gép lapot húz.')
        gepLapok.append(huzas(pakli))
        gepErtek = ertek(gepLapok)
        if gepErtek > 21:
            print('A gép besokalt. Nyertél.')
            global jatekVege
            jatekVege = 1

    else:
        print('A gép megáll.')
        global gepMegallt
        gepMegallt = 1

def terites(jatekosLapok, gepLapok):
    jatekosErtek = ertek(jatekosLapok)
    gepErtek = ertek(gepLapok)
    print('Lapjaid: ', jatekosLapok, ', Értéke: ',jatekosErtek)
    print('A gép lapjai: ', gepLapok, ', Értéke: ', gepErtek)
    if jatekosErtek > gepErtek:
        print('Nyertél.')
    elif gepErtek > jatekosErtek:
        print('A gép nyert.')
    elif jatekosErtek == gepErtek:
        if len(jatekosLapok) < len(gepLapok):
            print('Nyertél.')
        elif len(jatekosLapok) > len(gepLapok):
            print('A gép nyert.')
        else:
            print('Döntetlen.')



def generalas():
    pakli = []
    szamsor = []
    szamsor.extend(range(2,11))
    szamsor.extend(['J','Q','K','A'])
    for i in range(4):
        pakli.extend(szamsor)
    return pakli

def huzas(pakli):
    i = random.randint(0, len(pakli) - 1)
    lap = pakli[i]
    pakli.remove(lap)
    return lap

def ertek(lapok):
    ertek = 0
    aszDarab = 0
    for i in range(len(lapok)):
        if isinstance(lapok[i], int):
            ertek += lapok[i]
        else:
            if 'A' == lapok[i]:
                aszDarab+= 1
            else:
                ertek += 10
    if aszDarab == 2 and len(lapok) == 2:
        ertek = 21
    elif aszDarab > 0:
        for i in range(aszDarab):
            if ertek + 11 <= 21:
                ertek +=11
            else:
                ertek += 1
    return ertek