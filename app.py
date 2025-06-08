
from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == 'teste@amlvadvocacia.com.br' and password == '123456':
        session['user'] = {'email': email}
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html', user=session["user"])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
