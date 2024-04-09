from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

def send_message(chat_id, text):
    token = '6415269726:AAHu0ImRKiC-eIxX1gNpP_eN-k23v3qiaF4'  # Замените на токен вашего бота
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}
    response = requests.get(url, params=params)
    return response.json()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        chat_id = request.form['chat_id']
        text = request.form['text']
        send_message(chat_id, text)
        return 'Сообщение отправлено!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
