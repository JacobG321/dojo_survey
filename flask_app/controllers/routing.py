
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import Users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'dojo_location' : request.form["dojo_location"],
        'favorite_language' : request.form["favorite_language"],
        'comments' : request.form["comments"],
    }
    session['first_name'] = request.form["first_name"]
    session['last_name'] = request.form["last_name"]
    session['dojo_location'] = request.form["dojo_location"]
    session['favorite_language'] = request.form["favorite_language"]
    session['comments'] = request.form["comments"]

    if not Users.validate_user(data):
        return redirect('/')

    Users.save(data)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')