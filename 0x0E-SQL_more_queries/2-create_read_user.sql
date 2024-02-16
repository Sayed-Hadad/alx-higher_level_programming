-- a script that creates the database hbtn_0d_2 and the user user_0d_2 with READ only privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'  IDENTIFIED BY 'user_0d_2_pwd';
-- gives SELECT access on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
