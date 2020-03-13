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
    

Now in order to start the connection within flask we will do the following

    def connection():
        dbconn = MySQLdb.connect(host = DB_HOST,
                             user = DB_USERNAME,
                             passwd = DB_PASSWORD,
                             db = DB_NAME)
        cur = dbconn.cursor()
        return (cur, dbconn)
        
This will return both the cursor object and database connection in order to commit any changes we make to the DB. The following variables DB_HOST, DB_USERNAME, DB_PASSWORD and DB_NAME are stored as environment variables in order to keep them seperate of the source code.


    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ['DB_HOST']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_NAME = os.environ['DB_NAME']
    
Which are set in the wsgi configuration file as shown below


    os.environ['DB_PASSWORD'] = '*****'
    os.environ['DB_HOST'] = '*****'
    os.environ['DB_USERNAME'] = '*****'
    os.environ['DB_NAME'] = 'mickpower$quotes'
    
    
After the connection is set we may now insert the quote that is pulled daily from our [script](https://github.com/mikeyPower/web-scrapper) directly into the database

    @app.route('/',methods=['GET', 'POST'])
    def index():

        date = getTodaysDate()
        quotes = quote()
        cursor = connection()
        cur = cursor[0]
        db = cursor[1]
        todays_date = datetime.datetime.now()
        today = todays_date.strftime('%Y-%m-%d')
        try:
            cur.execute("INSERT INTO quotes(quote,quote_date,author) VALUES (%s, %s, %s)", (quotes[0], today, quotes[1]))
            db.commit()
        except:
            print()
        return render_template("index.html",quote=quotes[0],author=quotes[1],day=date)
        
 To see if everything is working properly, let's inspect the database and we should see some records
 
    mysql> select * from quotes;
    +----------+-------------------------------------------------------+------------+----------------+
    | quote_id | quote                                                 | quote_date | author         |
    +----------+-------------------------------------------------------+------------+----------------+
    |        1 | Fortune favors the prepared mind.                     | 2020-03-12 |  Louis Pasteur |
    |        2 | My religion is very simple. My religion is kindness.  | 2020-03-13 |  Dalai Lama    |
    +----------+-------------------------------------------------------+------------+----------------+
    2 rows in set (0.01 sec)
    
To see all of this in action head over to this [repository](https://github.com/mikeyPower/cv_site)
