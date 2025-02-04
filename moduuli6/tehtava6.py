def main():


    print("Ohjelma laskee pizzojen vastineen rahalle.")


    print("Anna ensimmäisen pizzan halkaisija senttimetreinä (cm): ")
    dia1 = float(input(" > "))
    print("Anna ensimmäisen pizzan hinta euroina (€): ")
    cost1 = float(input(" > "))

    print("Anna toisen pizzan halkaisija senttimetreinä (cm): ")
    dia2 = float(input(" > "))
    print("Anna toisen pizzan hinta euroina (€): ")
    cost2 = float(input(" > "))

    value1 = costcalc(dia1, cost1)
    value2 = costcalc(dia2, cost2)

    print(f"Ensimmäisen pizzan metrihinta: {value1:0.2f} €/m^2")
    print(f"Toisen pizzan metrihinta: {value2:0.2f} €/m^2")

    if value1 > value2:
        print("Toinen pizza on halvempi.")
    elif value1 < value2:
        print("Ensimmäinen pizza on halvempi.")
    elif value1 == value2:
        print("Pizzojen metrihinnat ovat samat.")


def costcalc(dia, cost):
    import math
    pinta = ((math.pi/4)*dia**2)*0.0001
    return cost / pinta

main()