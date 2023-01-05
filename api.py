import os
from flask import Flask, jsonify, request
import json
import postFlow as main
import requests

app = Flask(__name__)
app.secret_key = "bruhmomento911"


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

## ENDPOINT ROUTES ##

@app.route('/')
def home():
  return "Hello World!"

@app.route('/test')
def resp():
  resp = "Python-Twitter-BH-Version-1"
  status = "Everything working, all chill"
  return jsonify(resp, status)

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
  # payload = request.get_json()
  # if payload is None:
  #   return jsonify("No payload!")
  # else:
  return "Tweet successfull"

  
@app.route('/postTweet', methods=['POST','GET'])
def postTweet():
  payload = request.get_json()
  if payload is None:
    return jsonify("No payload!")
  else:
    main.postFlow(payload)
    return jsonify(payload)

if __name__ == "__main__":
  app.run()