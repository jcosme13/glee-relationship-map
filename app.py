#from PIL import Image
import base64
from flask import Flask, render_template,request
import sqlite3
import functools
import operator
import os

IMG_FOLDER = os.path.join('static', 'images')

app = Flask('app')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/', methods = ['GET'])
def home():
    conn = sqlite3.connect('glee-rel.db')
    c = conn.cursor()

    c.execute('SELECT DISTINCT ent FROM entries ORDER BY RANDOM() LIMIT 2')
    results = c.fetchall()

    res = convertTuple(results)

    c.execute('SELECT img FROM entries WHERE ent="Rachel"')
    img = c.fetchall()

    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], img)
    #print(img)
    #print(full_filename)

    img = convertTuple(img[0])
    print(img)
    
    # Render the homepage 
    return render_template("/index.html", res=res, img=img)

@app.route('/map', methods = ['GET'])
def map():
    return render_template("/glee-map.html")

def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

app.run(host='0.0.0.0', port=8080)
