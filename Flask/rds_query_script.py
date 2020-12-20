
import pymysql


# configuration details

endpoint = "respyre-labs.chganerodhca.us-east-2.rds.amazonaws.com"
username = "respyre_asthma"
password = "airflow884"
database_name = "vic_cities"



## establish connection

connection = pymysql.connect(endpoint,user = username,passwd = password,db=database_name)


def data_retrieve_lambda():
    cursor = connection.cursor()
    cursor.execute('SELECT * from cities')
    rows = cursor.fetchall()

    for i in rows:
        print("{0} {1} {2}".format(i[0], i[1], i[2]))


data_retrieve_lambda()
