import mysql.connector
from mysql.connector import Error


def delete_data(empid):
 
    query = "DELETE FROM employees WHERE emp_no = %s"
 
    try:
        db = mysql.connector.connect(host=os.environ['HOST'],user='USERNAME',passwd='PASSWORD', port='PORT', database='kart')
        if db.is_connected():
            print('Connected to MySQL database')
        cursor = db.cursor()
        cursor.execute(query, (empid,))
        print(cursor.rowcount, "record(s) deleted")

 
        # accept the change
        db.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        db.close()
 
def lambda_handler(event, context):
    empid=1006
    delete_data(empid)