DROP database IF EXISTS ctf;
CREATE database sharifdb;
USE sharifdb;
CREATE TABLE flag 
(
    flag TEXT
);

CREATE TABLE users 
(
    username TEXT,
    password TEXT
);

INSERT INTO flag VALUES ('SHARIF{testflag}');
INSERT INTO users VALUES ('admin','ezpass');
INSERT INTO users VALUES ('guest','guest');
CREATE USER user@'%' IDENTIFIED BY 'password';
GRANT SELECT ON sharifdb.flag TO 'user'@'%';
GRANT SELECT ON sharifdb.users TO 'user'@'%';
FLUSH PRIVILEGES;