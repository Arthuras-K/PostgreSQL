/* название и год выхода альбомов, вышедших в 2013 году */
SELECT name, release_date FROM album
WHERE release_date = 2013;


/* название и продолжительность самого длительного трека */
SELECT name, time FROM track
ORDER BY time DESC
LIMIT 1;


/* название треков, продолжительность которых не менее 3,5 минуты */
SELECT name FROM track
WHERE time > 3.5
ORDER BY name;


/* названия сборников, вышедших в период с 2017 по 2020 год включительно */
SELECT name FROM collection
WHERE release_date BETWEEN 2017 AND 2020;


/* исполнители, чье имя состоит из 1 слова */
SELECT name FROM musician
WHERE name NOT LIKE '% %'
ORDER BY name;


/* название треков, которые содержат слово "мой"/"my" */
SELECT name FROM track 
WHERE name ILIKE 'мой%' OR 
      name ~~* '%мой%' OR
      name ~~* '%мой' OR 
      name ~~* 'my%' OR 
      name ~~* '%my%' OR
      name ~~* '%my';