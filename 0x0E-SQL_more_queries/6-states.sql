-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use this database to insert tables in
USE hbtn_0d_usa;
-- create the table states
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
