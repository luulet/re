import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='sampo',
         password='luulee',
        autocommit=True,
        #collation='utf8mb3_general_ci'
        collation='utf8mb3_general_ci'
         )


def main(country):


    sql = f"SELECT type FROM airport where iso_country='{country}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    pienkentta = 0
    kentta = 0
    isokentta = 0
    heli = 0
    sea = 0


    for airport in tulos:
        if airport[0] == "small_airport":
            pienkentta += 1
    for airport in tulos:
        if airport[0] == "medium_airport":
            kentta += 1
    for airport in tulos:
        if airport[0] == "large_airport":
            isokentta += 1
    for airport in tulos:
        if airport[0] == "heliport":
            heli += 1
    for airport in tulos:
        if airport[0] == "seaplane_base":
            sea += 1
    if kursori.rowcount > 0:
        if isokentta > 0:
            print(f'Isoja lentokenttiä on {isokentta}.')
        if kentta > 0:
            print(f'Keskikokoisia lentokenttiä on {kentta}.')
        if pienkentta > 0:
            print(f"Pienlentokenttiä on {pienkentta}.")
        if heli > 0:
            print(f'Helikopterikenttiä on {heli}.')
        if sea > 0:
            print(f'Vesilentokoneen tukikohtia on {sea}.')





print("Anna maakoodi, ja ohjelma tulostaa lentokenttien määrät tyypeittäin.")
country = input(" > ")
main(country)

