from flask import Flask, jsonify, render_template
import requests

app= Flask(__name__)

@app.route("/")
def get_data():
    try:
        url = 'http://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        if response.status_code == 200:
            data=response.json()
            return jsonify(data)
        else:
            return jsonify(f"Error: Failed to fetch data from {url}, Status Code: {response.status_code}")
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__=='__main__':
    app.run(debug=True)