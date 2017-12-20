from flask import Flask


account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

app = Flask(__name__)


# jwt for auth?

@app.route('/')
def defaultMessage():
	return "Add video id to URL"

@app.route('/<url>')
def hello_world(url):

	return "associated JSON data for URL: %s" % url

@app.route('/SMS/<Twiml>', methods=['GET','POST'])
def sms_reply():
	return Twiml

if __name__ == '__main__':
  app.run()
