"""
    http://jsonplaceholder.typicode.com/users
"""

from flask import Flask, jsonify, render_template
import requests

app= Flask(__name__)

@app.route("/")
def get_data():    
    url = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    
    if response.status_code ==200:
        data=response.json()
        return jsonify(data)
    else:
        return jsonify("error")
    response.status_code
    
if __name__=='__main__':
    app.run(debug=True)