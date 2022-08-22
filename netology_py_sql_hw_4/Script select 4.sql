/* количество исполнителей в каждом жанре */
SELECT genre.name, COUNT(*) FROM genre 
       JOIN genre_mus 
       ON genre.id = genre_mus.genre_id
       JOIN musician 
       ON genre_mus.musician_id = musician.id
 GROUP BY genre.name
 ORDER BY COUNT(musician.name) DESC;


/* количество треков, вошедших в альбомы 2019-2020 годов */
SELECT COUNT(*) AS count_track FROM track 
       JOIN album 
       ON track.album_id = album.id
 WHERE release_date BETWEEN 2019 AND 2020;


/* средняя продолжительность треков по каждому альбому */
SELECT album.name, ROUND(AVG(time), 2) AS AVG_album_sec FROM track 
       JOIN album 
       ON track.album_id = album.id
 GROUP BY album.name
 ORDER BY album.name;


/* все исполнители, которые не выпустили альбомы в 2020 году */
SELECT DISTINCT musician.name FROM album 
       JOIN album_mus 
       ON album.id = album_mus.album_id
       JOIN musician 
       ON album_mus.musician_id = musician.id
 WHERE release_date != 2020
 ORDER BY musician.name;
       

/* названия сборников, в которых присутствует конкретный исполнитель 'Fever 333' */
SELECT DISTINCT collection.name FROM collection 
       JOIN track_coll 
       ON collection.id = track_coll.collection_id
       JOIN track 
       ON track_coll.track_id = track.id
 WHERE track.name IN (
       SELECT track.name FROM musician 
              JOIN album_mus 
              ON musician.id = album_mus.album_id 
              AND musician.name = 'Fever 333'
              JOIN album 
              ON album_mus.album_id = album.id
              JOIN track 
              ON track.album_id = album.id);
     
      
      
/* название альбомов, в которых присутствуют исполнители более 1 жанра */
SELECT album.name FROM musician 
       JOIN album_mus 
       ON musician.id = album_mus.album_id 
       JOIN album 
       ON album_mus.album_id = album.id
 WHERE musician.name IN (
       SELECT musician.name FROM musician 
              JOIN genre_mus 
              ON musician.id = genre_mus.musician_id
              JOIN genre 
              ON genre_mus.genre_id = genre.id
        GROUP BY musician.name
       HAVING COUNT(genre.name) > 1); 
      
       
/* наименование треков, которые не входят в сборники */
SELECT track.name FROM track 
 WHERE track.name NOT IN (
       SELECT DISTINCT track.name FROM track
              JOIN track_coll 
              ON track.id = track_coll.track_id
              JOIN collection 
              ON track_coll.collection_id = collection.id);



/* исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько) */
SELECT DISTINCT musician.name, time AS time_sec FROM musician 
       JOIN album_mus 
       ON musician.id = album_mus.musician_id 
       JOIN album 
       ON album_mus.album_id = album.id
       JOIN track 
       ON track.album_id = album.id
 WHERE time = (SELECT MIN(time) FROM track);


/* название альбомов, содержащих наименьшее количество треков */
SELECT album.name, COUNT(*)  FROM album
       JOIN track 
       ON track.album_id = album.id
 GROUP BY album.name
HAVING COUNT(track) = (SELECT MIN(time) FROM track); 
