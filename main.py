#app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Rahul Kumar Paswan!'

@app.route('/dashboard')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')


@app.route('/login')
def login():
    # Render the dashboard template
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
