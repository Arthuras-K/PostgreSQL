CREATE TABLE IF NOT EXISTS genre (
    ID   SERIAL      PRIMARY KEY,
    name VARCHAR(40) UNIQUE
);


CREATE TABLE IF NOT EXISTS musician (
    ID   SERIAL      PRIMARY KEY,
    name VARCHAR(60) UNIQUE
);


CREATE TABLE IF NOT EXISTS genre_mus (
    ID          SERIAL   PRIMARY KEY,
    genre_id    INTEGER  NOT NULL REFERENCES genre(id),
    musician_id INTEGER  NOT NULL REFERENCES musician(id)
);


CREATE TABLE IF NOT EXISTS album (
    ID           SERIAL      PRIMARY KEY,
    name         VARCHAR(60) NOT NULL,
    release_date INTEGER     CHECK(release_date > 1000 AND release_date < 3000)
);


CREATE TABLE IF NOT EXISTS album_mus (
    ID          SERIAL   PRIMARY KEY,
    musician_id INTEGER  NOT NULL REFERENCES musician(id),
    album_id    INTEGER  NOT NULL REFERENCES album(id)
);


CREATE TABLE IF NOT EXISTS track (
    ID       SERIAL      PRIMARY KEY,
    name     VARCHAR(60) NOT NULL,
    time     INTEGER     NOT NULL CHECK(time > 0 AND time < 90000), 
    album_id INTEGER     REFERENCES album(id)
);


CREATE TABLE IF NOT EXISTS collection (
    ID           SERIAL      PRIMARY KEY,
    name         VARCHAR(60) NOT NULL,
    release_date INTEGER     CHECK(release_date > 1000 AND release_date < 3000)
);


CREATE TABLE IF NOT EXISTS track_coll (
    ID            SERIAL   PRIMARY KEY,
    track_id      INTEGER  NOT NULL REFERENCES track(id),
    collection_id INTEGER  NOT NULL REFERENCES collection(id)
);