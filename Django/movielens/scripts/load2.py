import json
import psycopg2
import os.path

# connect to the database
conn = psycopg2.connect(host="localhost", database="moviedb", user="username", password="123")

# create for to read the data from json file from data folder and insert into the database
for i in range(2, 611):


    if os.path.isfile(
            f'/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_users/{i}.json'):
        with open(
                f"/Users/moneymachine/Desktop/DjangoProject/MovieRatingPlatform/Django/dane/picked_users/{i}.json") as f:
            data = json.load(f)

        # create a cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(
            "INSERT INTO auth_user (id, password, first_name, last_name, username, email, is_superuser, is_staff, is_active, "
            "date_joined) VALUES (%s, %s, "
            "%s, %s, %s, %s, %s, %s, %s, %s)",
            (data["user_id"], data["password"], data["first_name"], data["last_name"], data["username"], f"user{i}@gmail.com", "f",
             "f" , "t", "2020-01-01 00:00:00.000000"))

        # commit the changes to the database
        conn.commit()

        # close the cursor and connection

    else:
        continue




cur.close()
conn.close()





