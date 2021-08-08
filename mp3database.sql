CREATE TABLE users
(user_id		SERIAL			NOT NULL,
 user_email		VARCHAR(128)	NOT NULL,
 user_name		VARCHAR(128)	NOT NULL,
 user_password 	VARCHAR(128)	NOT NULL
);

DROP TABLE users;

SELECT * FROM users

DELETE FROM users