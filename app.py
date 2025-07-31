from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shrine-history')
def shrine_history():
    return render_template('shrine_history.html')

"""
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"New message from {name} ({email}): {message}")
    return f"Thanks {name}, your message has been received!"

"""

if __name__ == '__main__':
    app.run(debug=True)
