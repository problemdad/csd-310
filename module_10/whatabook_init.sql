# JOSHUA HAMMERLING
# WHATABOOK INIT FILE

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1212 Sesame Street, Bellevue, NE 68123');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('CISSP All-in-One Exam Guide, Ninth Edition', 'Shin Harris', 'CISSP All In One Exam Guide');

INSERT INTO book(book_name, author, details)
    VALUES('Destination CISSP: A Concise Guide', 'Rob Witcher', 'A concise study guide for the CISSP Exam');

INSERT INTO book(book_name, author, details)
    VALUES('ISC2 CISSP Certified Information Systems Security Professional Official Study Guide', 'Mike Chapple', "The official ISC2 CISSP Study Guide");

INSERT INTO book(book_name, author, details)
    VALUES('CISSP For Dummies', 'Lawrence Miller', 'CISSP for Dummies');

INSERT INTO book(book_name, author, details)
    VALUES('How To Think Like A Manager for the CISSP Exam', 'Luke Ahmed', 'Changing your mindset for the CISSP exam');

INSERT INTO book(book_name, author)
    VALUES("Star Wars Episode III: Revenge of the Sith", 'Matthew Stover');

INSERT INTO book(book_name, author)
    VALUES('Star Wars Episode I: The Phantom Menace', 'Terry Brooks');

INSERT INTO book(book_name, author)
    VALUES('Star Wars Episode II: Attack of the Clones', 'R.A. Salvatore');

INSERT INTO book(book_name, author)
    VALUES('Rogue One: A Star Wars Story', 'Alexander Freed');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Luke', 'Skywalker');

INSERT INTO user(first_name, last_name)
    VALUES('Darth', 'Vader');

INSERT INTO user(first_name, last_name)
    VALUES('Han', 'Solo');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Luke'), 
        (SELECT book_id FROM book WHERE book_name = 'CISSP For Dummies')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Darth'),
        (SELECT book_id FROM book WHERE book_name = 'Star Wars Episode III: Revenge of the Sith')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Han'),
        (SELECT book_id FROM book WHERE book_name = 'Rogue One: A Star Wars Story')
    );
