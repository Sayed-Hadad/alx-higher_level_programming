--  a script that creates the MySQL server user user_0d_1 with all PRIVILEGES
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'  IDENTIFIED BY 'user_0d_1_pwd';
-- GRANT This user all privileges
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
