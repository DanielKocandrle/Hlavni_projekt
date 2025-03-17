    CREATE TABLE users (
        id  INT PRIMARY KEY,
        username VAR  UNIQUE NOT NULL,
        password varchar NOT NULL
    );

    INSERT INTO users ("username", "password") VALUES ("admin", "admin")

