from flask import Flask
app = Flask(__name__), render_template,request

@app.route("/")
def home():
    return render_template('home.html')
