def megtalal(karakterlanc, keresendo):
    if keresendo in karakterlanc:
        return karakterlanc.index(keresendo)
    else:
        return -1

def karakterszam(karakterlanc, megszamolando):
    return  karakterlanc.count(megszamolando)


def feladat2():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore, a!'
    karakter=(input("Adj meg egy karakert: "))
    # kiírjuk a visszakapott eredményt
    print(megtalal(szoveg, karakter))
    # változóba tesszük
    eredmeny=megtalal(szoveg, karakter)
    if eredmeny==-1:
        print("A megadott karakter nem szerepel a szövegben")
    else:
        print('A megadott karakter a', eredmeny, 'indexű helyen fordul elő elősször')

def feladat4():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore, a!'
    karakter=(input("Adj meg egy karakert: "))
    print('A megadott szövegben az adott karakter', karakterszam(szoveg, karakter), 'alkalommal fordul elő')

def feladat6():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore, a!'
    print('A megadott szöveg', karakterszam(szoveg, ' ')+1, 'szóból áll')

def feladat5():
    prefixes='JKLMOPQ'
    suffixe='ack'
    kacsak=[]
    for item in prefixes:
        kacsak.append(item+suffixe)
    for item in kacsak:
        print(item, end=' ')
    
def nagybetu():
    nagybetuk='AQÍYSWXCDERFVBGTZHNMJUIKLOPÉŐÁŰÚÓÜÖ'


#itt kezdődik a főprogram
#feladat2()
#feladat4()
#feladat6()
#feladat5()