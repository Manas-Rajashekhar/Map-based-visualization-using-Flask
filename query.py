import pymysql
import geocoding as gc
import distance as dt
import folium
# configuration details

endpoint = "respyre-labs.chganerodhca.us-east-2.rds.amazonaws.com"
username = "respyre_asthma"
password = "airflow884"
database_name = "vic_cities"

## establish connection

connection = pymysql.connect(endpoint,user = username,passwd = password,db=database_name)


def hospital_data():
    cursor = connection.cursor()
    query = 'SELECT * from Hospitals'
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows



