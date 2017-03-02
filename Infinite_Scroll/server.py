from flask import Flask, render_template
import json
from pprint import pprint

app = Flask(__name__)





@app.route('/')
def index():
    with open('pins_formatted.json') as data_file:    
        data = json.load(data_file)
    return render_template("page_of_pins.html")

