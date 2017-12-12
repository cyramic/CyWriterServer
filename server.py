import logging
import logmatic
import sqlite3
from os import path
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logmatic.JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def create_app(config=None, environment=None):
    app = Flask(__name__)
    CORS(app)
    return app

app = create_app()

@app.route("/chapter-list/<int: docid>")
def chapterlist(docid):
	db = sqlite3.connect('data/test')
	cursor = db.cursor()
	#cursor.execute("SELECT * FROM chapter WHERE documentid = ? ORDER BY sortorder ASC", (docid,))
	#rows = cursor.fetchall()
	db.close()

	#return jsonify(rows)
	return false

@app.route("/doc-list")
def doclist():
	db = sqlite3.connect('data/test')
	cursor = db.cursor()
	cursor.execute("SELECT * FROM document ORDER BY title ASC")
	rows = cursor.fetchall()
	db.close()

	return jsonify(rows)

@app.route("/save-doc/<int: docid>")
def save_document(docid):
	db = sqlite3.connect('data/test')
	cursor = db.cursor()
	# get post variables here...
	
	return false

# Should be modify/save instead of just add...
@app.route("/add-doc/<path:doctitle>")
def add_document(doctitle):
	db = sqlite3.connect('data/test')
	cursor = db.cursor()
	cursor.execute("INSERT OR IGNORE INTO document(title) VALUES ( ? )", (doctitle,))
	db.commit()
	db.close()
	return "Sucess"

@app.route("/init")
def initialize():
	db = sqlite3.connect('data/test')
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS document(id INTEGER PRIMARY KEY, Created DATETIME DEFAULT CURRENT_TIMESTAMP, title TEXT UNIQUE)")
	db.commit()
	cursor.execute("CREATE TABLE IF NOT EXISTS chapter(id INTEGER PRIMARY KEY, documentid INTEGER, Created DATETIME DEFAULT CURRENT_TIMESTAMP, title TEXT, documenttext TEXT, sortorder INTEGER)")
	db.commit()
	db.close()
	return "Done"

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, threaded=True)
	
	

