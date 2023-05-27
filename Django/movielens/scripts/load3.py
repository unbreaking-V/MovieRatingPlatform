import json
import psycopg2
import os.path

# connect to the database
conn = psycopg2.connect(host="localhost", database="moviedb", user="username", password="123")

# create for to read the data from json file from data folder and insert into the database


with open("/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_ratings.json") as f:
    data = json.load(f)

# create a cursor
cur = conn.cursor()

# Iterate over the data
for item in data:
    rating = item["rating"]
    movie_id = item["movie_id"]
    user_id = item["user_id"]

    # Execute the INSERT statement
    cur.execute(
        "INSERT INTO userview_rating (value, movie_id, user_id) VALUES (%s, %s, %s)",
        (rating, movie_id, user_id)
    )

    # Commit the changes to the database
    conn.commit()


cur.close()
conn.close()





