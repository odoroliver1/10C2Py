'''
#import math
#a=math.pi
# kerekítés
print(round(6.1432,3))
print(round(6.1432,2))
#hatványozás
print(pow(2,8)) #pow(alao,kitevő)
#abs aboszolut ertek

#print(abs(-12))
#print(min(1,2,3,5,6,7,8,9,))
#print(max(1,2,3,4,5,6,7,8,9))
#print(a)

from math import *
b=pi
print(b)
#négyzetgyök vonás -sqrt

print(sqrt(4))
#felfelé kerekítés ceil
print(ceil(4.12))
print(floor(5.99))

from math import*
'''
# 1. négyzet kerülete, területe
a = float(input("Kérem a oldalt :"))
kerulet = 4*a
terulet =a**2
print(kerulet)
print(terulet)
# 2. téglalap kerülete, területe
a = float(input("Kérem a oldalt:"))
b = float(input("Kérem b oldalt:"))
kerulet = 2*a+b
terulet = a*b
print(kerulet)
print(terulet)
# 3. kör kerülete (2*r*PI), területe (r*2*PI)
r = float(input("Kérem r-t:"))
kerulet = 2*r*pi
terulet = 2**2*pi
print(kerulet)
print(terulet)
# 4. kocka térfoagata(V=a^3), felszíne (A=6*a^2)
a = float(input("Kérem a számot:"))
V = a**3
A = 6*a**2
print(V)
print(A)
# 5. derégszögű háromszög 2 befogóját kérd be, add meg az átfogót!
a = float(input("Kérem a számot:"))
b = float(input("Kérem b számot:"))
negyzetgyok = a**2+b**2
megoldas = sqrt(negyzetgyok)
print(megoldas)






