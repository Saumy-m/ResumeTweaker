#imports go below
import os # importing os module to fetch file paths
from flask import Flask, render_template, request # importing necessary functions from flask module

app = Flask(__name__) # creating a Flask application instance

# homepage route
@app.route('/', methods=['GET'])
def home():
    # if request.method == 'POST': # checking if the request method is POST
    #     name = request.form['job-descript'] 
    #     return f"Recieved Job Description: {name}" # returns the job description
    
    return render_template('index.html') # rendering index.html template 

#dynamic results page testing
@app.route('/result', methods=['POST'])
def Job_Descript():
    # 1. Grab the data from the form
    job_description = request.form['job-descript']
    
    # 2. Pass that data into your new output HTML file
    return render_template('result.html', description=job_description)

if __name__ == '__main__': # checking if the script is run directly
    app.run(debug=True, port=5000) # running the Flask application in debug mode