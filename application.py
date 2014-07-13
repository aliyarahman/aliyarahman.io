# Must be in a file called 'application.py' in order to work on Beanstalk
from flask import Flask, render_template

application = Flask(__name__) # Must be called 'application' in order to work on Beanstalk

@application.route('/')
def index():
  return render_template("index.html")

application.run(debug = True) # Comment this out upon deployment to Elastic Beanstalk

