
from flask import Flask, render_template,request,redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'Hello'

@app.route('/')         
def index():
    return render_template("count.html")

@app.route('/submit', methods=['POST'])         
def checkout():
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomments'] = request.form['comments']
    return redirect("/user")
  
@app.route('/user')
def user():
  return render_template('submit.html')
  


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  