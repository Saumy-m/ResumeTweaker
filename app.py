#imports go below
import os # importing os module to fetch file paths
from flask import Flask, render_template, request # importing necessary functions from flask module

app = Flask(__name__) # creating a Flask application instance

# homepage route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': # checking if the request method is POST
        name = request.form['job-descript'] 
        return "Successful!" # returns the job description
    
    return render_template('index.html') # rendering index.html template 

if __name__ == '__main__': # checking if the script is run directly
    app.run(debug=True, port=5000) # running the Flask application in debug mode