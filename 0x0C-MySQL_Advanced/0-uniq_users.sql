--creates a table users
CREATE TABLE If NOT EXISTS users (  
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY ( id ),
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
