import random
try:
    poziom_trudnosci=int(input("Wybierz poziom trudności. 1 to łatwy 2 to średni 3 to trudny"))
except:
    poziom_trudnosci=1
    
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

gra=1
pietro=1
print("Jesteś poszukiwaczem przygód okrywającym starożytne lochy. Lochy są podzielona na piętra. Na każdym piętrze stawisz czoła wyzwaniu, które możesz rozwiązać na wiele sposobów.")
print("Aby wybrać rozwiązanie trzeba podac jego numer")
while gra==1:
    print(pietro," piętro")
    pokoj=random.randint(1,4)
    if pokoj==1:
        print("Przed tobą widnieje dziura w przepaść")
        print("Wybierz rozwiązanie tego wyzwania")
        print("drewno:",drewno)
        print("leki:",leki)
        print("broń:",bron)
        try:
            rozwiazanie=int(input("1. Przeskocz dziurę. Szansa powodzenia 50%. 2. Użyj drewna do przejścia nad dziurą. Drewno-1"))
        except:
           rozwiazanie=1
        if rozwiazanie==1:
                sukces=random.randint(1,2)
                if sukces==1:
                    print("Przeskoczyłeś dziurę")
                    pietro=pietro+1
                else:
                    print("Spadleś w dziurę")
                    print("Porażka")
                    gra=2
        else:
            if drewno!=0:
                print("Użyłeś drewna do przejscia na dziurą. Drewno-1")
                drewno=drewno-1
                pietro=pietro+1
            else:
                sukces=random.randint(1,2)
                if sukces==1:
                    print("Przeskoczyłeś dziurę")
                    pietro=pietro+1
                else:
                    print("Spadleś w dziurę")
                    print("Porażka")
                    gra=2
    if pokoj==2:
        print("Widzisz potwora, który zaczyna pełzać w twoja stronę")
        print("Wybierz rozwiązanie tego wyzwania")
        print("drewno",drewno)
        print("leki",leki)
        print("bron",bron)
        try:
            rozwiazanie=int(input("1 Walcz z potworem na golę pięści szansa powodzenia 25%. 2 Użyj broni do walki z potworem Broń-1"))
        except:
            rozwiazanie=1
        if rozwiazanie==1:
            sukces=random.randint(1,4)
            if sukces==1:
                print("Pokonałeś potwora gołymi pięściami")
                pietro=pietro+1
            else:
                if leki!=0:
                    print("Zostałęś ranny. Leki-1")
                    leki=leki-1
                    pietro=pietro+1
                else:
                    print("Poległeś od odniesionych ran")
                    print("Porażka")
                    gra=2
        else:
            if bron!=0:
                print("Użyłeś broni do zabicia potowra. Broń-1 ")
                bron=bron-1
                pietro=pietro+1
            else:
                sukces=random.randint(1,4)
                if sukces==1:
                    print("Pokonałeś potwora gołymi pięściami")
                    pietro=pietro+1
                else:
                    if leki!=0:
                        print("Zostałęś ranny. Leki-1")
                        leki=leki-1
                        pietro=pietro+1
                    else:
                        print("Poległeś od odniesionych ran")
                        print("Porażka")
                        gra==2
    if pokoj==3:
        print("Napotykasz pułapkę")
        print("Wybierz rozwiązanie tego wyzwania")
        print("drewno",drewno)
        print("leki",leki)
        print("bron",bron)
        try:
            rozwiazanie=int(input("1 Przebiegnij przez pułapkę szansa powodzenia 20%. 2 Użyj zasobów do rozbrojenia pulapki. Broń-2 Drewno-2"))
        except:
            rozwiazanie=1
        if rozwiazanie==1:
            sukces=random.randint(1,5)
            if sukces==1:
                print("Przebiegnołeś pułapkę")
                pietro=pietro+1
            else:
                if leki!=0:
                    print("Zostałęś ranny. Leki-1")
                    leki=leki-1
                    pietro=pietro+1
                else:
                    print("Poległeś od odniesionych ran")
                    print("Porażka")
                    gra=2
        else:
            if bron>=2 and drewno>=2:
                print("Użyłeś zasobów do rzobrojenia pułapki. Broń-2 Drewno-2 ")
                bron=bron-2
                drewno=drewno-2
                pietro=pietro+1
            else:
                sukces=random.randint(1,4)
                if sukces==1:
                    print("Przebiegnołeś pułapkę")
                    pietro=pietro+1
                else:
                    if leki!=0:
                        print("Zostałęś ranny. Leki-1")
                        leki=leki-1
                        pietro=pietro+1
                    else:
                        print("Poległeś od odniesionych ran")
                        print("Porażka")
                        gra==2
    if pokoj==4:
        print("Odnalazłeś skrzynkę z zasobami")
        drewno=drewno+2
        bron=bron+2
        leki=leki+2
        pietro=pietro+1
print("Dotarleś do", pietro, "piętra")  


        
        
                
        
     

              


  
