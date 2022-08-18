INSERT INTO genre (id, name)
VALUES (1, 'Панк-рок'), (2, 'Рок'), (3, 'Рэп'), 
       (4, 'Джаз'), (5, 'Шансон'), (6, 'Рок-н-ролл');


INSERT INTO musician (id, name)
VALUES (1, 'Green Day'), (2, 'The Offspring'), (3, 'Порнофильмы'),
       (4, 'Fever 333'), (5, 'Linkin Park'), (6, 'Lumen'), (7, 'Red Hot Chili Peppers'), 
       (8, 'Anacondaz'), (9, 'Eminem'),
       (10, 'Луи Армстронг'),
       (11, 'Михаил Круг'), (12, 'Ирина Круг'),
       (13, 'Элвис Пресли');


INSERT INTO genre_mus(id, genre_id, musician_id)
VALUES (1, 1, 1), (2, 1, 2), (3, 1, 3),
       (4, 2, 4), (5, 2, 5), (6, 2, 6), (7, 2, 7),
       (8, 3, 8), (9, 3, 9),
       (10, 4, 10),
       (11, 5, 11), (12, 5, 12),
       (13, 6, 13),
       (14, 1, 7), (15, 2, 1), (16, 2, 2), (17, 2, 3), (18, 3, 4), (19, 3, 5);


INSERT INTO album (id, name, release_date)
VALUES (1, 'Nimrod.', 1997), (2, 'Smash', 1994), (3, 'Это пройдёт', 2020),
       (4, 'Strength in Numb333rs', 2019), (5, 'Hybrid Theory', 2000), (6, 'Мир', 2009), (7, 'One Hot Minute', 1995),
       (8, 'Без паники', 2013), (9, 'The Eminem Show', 2002), (10, 'Encore', 2004),
       (11, 'Satchmo at Pasadena', 1951),
       (12, 'Жиган-лимон', 1994), (13, 'Шанель', 2013),
       (14, 'Elvis Presley', 1956), (15, 'Follow That Dream', 1962);


INSERT INTO album_mus(id, musician_id, album_id)
VALUES (1, 1, 1), (2, 2, 2), (3, 3, 3), 
       (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7), 
       (8, 8, 8), (9, 9, 9), (10, 9, 10),
       (11, 10, 11),
       (12, 11, 12), (13, 12, 13),
       (14, 13, 14), (15, 13, 15);


INSERT INTO track (id, name, time, album_id)
VALUES (1, 'Good Riddance', 2.34, 1), (2, 'Walking Alone', 2.45, 1), 
       (3, 'Gotta Get Away', 3.52, 2),
       (4, 'Это пройдёт', 3.56, 3), (5, 'Дядя Володя', 4.17, 3),(6, 'Нас догонит любовь', 3.47, 3),
       (7, 'Burn It', 3.51, 4), (8, 'One of Us', 3.24, 4),
       (9, 'In the End', 3.36, 5), (10, 'Crawling', 3.29, 5), (11, 'One Step Closer', 2.36, 5), (12, 'Papercut', 3.05, 5),
       (13, 'Вся вера и любовь этого мира', 4.09, 6), (14, 'Дотянуться до звезды', 3.07, 6),
       (15, 'My Friends', 4.02, 7),
       (16, 'Семь миллиардов', 2.55, 8), (17, 'Не учи меня как жить', 2.05, 8),
       (18, 'White America', 5.24, 9), (19, 'Cleanin Out My Closet', 4.58, 9), (20, 'Without Me', 4.50, 9), (21, 'Sing for the Moment', 5.39, 9),
       (22, 'Like Toy Soldiers', 4.57, 10), (23, 'Mosh', 5.18, 10),
       (24, 'Back Home Again in Indiana', 5.31, 11), (25, 'Baby, It''s Cold Outside', 5.42, 11), (26, 'Way Down Yonder in New Orleans', 5.42, 11),
       (27, 'Кольщик', 4.47, 12), (28, 'Фраер', 2.56, 12),
       (29, 'А он успел', 3.36, 13),
       (30, 'Blue Suede Shoes', 2.00, 14), (31, 'I Got a Woman', 2.25, 14),
       (32, 'Flaming Star', 2.00, 15);


INSERT INTO collection (id, name, release_date)
VALUES (1, 'Весь рок', 2011), (2, 'Панк-рок лучшее', 2012), (3, 'Только на русском', 2013), (4, 'Русские хиты', 2014), 
       (5, 'Рок-н-ролл', 2015), (6, 'Для тренировки', 2016), (7, 'Для отсидочки', 2017), (8, 'Верните мой 2007', 2018);


INSERT INTO track_coll(id, track_id, collection_id)
VALUES (1, 7, 1), (2, 8, 1), (3, 9, 1), (4, 10, 1), (5, 11, 1), (6, 12, 1), (7, 13, 1), (8, 14, 1), (9, 15, 1),
       (10, 1, 2), (11, 2, 2), (12, 4, 2), (13, 5, 2),
       (14, 4, 3), (15, 5, 3), (16, 6, 3), (17, 13, 3), (18, 14, 3), (19, 16, 3), (20, 17, 3), (21, 27, 3), (22, 28, 3), (23, 29, 3),
       (24, 4, 4), (25, 5, 4), (26, 13, 4), (27, 17, 4), (28, 27, 4),
       (29, 30, 5), (30, 31, 5), (31, 32, 5),
       (32, 2, 6), (33, 3, 6), (34, 4, 6), (35, 7, 6), (36, 9, 6), (37, 10, 6), (38, 11, 6), (39, 12, 6), (40, 14, 6),
       (41, 9, 7), (42, 27, 7), (43, 28, 7),
       (44, 7, 8), (45, 8, 8), (46, 18, 8), (47, 20, 8), (48, 22, 8), (49, 23, 8);