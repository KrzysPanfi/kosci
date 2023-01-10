import random
print("czy chcesz zagrać")
gra=int(input("jesli tak napisz 1"))
print("Aby wygrać obie kości muszą mieć jedną liczbę")
print("wybiesz zasieg kosci")
zasieg=int(input("jesli zagieg kosci ma byc 1-6 napisz 1, jesli zagieg kosci ma byc 7-12 napisz 2, jesli zagieg kosci ma byc 13-18 napisz 3 " ))
    #print("czy chcesz zagrać")
    #gra=int(input("jesli tak napisz 1"))
    #print("Aby wygrać obie kości muszą mieć jedną liczbę")
if zasieg == 1:
    while gra == 1:
          a=random.randint(1,6)
          b=random.randint(1,6)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))
          elif a!=b:
              print("Masz pecha")
              gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))
if zasieg == 2:
    while gra == 1:
          a=random.randint(7,12)
          b=random.randint(7,12)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))
          elif a!=b:
              print("Masz pecha")
              gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))
if zasieg == 3:
    while gra == 1:
          a=random.randint(13,18)
          b=random.randint(13,18)
          print(a)
          print(b)
          if a==b:
            print("Masz szczęście")
            gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))
          elif a!=b:
              print("Masz pecha")
              gra=int(input("czy chcesz zagrać ponownie? Jesli tak napisz 1"))



        
        
