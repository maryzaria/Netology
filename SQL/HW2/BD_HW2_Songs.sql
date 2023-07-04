CREATE TABLE IF NOT EXISTS Singer (
singer_id SERIAL PRIMARY key,
singer_name VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Album (
album_id SERIAL PRIMARY KEY,
album_name VARCHAR(40) UNIQUE NOT NULL,
album_year INTERVAL YEAR NOT NULL CHECK (album_year > 1900)
);

CREATE TABLE IF NOT EXISTS SingerAlbum (
singer_id INTEGER REFERENCES Singer(singer_id),
album_id INTEGER REFERENCES Album(album_id),
CONSTRAINT pk1 PRIMARY KEY (singer_id, album_id)
);

CREATE TABLE IF NOT EXISTS Genre (
genre_id SERIAL PRIMARY KEY, 
name VARCHAR(40) UNIQUE NOT NULL,
description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS SingerGenre (
singer_id integer REFERENCES Singer(singer_id),
genre_id integer REFERENCES Genre(genre_id),
CONSTRAINT pk2 PRIMARY KEY (singer_id, genre_id)
);

CREATE TABLE IF NOT EXISTS Song (
song_id SERIAL PRIMARY KEY,
song_name VARCHAR(20) UNIQUE NOT NULL,
duration INTEGER NOT NULL CHECK (duration > 180),
album_id INTEGER REFERENCES Album(album_id)
);

CREATE TABLE IF NOT EXISTS Digest (
digest_id SERIAL PRIMARY KEY,
digest_name VARCHAR(20) UNIQUE NOT NULL,
digest_year INTERVAL YEAR NOT NULL CHECK (digest_year > 1900)
);

CREATE TABLE IF NOT EXISTS SongDigest (
song_id INTEGER REFERENCES Song(song_id),
digest_id INTEGER REFERENCES Digest(digest_id),
CONSTRAINT pk3 PRIMARY KEY (song_id, digest_id)
);