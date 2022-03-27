from flask import Flask, render_template,request
import sqlite3
import functools
import operator

app = Flask('app')

@app.route('/', methods = ['GET'])
def home():
    conn = sqlite3.connect('glee-rel.db')
    c = conn.cursor()

    c.execute('SELECT DISTINCT ent FROM entries ORDER BY RANDOM() LIMIT 2')
    results = c.fetchall()

    res = convertTuple(results)
    
    # Render the homepage 
    return render_template("/index.html", res=res)

@app.route('/map', methods = ['GET'])
def map():
    return render_template("/glee-map.html")

def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str

app.run(host='0.0.0.0', port=8080)
