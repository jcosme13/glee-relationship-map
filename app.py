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
    res = c.fetchall()

    print(res[0])
    print(res[1])

    c.execute('SELECT img FROM entries WHERE ent=?', res[0])
    img1 = c.fetchall()
    img1 = convertTuple(img1[0])

    c.execute('SELECT img FROM entries WHERE ent=?', res[1])
    img2 = c.fetchall()
    img2 = convertTuple(img2[0])

    res = convertTuple(res) 
    # Render the homepage 
    return render_template("/index.html", res=res, img1=img1, img2=img2)

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
