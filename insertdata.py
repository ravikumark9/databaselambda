import mysql.connector
from mysql.connector import Error
 
#def emp_info(emp_no, birth_date, first_name, last_name, gender, hire_date):
def emp_info(empdetails):
    query = "INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
#args = (emp_no, birth_date, first_name, last_name, gender, hire_date)
 
    try:
        db = mysql.connector.connect(host='mytestdb.czznuh47qfib.us-east-2.rds.amazonaws.com',user='root',passwd='scsbbrc321', database='kart')
        if db.is_connected():
            print('Connected to MySQL database')
        cursor = db.cursor()
        cursor.executemany(query, empdetails)
    
        db.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        db.close()
 
def lambda_handler(event, context):
    empdetails = [('1006','2001-05-01','sruthi','','F','2016-01-8'),
             ('1011','1981-7-2','hari','prasad','M','2013-11-1')]             
    emp_info(empdetails)
    
