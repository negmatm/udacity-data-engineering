# Define drop table sql script variables

songplay_table_drop = "DROP TABLE IF EXISTS Fact_Song_Plays"
user_table_drop = "DROP TABLE IF EXISTS Dim_Users"
song_table_drop = "DROP TABLE IF EXISTS Dim_Songs"
artist_table_drop = "DROP TABLE IF EXISTS Dim_Artists"
time_table_drop = "DROP TABLE IF EXISTS Dim_Time"

# Define create table sql script variables

songplay_table_create = ("CREATE TABLE IF NOT EXISTS Fact_Song_Plays(SongPlay_ID SERIAL PRIMARY KEY, Start_Time TIMESTAMP NOT NULL, User_ID VARCHAR NOT NULL, Level VARCHAR, Song_ID VARCHAR, Artist_ID VARCHAR, Session_ID INT, Location VARCHAR, User_Agent VARCHAR )")

user_table_create = ("CREATE TABLE IF NOT EXISTS Dim_Users(User_ID VARCHAR PRIMARY KEY, First_Name VARCHAR, Last_Name VARCHAR, Gender CHAR, Level VARCHAR)")

song_table_create = ("CREATE TABLE IF NOT EXISTS Dim_Songs(Song_ID VARCHAR PRIMARY KEY, Title VARCHAR, Artist_ID VARCHAR, Year INT, Duration NUMERIC)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS Dim_Artists(Artist_ID VARCHAR PRIMARY KEY, Name VARCHAR, Location VARCHAR, Latitude NUMERIC, Longitude NUMERIC)")

time_table_create = ("CREATE TABLE IF NOT EXISTS Dim_Time(Start_Time TIMESTAMP PRIMARY KEY, Hour INT, Day INT, weekday INT, Week INT, Month INT, Year INT)")

# Define insert sql script variables

songplay_table_insert = ("INSERT INTO Fact_Song_Plays(Start_Time, User_ID, Level, Song_ID, Artist_ID, Session_ID, Location, User_Agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO Dim_Users(User_ID, First_Name, Last_Name, Gender, Level) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (User_ID) DO NOTHING")

song_table_insert = ("INSERT INTO Dim_Songs(Song_ID, Title, Artist_ID, Year, Duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (Song_ID) DO NOTHING")

artist_table_insert = ("INSERT INTO Dim_Artists(Artist_ID, Name, Location, Latitude, Longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (Artist_ID) DO NOTHING")

time_table_insert = ("INSERT INTO Dim_Time(Start_Time, Hour, Day, Week, Month, Year, WeekDay) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (Start_Time) DO NOTHING")

# Define select sql script variable for getting song_id and artist_id from song and artist dimension tables, respectively

song_select = ("SELECT Dim_Songs.Song_ID, Dim_Artists.Artist_ID FROM (Dim_Songs JOIN Dim_Artists ON \
                Dim_Songs.Artist_ID = Dim_Artists.Artist_ID) \
                WHERE Dim_Songs.Title = %s AND Dim_Artists.Name = %s AND Dim_Songs.Duration = %s") 

# Define create and drop query lists

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
