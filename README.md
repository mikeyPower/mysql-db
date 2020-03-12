# mysql-db

In order to see your database run the following command

    mysql> SELECT DATABASE();
    +------------------+
    | DATABASE()       |
    +------------------+
    | mickpower$quotes |
    +------------------+
    1 row in set (0.00 sec)
    
    
As an example we are going to create a table called quotes within our database which will store the quotes that are being pulled from the daily script

    CREATE TABLE IF NOT EXISTS quotes (
    -> quote_id INT AUTO_INCREMENT PRIMARY KEY,
    -> 
    -> quote VARCHAR (255) NOT NULL,
    -> quote_date DATE,
    -> author VARCHAR (255) NOT NULL
    -> );
    
To see that our table has been created run the following command

    mysql> SHOW TABLES;
    +----------------------------+
    | Tables_in_mickpower$quotes |
    +----------------------------+
    | quotes                     |
    +----------------------------+
    1 row in set (0.00 sec)
    
You should see something like above, if you see the following your table has still not been created

    mysql> show tables;
    Empty set (0.00 sec)
    
    
    
