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


def airport_finder(ICAO):
    sql = f"SELECT name, municipality FROM airport where ident='{ICAO}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    for rivi in tulos:
        print(f"Lentokentän nimi on {rivi[0]} ja sijaitsee paikkakunnassa {rivi[1]}.")

print("Anna lentoaseman ICAO-koodi")
ICAO = input(" > ")
airport_finder(ICAO)