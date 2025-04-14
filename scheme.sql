-- Tabulka uživatelů
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    role VAR NOT NULL
);

INSERT INTO users (username, password, role)
VALUES
    ("a", "a", "admin"),
    ("u", "u", "user");

-- Tabulka závodů s user_id a AUTOINCREMENT
CREATE TABLE races (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Vložení závodů s přiřazeným uživatelem
-- (admin má id = 1, user má id = 2)
INSERT INTO races (name, description, user_id)
VALUES
    ("Bahrajn", "prvni zavod sezony", 1),
    ("Austrálie", "druhy zavod sezony", 2);
