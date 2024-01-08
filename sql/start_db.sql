/* coords.db */
CREATE TABLE sqlite_sequence(name, seq);

CREATE TABLE Location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

/* userbase.db */
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE sqlite_sequence(name, seq);