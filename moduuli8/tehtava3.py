import mysql.connector
from geopy import distance

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

def coordinate_finder(location):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{location}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        return tulos



print("Ohjelma laskee kahden lentokentän välisen etäisyyden.")
print("Anna ensimmäisen lentokentän ICAO-koodi")
location1 = input(" > ")
print("Anna toisen lentokentän ICAO-koodi")
location2 = input(" > ")


coordinate_finder(location1)
coordinate_finder(location2)

print()
print("Lentokenttien koordinaatit:")
print(coordinate_finder(location1))
print(coordinate_finder(location2))
print()
print(f"Lentokenttien välinen etäisyys on {distance.distance(coordinate_finder(location1), coordinate_finder(location2)).km:0.2f} km.")

