from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

def send_message(chat_id, text):
     # Замените на токен вашего бота
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()



@app.route('/', methods=['GET', 'POST'])
def index():
    message_sent = False
    if request.method == 'POST':
        chat_id = request.form['chat_id']
        text = request.form['text']
        send_message(chat_id, text)
        message_sent = True
    return render_template('index.html', message_sent=message_sent)
