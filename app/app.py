#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/home/amitt001/mycodes/dgplug/project/app/static')

@app.route('/')
def index():
    return "hey"

@app.route('/add/')
def add():
    return app.send_static_file('data.txt')

@app.route('/search/')
def search():
    return app.send_static_file('search.txt')

if __name__ == '__main__':
    app.debug = True
    app.run()
