from math import*

#harjutus 1

#print("Arvuta peast! ...4*100-55")

#o_vastus=4*100-55
#vastus=int(input("Lahenda �lesanne ..."))
#k=1

#while True:
#    if  o_vastus==vastus: 
#        break       
#    else:
#        print("Viga! Sisesta �ige vastus on ...", )
#        vastus=int(input("Lahenda �lesanne ..."))
#        k+=1

#print("�ige vastus! Katsed oli ...",k )

#x=0
#print("while")
#while x<30:

#    if x%2==1:

#        print(x, end=" ")

#    x+=1


#x=0
#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x==30: 
#        break

#print("For:")
#for x in range(30):
#    if x%2==1:
#        print(x, end=" ")

print("*** NUMBRIDEGA M�NGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage t�isarv => "))) #l�pp sulud x2 korda
        break
    except ValueError:
         print("See ei ole t�isarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole m�tet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("M��rake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0: #; vahetatud : 
        if b % 2 == 0: #  = lisatud
            paaris += 1
        else:
            paaritu += 1
        b = b // 10  #positsioon vahetatud
                    #kustutatud ja lisatud enter
    print("Paarisarvud:",paaris) # koma lisatud
    print("paarituid numbreid:",paaritu) # koma lisatud
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0: # : lisatud
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # positsiooni vahetamine, =+ vahetatud +=
    print("*�mberp��ratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse h�poteesi testimine") # kustutasin algsulg
    print()
    if c % 2 == 0: # lisanud =
        print("c on paarisarv. Jagage 2-ga.")
    else:
        print("c on paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0: # = lisatud
                    c = c / 2 # = kustutatud
            else:
                    c = (3*c + 1) / 2 # = kustutatud
            print(round(c), end=" ") # juttum�rg lisatud
    print()
    print("H�potees on �ige") # juttum�rg vahetatud
