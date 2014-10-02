#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for
import fsearch


###static content###app = Flask(__name__, static_url_path='/home/path/to/static')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open(".config") as config:
            for loc in config:

                if "location" in loc:
                    path = loc.split()[-1]

        try:
            value = fsearch.fsearch(path, request.form['type'], request.form['filename'])

        except FileNotFoundError:
            return "No Index file exist. Please run filesearch.py script to index data or setup cron job, setup .config file for your system."
    
        if value:
            return value
        else:
            return "0 result found. Try a different keyword."

    else:
        return render_template('index.html')

#@app.route('/add/')
#def add():
#    return app.send_static_file('')

#@app.route('/search/')
#def search():
#    return app.send_static_file('')


if __name__ == '__main__':
    app.debug = True
    app.run()
