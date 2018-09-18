import mysql.connector
from mysql.connector import Error


def lambda_handler(event, context):

    """ Connect to MySQL database """
    
    try:
        db = mysql.connector.connect(host=os.environ['HOST'],user='USERNAME',passwd='PASSWORD', port='PORT', database='kart')
        if db.is_connected():
            print('Connected to MySQL database')
            print db
            cur = db.cursor()
            cur.execute("select * from employees")
            myresult = cur.fetchall()

            for x in myresult:
                print(x)
    except Error as e:
        print(e)
 
    finally:
        db.close()
 
