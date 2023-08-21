import random

poziom_trudnosci=int(input("Wybierz poziom trudności. 1 to łatwy 2 to średni 3 to trudny"))
if poziom_trudnosci==1:
    drewno=5
    leki=5
    bron=5
elif poziom_trudnosci==2:
    drewno=3
    leki=3
    bron=3
elif poziom_trudnosci==3:
    drewno=1
    leki=1
    bron=1


print("Jesteś poszukiwaczem przygód okrywającym starożytne lochy. Lochy są podzielona na piętra. Na każdym piętrze stawisz czoła wyzwaniu, które możesz rozwiązać na wiele sposobów.")
print("1 piętro")
print("Przed tobą widnieje dziura w przepaść")
print("Wybierz rozwiązanie tego wyzwania")
print("drewno:",drewno)
print("leki:",leki)
print("broń:",bron)
rozwiazanie=int(input("1 przeskocz dziure szansa powodzenia 50%. 2 Użyj drewna do przejścia nad dziurą Drewno-1"))
if rozwiazanie==1:
    sukces=random.randint(1,2)
    if sukces==1:
        print("Przeskoczyłeś dziurę")
    else:
        print("Spadleś w dziurę")
        print("Porażka")
        exit("Porażka")
else:
    if drewno!=0:
        print("Użyłeś drewna do przejscia na dziurą. Drewno-1")
        drewno=drewno-1
    else:
        sukces=random.randint(1,2)
        if sukces==1:
            print("Przeskoczyłeś dziurę")
        else:
            print("Spadleś w dziurę")
            print("Porażka")
            exit()
        
              
print("2 piętro")
print("Widzisz potwora, który zaczyna pełzać w twoja stronę")
print("Wybierz rozwiązanie tego wyzwania")
print(drewno)
print(leki)
print(bron)
rozwiazanie=int(input("1 Walcz z potworem na golę pięści szansa powodzenia 25%. 2 Użyj broni do walki z potworem Broń-1"))
if rozwiazanie==1:
    sukces=random.randint(1,4)
    if sukces==1:
        print("Pokonałeś potwora gołymi pięściami")
    else:
        if leki!=0:
            print("Zostałęś ranny. Leki-1")
            leki=leki-1
        else:
            print("Poległeś od odniesionych ran")
            print("Porażka")
            quit()
else:
    if bron!=0:
        print("Użyłeś broni do zabicia potowra. Broń-1 ")
        bron=bron-1
    else:
        sukces=random.randint(1,4)
        if sukces==1:
            print("Pokonałeś potwora gołymi pięściami")
        else:
            if leki!=0:
                print("Zostałęś ranny. Leki-1")
                leki=leki-1
            else:
                print("Poległeś od odniesionych ran")
                print("Porażka")
                quit()

  
print("3 piętro")
print("Przed tobą skarb jednak jest chroniony przez pułapki")
print("Wybierz rozwiązanie tego wyzwania")
print(drewno)
print(leki)
print(bron)
rozwiazanie=int(input("1 Przebjegnij przez pułapki. Szansa na powodzienie 10%. 2 Użyj zasobów do rozbrojenia pułapki. Drewno-2 Broń -2"))
if rozwiazanie==1:
    sukces=random.randint(1,10)
    if sukces==1:
        print("Przebiegłeś przez pułapki")
        print("Znalazłeś skarb")
        print("Wygrana")
        quit()
    else:
        if leki!=0:
            print("Zostałęś ranny. Leki-1")
            leki=leki-1
            print("Znalazłeś skarb")
            print("Wygrana")
            quit()
        else:
            print("Poległeś od odniesionych ran")
            print("Porażka")
            quit()
else:
    if drewno>=2 and bron>=2:
        print("Użyłeś zasobów do rozbrojenia pułapki. Drewno-2. Broń -2")
        drewno=drewno-2
        bron=bron-2
        print("Znalazłeś skarb")
        print("Wygrana")
        quit()
    else:
        print("Brak zasobów")
        sukces=random.randint(1,10)
        if sukces==1:
            print("Przebiegłeś przez pułapki")
            print("Znalazłeś skarb")
            print("Wygrana")
            quit()
        else:
            if leki!=0:
                print("Zostałęś ranny. Leki-1")
                leki=leki-1
                print("Znalazłeś skarb")
                print("Wygrana")
                quit()
            else:
                print("Poległeś od odniesionych ran")
                print("Porażka")
                quit()
                
