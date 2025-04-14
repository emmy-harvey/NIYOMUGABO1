Optional: Fake sensor data sender  file


 

 


from flask import Flask, render_template, request, redirect


import sqlite3


from datetime import datetime


 


app = Flask(__name__)


 


def init_db():


    with
sqlite3.connect("database.db") as conn:


        c =
conn.cursor()


        c.execute('''


            CREATE
TABLE IF NOT EXISTS sensor_data (


                id
INTEGER PRIMARY KEY AUTOINCREMENT,


               
humidity REAL,


               
temperature REAL,


               
soil_moisture REAL,


               
timestamp TEXT


            )


        ''')


        conn.commit()


 


@app.route('/', methods=['GET'])


def index():


    with
sqlite3.connect("database.db") as conn:


        c =
conn.cursor()


       
c.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT
10")


        data =
c.fetchall()


    return
render_template('index.html', data=data)


 


@app.route('/submit', methods=['POST'])


def submit():


    humidity =
request.form.get('humidity')


    temperature =
request.form.get('temperature')


    soil_moisture = request.form.get('soil_moisture')


    timestamp
= datetime.now().strftime('%Y-%m-%d %H:%M:%S')


 


    with
sqlite3.connect("database.db") as conn:


        c =
conn.cursor()


       
c.execute("INSERT INTO sensor_data (humidity, temperature,
soil_moisture, timestamp) VALUES (?, ?, ?, ?)",


                  (humidity, temperature,
soil_moisture, timestamp))


        conn.commit()


   


    return
redirect('/')


 


if __name__ == '__main__':


    init_db()


   
app.run(debug=True)


 


 


 


 


 


 


 

