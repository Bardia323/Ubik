# build a flask api in python that has one Get request
import time
import os
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from datetime import datetime
from random import randint

import json


def import_list_from_txt(list_from_txt):
    file_name = list_from_txt
    with open(file_name, "r") as f:
        list_of_strings = f.read()
        return list_of_strings

taglines = import_list_from_txt(os.getcwd()+'/500SlogansforUBIK.txt').split('\n\n')
ads = import_list_from_txt(os.getcwd()+'/500 UBIK for UBIK ads.txt').split('\n\n')

#taglines = import_list_from_txt('C:\\Users\\bardi\\Desktop\\Programs\\UBIK\\APP 1'+'\\500SlogansforUBIK.txt').split('\n\n')
#ads = import_list_from_txt('C:\\Users\\bardi\\Desktop\\Programs\\UBIK\\APP 1'+'\\500 UBIK for UBIK ads.txt').split('\n\n')

# Create a Flask instance
app = Flask(__name__, template_folder='template')

# Return a template
@app.route('/')
def index():
    return render_template('index.html', Tagline=taglines[randint(0,len(taglines))].split("Slogan:", 1)[1], Paragraph= ads[randint(0,len(ads))])

# Run the app
def main():
    app.run()


if __name__ == "__main__":
    main()
