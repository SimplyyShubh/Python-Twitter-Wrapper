from flask import Flask, jsonify, request
import influencer
import asyncio

app = Flask(__name__)
app.secret_key = "bruhmomento911"

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

## ENDPOINT ROUTES ##

@app.route('/tweets')
def get_influencer_tweets():
    return jsonify(influencer.asyncio.new_event_loop().run_until_complete(influencer.getInfTweets()))

if __name__ == "__main__":
    app.run(debug=True)