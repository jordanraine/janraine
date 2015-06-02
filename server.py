
from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

janrain_engage_root_url = "https://jordantestapp.rpxnow.com//api/v2/auth_info"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my_url', methods=['POST'])
def my_url():
    token = request.form['token']
    engage_api_params = {
        'apiKey': os.environ['JANRAIN_ENGAGE_API_KEY'],
        'token': token
    }
    user_data = requests.get(janrain_engage_root_url, params=engage_api_params)
    auth_info = user_data.json()
    profile = auth_info['profile']
    name = profile['name']['formatted']
    #store_user_data_in_postgres(name)
    return render_template('logged_in.html', name=name)

if __name__ == "__main__":
app.run(debug=True, port=3000)
