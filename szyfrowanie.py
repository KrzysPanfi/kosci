#interpreter do uruchomienia: https://www.onlinegdb.com/online_python_compiler
while True:
    tekst = input("Podaj zdanie do zakodowania:")
    przesuniecie = "14"
    while not przesuniecie.replace("-","").isnumeric() or int(przesuniecie) > 13 or int(przesuniecie) < -13:
        przesuniecie = input("Podaj przesuniecie(od -13 do 13):")
    wynik = ""
    nowa_litera = ""
    kod_znaku = 0
    tekst = tekst.upper()
    for i in tekst:
        kod_znaku = ord(i) # zmieniamy znak na jego kod ASCII
        if i.isupper(): # jezeli znak to litera, to kodujemy (przesuwamy)
            kod_znaku = kod_znaku + int(przesuniecie)
            nowa_litera = chr(kod_znaku)
            if not nowa_litera.isupper(): # jezeli po przesunieciu juz nie jest litera, to idziemy z drugiej strony
                if kod_znaku > ord("Z"):
                    kod_znaku = ord("A") + kod_znaku - ord("Z") - 1
                elif kod_znaku < ord("A"):
                    kod_znaku = ord("Z") - (ord("A") - kod_znaku) + 1               
        wynik = wynik + chr(kod_znaku)
    print("Wynik:",wynik)