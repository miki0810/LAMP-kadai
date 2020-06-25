import mysql.connector
from flask import *

app = Flask(__name__)

conn = mysql.connector.connect(user='root', password='T19862my@sfc.keio.ac.jp', host='localhost', database='test')
cur = conn.cursor()

cur.execute("select * from info;")

coment = ["","",""]

for row in cur.fetchall():
    coment[0] = row[0]
    coment[1] = row[1]
    coment[2] = row[2]

@app.route("/")
def main():
    return  jsonify(coment)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
