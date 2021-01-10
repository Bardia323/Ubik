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
#from forms import *
import json
import requests
from werkzeug.datastructures import Headers


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
app.config['SECRET_KEY'] = '3cbf224240f0b822365c90a5f6ebe108b5'

# Return a template
@app.route('/')
def index():
    return render_template('index.html', 
                           Tagline=taglines[randint(0,len(taglines))]
                           .split("Slogan:", 1)[1], 
                           Paragraph= ads[randint(0,len(ads))])

@app.route('/try')
def tryy():
    return render_template('try.html')
    
    
    
""" @app.route('/payment')
def regiter():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form) """


""" @app.route('/Login')
def login():
    def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form) """

@app.route('/Minds/Slogans')
def slogans():
    pass
    
@app.route('/Minds/Reviews')
def reviews():
    pass
@app.route('/Minds/Ads')
def Ads():
    pass
    
# Run the app
def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
