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

    for airport in tulos:
        if airport[0] == "small_airport":
            pienkentta += 1
    for airport in tulos:
        if airport[0] == "airport":
            kentta += 1
    for airport in tulos:
        if airport[0] == "large_airport":
            isokentta += 1

    if kursori.rowcount > 0:
        print(pienkentta, kentta, isokentta)
        return pienkentta, kentta, isokentta

def type():




print("Anna maakoodi, ja ohjelma tulostaa lentokenttien määrät tyypeittäin.")
country = input(" > ")
main(country)
