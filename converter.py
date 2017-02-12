print("Pozdravljeni v pretvorniku kilometrov v milje.")

i = True
while i == True:
    stevilo_kilometrov = int(raw_input("Prosimo, vnesite stevilo kilometrov: "))
    stevilo_milj = str(stevilo_kilometrov * 0.62)
    stevilo_kilometrov_str = str(stevilo_kilometrov)

    print (stevilo_kilometrov_str + " km je enako " + stevilo_milj + " milj.")

    novo = raw_input("Zelite pretvoriti se enkrat(da/ne): ")
    if novo == "da":
        i = True
    else:
        i = False
        print("Zahvaljujemo se vam za uporabo nasega programa.")


