#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", title = 'FScrapy')

@app.route('/add/')
def add():
    fobj = open('data.txt')
    j = fobj.readlines()
    for i in j:
        return i

@app.route('/search/')
def search():
    return 'Please enter file name to search with its type(for ex file.py then type= python, file2.txt type=text...)\n'

if __name__ == '__main__':
    app.run(debug = True)
