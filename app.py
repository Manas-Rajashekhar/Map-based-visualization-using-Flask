from flask import Flask, render_template , request
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


data = hospital_data()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page_landing():

    return render_template('index.html')


@app.errorhandler(404)
def wrong_address(e):
    return render_template("error.html")

@app.route('/View_all', methods=['GET','POST'])
def View_all():
    if request.method == "POST":
        address = request.form['address']
        km = request.form['km']
        lat, lng = gc.get_geocoding(address)
        closest_info = []
        info = []
        dist = []

        for i in data:
            d = dt.distance(lat, i[0], lng, i[1])
            dist.append(d)
            temp = [i[0], i[1], i[2], i[3], i[4], d]
            info.append(temp)
            dist.sort()

        for each in dist:
            for i in info:
                if each == i[5]:
                    closest_info.append(i)

        map = folium.Map(location=[lat, lng], zoom_start=10)
        folium.TileLayer('Stamen Terrain').add_to(map)
        folium.TileLayer('Stamen Toner').add_to(map)
        folium.TileLayer('Stamen Water Color').add_to(map)
        folium.TileLayer('cartodbpositron').add_to(map)
        folium.TileLayer('cartodbdark_matter').add_to(map)
        folium.LayerControl().add_to(map)

        for i in range(len(closest_info)):
            if closest_info[i][5] < float(km):
                html = """<h4> Hospital name: </h4>""" + closest_info[i][2]+ \
                       """<h4>Type:</h4>""" + closest_info[i][3] + \
                       """<h4>Address:</h4>""" + closest_info[i][4]

                # IFrame
                iframe = folium.IFrame(html=html, width=200, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                marker = folium.Marker(location=[closest_info[i][0], closest_info[i][1]],popup=popup, icon=folium.Icon(color='red', icon='plus'))
                marker.add_to(map)
            else:
                continue

        marker_user = folium.Marker(location=[lat, lng], popup='Current Location',icon=folium.Icon(color='green', icon='user'))
        marker_user.add_to(map)
    return map._repr_html_()




if __name__ == "__main__":
    app.run()
