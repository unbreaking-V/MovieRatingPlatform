import json
import psycopg2
import os.path

# connect to the database
conn = psycopg2.connect(host="localhost", database="moviedb", user="username", password="123")

# create for to read the data from json file from data folder and insert into the database
for i in range(1, 113):
    if os.path.isfile(
            f'/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_movies/{i}.json'):
        with open(
                f"/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_movies/{i}.json") as f:
            data = json.load(f)

        # create a cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(
            "INSERT INTO userview_movie (movieid, title, year, genre, director, imdblink, image, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (i, data["title"], data["year"], data["genre"], data["director"], data["imdbLink"], data["image"],
             data["description"]))

        # commit the changes to the database
        conn.commit()

        # close the cursor and connection

    else:
        continue




cur.close()
conn.close()





