def main():
    print("Ohjelma laskee pizzojen vastineen rahalle.")
    print("Anna ensimmäisen pizzan halkaisija senttimetreinä: ")
    dia1 = float(input(" > "))
    print("Anna ensimmäisen pizzan hinta euroina: ")
    cost1 = float(input(" > "))
    print("Anna toisen pizzan halkaisija senttimetreinä: ")
    dia2 = float(input(" > "))
    print("Anna toisen pizzan hinta euroina: ")
    cost2 = float(input(" > "))
    print(pizza(value1))
    return dia1

def pizza(pizza):
    import math
    value1 = (math.pi/4)*pow(dia1,2)
    return value1
main()