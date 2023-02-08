from random import choice

cikolatalar = [
    "cokonat",
    "cokonat",
    "canga",
    "canga"
]
kazananlar = [
    "enes",
    "elyesa",
    "arda"
]
for i in kazananlar:
    secilen_cikolata = choice(cikolatalar)
    cikolatalar.remove(secilen_cikolata)
    print(f"{i} {secilen_cikolata} kazandı.")


