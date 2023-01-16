import random

zasieg=1
print("czy chcesz zagrać")
try:
    gra=int(input("jesli tak napisz 1"))
except:
    gra=2
if gra==1:
    print("Aby wygrać obie kości muszą mieć jedną liczbę")
    print("wybierz zasieg kosci")
    try:
        zasieg=int(input("jesli zasieg kosci ma byc 1-6 napisz 1, jesli zasieg kosci ma byc 7-12 napisz 2, jesli zasieg kosci ma byc 13-18 napisz 3" ))
    except:
        zasieg=1
    
if zasieg == 1:
    while gra==1:
          a=random.randint(1,6)
          b=random.randint(1,6)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
            except:
                gra=2
          elif a!=b:
              print("Masz pecha")
              try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
              except:
                  gra=2
              
if zasieg==2:
    while gra==1:
          a=random.randint(7,12)
          b=random.randint(7,12)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
            except:
                gra=2
          elif a!=b:
              print("Masz pecha")
              try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
              except:
                  gra=2
              
if zasieg==3:
    while gra==1:
          a=random.randint(13,18)
          b=random.randint(13,18)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
            except:
                gra=2
          elif a!=b:
              print("Masz pecha")
              try:
                gra=int(input("Czy chcesz zagrać ponownie? Jesli tak napisz 1"))
              except:
                  gra=2
