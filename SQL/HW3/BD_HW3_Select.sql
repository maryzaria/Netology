-- Название и продолжительность самого длительного трека.
SELECT song_name, duration FROM song
WHERE duration = (SELECT max(duration) FROM song);

-- Название треков, продолжительность которых не менее 3,5 минут
SELECT song_name, duration FROM song
WHERE duration > 210
ORDER BY duration DESC;

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT digest_name, digest_year FROM digest
WHERE digest_year BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова
SELECT singer_name FROM singer s 
WHERE singer_name NOT LIKE '% %'

-- Название треков, которые содержат слово «мой» или «my»
SELECT song_name FROM song
WHERE song_name LIKE '%мой%' OR song_name LIKE '%My%';

-- Количество исполнителей в каждом жанре
SELECT name, COUNT(s.singer_id) count FROM genre g
JOIN singergenre sg ON g.genre_id = sg.genre_id 
JOIN singer s ON sg.singer_id = s.singer_id 
GROUP BY name
ORDER BY count DESC;

-- Количество треков, вошедших в альбомы 2019–2020 годов
SELECT COUNT(s.song_id) FROM album a 
JOIN song s ON a.album_id = s.album_id 
WHERE a.album_year BETWEEN 2019 AND 2020;
-- Количество треков, вошедших в альбомы 2019–2020 годов с названием альбомов
SELECT a.album_name, COUNT(s.song_id) FROM album a 
JOIN song s ON a.album_id = s.album_id 
WHERE a.album_year BETWEEN 2019 AND 2020
GROUP BY a.album_name;

-- Средняя продолжительность треков по каждому альбому
SELECT album_name an, AVG(duration) avg FROM album a 
JOIN song s ON a.album_id = s.album_id 
GROUP BY an
ORDER BY avg DESC;

-- Все исполнители, которые не выпустили альбомы в 2020 году
SELECT singer_name FROM singer s 
JOIN singeralbum sa ON s.singer_id = sa.singer_id 
JOIN album a ON sa.album_id = a.album_id 
WHERE NOT a.album_year = 2020
GROUP BY singer_name;

-- Названия сборников, в которых присутствует конкретный исполнитель
SELECT digest_name FROM digest d
JOIN songdigest sd ON d.digest_id = sd.digest_id 
JOIN song ON sd.song_id = song.song_id 
JOIN album a ON song.album_id = a.album_id 
JOIN singeralbum sa ON a.album_id = sa.album_id 
JOIN singer ON sa.singer_id = singer.singer_id 
WHERE singer.singer_name = 'Фредди Меркьюри'
GROUP BY digest_name;

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра
SELECT album_name FROM album a 
JOIN singeralbum sa ON a.album_id = sa.album_id 
JOIN singer s ON sa.singer_id = s.singer_id 
JOIN singergenre sg ON s.singer_id = sg.singer_id  
JOIN genre g ON sg.genre_id = g.genre_id 
GROUP BY album_name 
HAVING count(g.genre_id) > 1;

-- Наименования треков, которые не входят в сборники
SELECT song_name FROM song s
LEFT JOIN songdigest sd ON s.song_id = sd.song_id 
LEFT JOIN digest d ON sd.digest_id = d.digest_id 
WHERE d.digest_name is NULL; 

-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек
SELECT DISTINCT singer_name, min(song.duration) FROM singer s
JOIN singeralbum sa ON s.singer_id = sa.singer_id
JOIN album a ON sa.album_id = a.album_id
JOIN song ON a.album_id = song.album_id 
WHERE song.duration = (SELECT min(duration) FROM song)
GROUP BY singer_name; 

-- Названия альбомов, содержащих наименьшее количество треков
SELECT album_name, count(s.song_id) FROM album a 
JOIN song s ON a.album_id = s.album_id 
GROUP BY album_name
HAVING count(s.song_id) = 1;