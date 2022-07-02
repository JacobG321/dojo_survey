
from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['first_name'] = request.form["first_name"]
    session['last_name'] = request.form["last_name"]
    session['location'] = request.form["location"]
    session['fav_language'] = request.form["fav_language"]
    session['comments'] = request.form["comments"]
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')