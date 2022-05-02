import math as ma

def kolo(r):
    return ma.pi*r*r

def prostokat(a,b):
    return a*b

def trojkat(a,b,c):
    ob=((a+b+c)/2)
    return (ob*(ob-a)*(ob-b)*(ob-c))**(1/2)

def zsumuj_liste(lista_do_zsumowania):
    result = 0
    for x in lista_do_zsumowania:
        result += x
    return result

dane=[]
wyniki = []
ilosc_figur= int(input())
for liczb in range(ilosc_figur):
    dane.append(input().split(" "))

#print(dane)  
for value in dane:
    #print(len(value))
    if len(value) ==1:
        #print(value[0])    
        wynik_kolo =kolo(float(value[0]))
        wyniki.append(wynik_kolo)
        #print(wynik_kolo)
        
    elif len(value) ==2:
        #print(float(value[0]),float(value[1]))
        wynik_prosokat = prostokat(float(value[0]),float(value[1]))
        wyniki.append(wynik_prosokat)
        #print(wynik_prosokat)
    elif len(value) ==3:
        #print(float(value[0]),float(value[1]),float(value[2]))
        wynik_trojkat = trojkat(float(value[0]),float(value[1]),float(value[2]))
        wyniki.append(wynik_trojkat)
        #print(wynik_trojkat)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
#print(wyniki)

print(round(zsumuj_liste(wyniki),2))