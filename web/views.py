from flask import render_template
from web import app
import requests


#====================================================================
#====================================================================
#====================================================================

def send(user_id,mes):
    acc = "e659874e1b3b2adc4315ef8c90a206d85a0b3cd4d7ac891d4aa253065626d1547191f534499c064160f68"
    payload = {'v': '5.74', 'user_id': user_id,'message': mes,'access_token':acc}
    r = requests.get('https://api.vk.com/method/messages.send', params=payload)
    return r.json()


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/red', methods=['GET', 'POST'])
def red():
    send("150524263","Кто-то нажал на рэд")
    return render_template('red.html')

@app.route('/white', methods=['GET', 'POST'])
def white():
    send("150524263", "Кто-то нажал на вайт")
    return render_template('white.html')