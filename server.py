
from flask import Flask, render_template,request,redirect  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'Hello'

@app.route('/')         
def index():
    return render_template("count.html")

@app.route('/submit', methods=['POST'])         
def checkout():
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comments = request.form['comments']
    return render_template("submit.html", name = name, language = language, location = location, comments = comments)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  