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
    
    
Now to show the entire structure of what we just created you can enter

    mysql> describe quotes;
     
Or

    mysql> explain quotes;
    
Which will both return the following result which is the quotes table

    +------------+--------------+------+-----+---------+----------------+
    | Field      | Type         | Null | Key | Default | Extra          |
    +------------+--------------+------+-----+---------+----------------+
    | quote_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
    | quote      | varchar(255) | NO   |     | NULL    |                |
    | quote_date | date         | YES  |     | NULL    |                |
    | author     | varchar(255) | NO   |     | NULL    |                |
    +------------+--------------+------+-----+---------+----------------+
    4 rows in set (0.00 sec)
    
    
