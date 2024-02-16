-- a script that lists all records of the table second_table of the database hbtn_0c_0
SELECT score, name FROM second_table
where (name IS NOT NULL or name != "")
ORDER BY score DESC;
