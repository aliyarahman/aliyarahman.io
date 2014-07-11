# Must be in a file called 'application.py' in order to work on Beanstalk
import flask

application = flask.Flask(__name__) # Must be called 'application' in order to work on Beanstalk

app.run(debug = True) # Comment this out upon deployment to Elastic Beanstalk

@application.route('/')
@application.route('/index')
def index():
  return ("Hello, Beanstalk")
