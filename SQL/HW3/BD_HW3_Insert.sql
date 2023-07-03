INSERT INTO singer (singer_id, singer_name) VALUES (DEFAULT, 'Фредди Меркьюри');
INSERT INTO singer (singer_id, singer_name) VALUES (DEFAULT, 'Виктор Цой');
INSERT INTO singer (singer_id, singer_name) VALUES (DEFAULT, 'Майкл Джексон');
INSERT INTO singer (singer_id, singer_name) VALUES (DEFAULT, 'Тейлор Свифт');
INSERT INTO singer (singer_id, singer_name) VALUES (DEFAULT, 'Адель');

INSERT INTO genre (name, description) VALUES ('поп-рок', 'жанр музыки, объединяющий элементы поп-музыки и рок-музыки');
INSERT INTO genre (name, description) VALUES ('рок', 'обобщающее название ряда направлений популярной музыки');
INSERT INTO genre (name, description) VALUES ('рок-н-ролл', 'жанр популярной музыки, получивший распространение в Соединённых Штатах в конце 1940-х — начале 1950-х годов');
INSERT INTO genre (name, description) VALUES ('поп-музыка', 'область массовой культуры, охватывающая различные формы, жанры и стили развлекательной и прикладной музыки 2-й половины XX — начала XXI веков');

INSERT INTO singergenre (singer_id, genre_id) VALUES (1, 1);
INSERT INTO singergenre (singer_id, genre_id) VALUES (2, 2);
INSERT INTO singergenre (singer_id, genre_id) VALUES (3, 3);
INSERT INTO singergenre (singer_id, genre_id) VALUES (4, 4);
INSERT INTO singergenre (singer_id, genre_id) VALUES (5, 4);
INSERT INTO singergenre (singer_id, genre_id) VALUES (3, 4);

INSERT INTO album (album_name, album_year) VALUES ('A Night at the Opera', 1975);
INSERT INTO song (song_name, duration, album_id) VALUES ('Bohemian Rhapsody', 355, 1);
INSERT INTO song (song_name, duration, album_id) VALUES ('Love of My Life', 219, 1);

INSERT INTO album (album_name, album_year) VALUES ('Группа крови', 1988);
INSERT INTO song (song_name, duration, album_id) VALUES ('Спокойная ночь', 368, 2);
INSERT INTO song (song_name, duration, album_id) VALUES ('Группа крови', 287, 2);

INSERT INTO album (album_name, album_year) VALUES ('Thriller', 1983);
INSERT INTO song (song_name, duration, album_id) VALUES ('Billie Jean', 295, 3);

INSERT INTO album (album_name, album_year) VALUES ('Speak Now', 2010);
INSERT INTO song (song_name, duration, album_id) VALUES ('Mine', 232, 4);

INSERT INTO album (album_name, album_year) VALUES ('Lover', 2019);
INSERT INTO song (song_name, duration, album_id) VALUES ('Cruel Summer', 181, 5);
INSERT INTO song (song_name, duration, album_id) VALUES ('ME!', 193, 5);

INSERT INTO album (album_name, album_year) VALUES ('30', 2020);
INSERT INTO song (song_name, duration, album_id) VALUES ('Woman Like Me', 300, 6);

INSERT INTO album (album_name, album_year) VALUES ('Dangerous', 1991);
INSERT INTO song (song_name, duration, album_id) VALUES ('Dangerous', 420, 7);
INSERT INTO song (song_name, duration, album_id) VALUES ('Who Is It', 395, 7);
INSERT INTO song (song_name, duration, album_id) VALUES ('Black or White', 256, 7);

INSERT INTO singeralbum (singer_id, album_id) VALUES (1, 1);
INSERT INTO singeralbum (singer_id, album_id) VALUES (2, 2);
INSERT INTO singeralbum (singer_id, album_id) VALUES (3, 3);
INSERT INTO singeralbum (singer_id, album_id) VALUES (4, 4);
INSERT INTO singeralbum (singer_id, album_id) VALUES (4, 5);
INSERT INTO singeralbum (singer_id, album_id) VALUES (5, 6);
INSERT INTO singeralbum (singer_id, album_id) VALUES (3, 7);

INSERT INTO digest (digest_name, digest_year) VALUES ('Лучшие песни 80-х', 2000);
INSERT INTO digest (digest_name, digest_year) VALUES ('Нестареющая классика', 2010);
INSERT INTO digest (digest_name, digest_year) VALUES ('Хиты на все времена', 2020);

INSERT INTO songdigest (song_id, digest_id) VALUES (3, 1);
INSERT INTO songdigest (song_id, digest_id) VALUES (4, 1);
INSERT INTO songdigest (song_id, digest_id) VALUES (1, 2);
INSERT INTO songdigest (song_id, digest_id) VALUES (2, 2);
INSERT INTO songdigest (song_id, digest_id) VALUES (3, 2);
INSERT INTO songdigest (song_id, digest_id) VALUES (4, 2);
INSERT INTO songdigest (song_id, digest_id) VALUES (5, 2);
INSERT INTO songdigest (song_id, digest_id) VALUES (2, 3);
INSERT INTO songdigest (song_id, digest_id) VALUES (6, 3);
INSERT INTO songdigest (song_id, digest_id) VALUES (3, 3);
INSERT INTO songdigest (song_id, digest_id) VALUES (1, 3);

INSERT INTO album (album_name, album_year) VALUES ('My time', 2023);
INSERT INTO song (song_name, duration, album_id) VALUES ('my own', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('own my', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('oh my god', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('my', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('myself', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('by myself', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('bemy self', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('myself by', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('beemy', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('premyne', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('мой', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('мойка', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('ты мой свет', 200, 8);
INSERT INTO song (song_name, duration, album_id) VALUES ('привет, мойдодыр', 200, 8);