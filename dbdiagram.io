//// -- LEVEL 1
//// -- Tables and References

// Creating tables

Table users {
    user_id VARCHAR [pk]
    first_name VARCHAR
    last_name VARCHAR
    gender CHAR
    level VARCHAR
}

Table songs {
    song_id VARCHAR [pk]
    title VARCHAR
    artist_id VARCHAR
    year INT
    duration NUMERIC
}
Table artists {
    artist_id VARCHAR [pk] 
    name VARCHAR
    location VARCHAR
    latitude NUMERIC
    longitude NUMERIC
}

Table time {
    start_time TIMESTAMP [pk] 
    hour INT
    day INT
    weekday INT
    week INT
    month INT
    year INT
}

Table songplays {
    songplay_id SERIAL [pk] 
    start_time  TIMESTAMP [not null]
    user_id     VARCHAR [not null]
    level       VARCHAR
    song_id     VARCHAR
    artist_id   VARCHAR
    session_id  INT
    location    VARCHAR 
    user_agent  VARCHAR
}

Ref: "songplays"."song_id" > "songs"."song_id"
Ref: "songplays"."artist_id" > "artists"."artist_id"
Ref: "songplays"."user_id" > "users"."user_id"
Ref: "songplays"."start_time" > "time"."start_time"
