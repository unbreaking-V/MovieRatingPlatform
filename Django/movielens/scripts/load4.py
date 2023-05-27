import json
import psycopg2
import os.path
from datetime import datetime




# connect to the database
conn = psycopg2.connect(host="localhost", database="moviedb", user="username", password="123")

# create for to read the data from json file from data folder and insert into the database


with open("/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_comments.json") as f:
    data = json.load(f)

# create a cursor
cur = conn.cursor()

# Iterate over the data
for item in data:
    user_id = item["user"]
    movie_id = item["movie"]
    comment = item["comment"]
    # timestamp = item["timestamp"]
    # unix_timestamp = test  # Replace with your actual Unix timestamp
    #
    # timestamp = int(datetime.fromtimestamp(unix_timestamp))

    # Execute the INSERT statement
    cur.execute(
        "INSERT INTO userview_comments (user_id, movie_id, comment, timestamp) VALUES (%s, %s, %s, %s)",
        (user_id, movie_id, comment, "2023-05-27 12:12:12")
    )

    # Commit the changes to the database
    conn.commit()


cur.close()
conn.close()





