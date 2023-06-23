create table if not exists Singers (
singer_id SERIAL primary key,
singer_name VARCHAR(40) unique not null
);

create table if not exists Albums (
album_id SERIAL primary key,
album_name VARCHAR(40) unique not null,
album_year interval year not null
);

create table if not exists SingerAlbum (
singer_id INTEGER references Singers(singer_id),
album_id INTEGER references Albums(album_id),
constraint pk1 primary key (singer_id, album_id)
);

create table if not exists Genres (
genre_id SERIAL primary key,
genre_name VARCHAR(40) unique not null,
description text not null
);

create table if not exists SingerGenre (
singer_id integer references Singers(singer_id),
genre_id integer references Genres(genre_id),
constraint pk2 primary key (singer_id, genre_id)
);

create table if not exists Songs (
song_id SERIAL primary key,
song_name VARCHAR(20) unique not null,
duration interval second not null,
album_id INTEGER references Albums(album_id)
);

create table if not exists Digests (
digest_id SERIAL primary key,
digest_name VARCHAR(20) unique not null,
digest_year interval year not null
);

create table if not exists SongDigest (
song_id integer references Songs(song_id),
digest_id integer references Digests(digest_id),
constraint pk3 primary key (song_id, digest_id)
);