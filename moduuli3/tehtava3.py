suku = input("Anna sukupuolesi (mies/nainen): ")
hemo = float(input("Anna hemoglobiiniarvo (g/l): "))
if suku=="mies":
    if 134>hemo:
        print("Hemoglobiiniarvo on alhainen.")
    elif 134<=hemo<=195:
        print("Hemoglobiiniarvo on normaali.")
    elif hemo>195:
        print("Hemoglobiiniarvo on korkea.")
if suku=="nainen":
    if 117>hemo:
        print("Hemoglobiiniarvo on alhainen.")
    elif 117<=hemo<=175:
        print("Hemoglobiiniarvo on normaali.")
    elif hemo>175:
        print("Hemoglobiiniarvo on korkea.")