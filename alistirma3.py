note = 50
name="ozcan"
age = 25

if note >= 0 and note < 35:
    print("FF")
elif note >= 35 and note < 55:
    print("CC")
elif note >= 55 and note < 70:
    print("BB")
elif note >= 70 and note < 101 :
    print("AA")
elif note == 299 and (name=="ozcan" or age==30):
    print("Sanslı!")
else:
    print("Hatalı Not!")


if note > 45:
    print("Harıka notunuz yuksek")
    if age < 29:
        print("Harıka yasınız da ıyı")
        if name == "ozcan":
            print("Harıka bır aday")
        else:
            print("Sansınız yok!")
    else:
        print("Elendiniz, cunku kartsınız")
else:
    print("Elendiniz, cunku notunuz dusuk.")
