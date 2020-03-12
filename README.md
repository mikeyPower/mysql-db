# mysql-db

To install MySQL, update the package index on your server with apt:

    $ sudo apt update
    
Then install the default package:

    $ sudo apt install mysql-server
    
TO open up the MySQL prompt from your terminal

    $ sudo mysql

To create your database run the following command

     mysql> CREATE DATABASE IF NOT EXISTS mickpower$quotes;
       
In order to see your database run the following command

    mysql> SELECT DATABASE();
    +------------------+
    | DATABASE()       |
    +------------------+
    | mickpower$quotes |
    +------------------+
    1 row in set (0.00 sec)
    
    
As an example we are going to create a table called quotes within our database which will store the quotes that are being pulled from the daily script

    mysql> CREATE TABLE IF NOT EXISTS quotes (
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
    
    
Now in order to ensure that only a single record is added daily and no more we are going to make the quote_date column a UNIQUE column to ensure duplicates are not added

    mysql> alter table quotes
        -> ADD CONSTRAINT date_unique UNIQUE (quote_date);
    Query OK, 0 rows affected (0.09 sec)
    Records: 0  Duplicates: 0  Warnings: 0
    
We can now see this represented in the table below

    mysql> describe quotes;
    +------------+--------------+------+-----+---------+----------------+
    | Field      | Type         | Null | Key | Default | Extra          |
    +------------+--------------+------+-----+---------+----------------+
    | quote_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
    | quote      | varchar(255) | NO   |     | NULL    |                |
    | quote_date | date         | YES  | UNI | NULL    |                |
    | author     | varchar(255) | NO   |     | NULL    |                |
    +------------+--------------+------+-----+---------+----------------+
    4 rows in set (0.00 sec)
    

