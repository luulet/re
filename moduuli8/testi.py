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

sql = f"select *flight_game"
