"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask ,render_template, request
from module1 import Distance, Printer
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template("index.html")


@app.route('/words', methods=["POST"])
def words():
    str1 = request.form.get("string1")
    str1len = len(str1)
    str2 = request.form.get("string2")
    str2len = len(str2)
    if not str1 or not str2:
        return "Not implemented yet"
    else:
        m = Distance(str1,str2)
        l = Printer(str1,str2,m)

        return render_template("matrix.html", str1len=str1len, str2len=str2len, m=m, l=l, str1=str1)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

