def feladat1():
    a = int(input("Kérek egy egész sámot! a="))
    if a%2==0:
        print("A megadott szám páros.")
    else:
        print("A megadott szám páratlan.")

def feladat4(szam):
    if szam>-30 and szam<40:
        print("A megadott szám -20 és 40 közé esik.")
    else:
        print("Nem esik a megadott intervallumba.")

def feladat5(szam):
    if szam<16:
        print(szam*10)
    else:
        print(szam/3)

def feladat11():
    a = float(input("Kérem az a oldalát! a="))
    b = float(input("Kérem a b oldalát! b="))
    c = float(input("Kérem a c oldalát! c="))
    if a+b>c and a+c>b and b+c>a:
        print("A háromszög szerkeszthető.")
    else:
        print("Nem szerkeszthető.")

#itt kezdő
#a=int(input("Kérek egy számot! a="))
#feladat1()
#feladat4(43)
#feladat4(34)
#feladat4(-30)
#feladat5(a)
feladat11()





