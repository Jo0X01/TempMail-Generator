import hashlib
import webbrowser
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

APIs = []
RAPID_LINK = "https://rapidapi.com/calvinloveland335703-0p6BxLYIH8f/api/temp-mail44"
TEMP_NEW_MAIL_API = "https://temp-mail44.p.rapidapi.com/api/v3/email/new"
TEMP_READ_MAIL_API = "https://temp-mail44.p.rapidapi.com/api/v3/email/%s/messages"
RAPID_API_KEYS = [
    "14bL6wjGCpnjZ7NF6Y6wHbTVqobUFvDrDD1SRJLWQpwKRf7J", # 100
    "73bf9805a4msh7ea2d4df7e80c66p1d6cb8jsnc953dcc4018e", # 200
    "22595dcd2emsh02a3fa46b810f78p1cb4b2jsn97d14ad367c9"
]
KEY = 0
TEMP_MAIL_HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEYS[KEY],
    "X-RapidAPI-Host": "temp-mail44.p.rapidapi.com"
}

class Email:
    TOKEN:str = None
    EMAIL:str = None
    HASH:str = None
    def __init__(self,e,t):
        self.EMAIL = e
        self.TOKEN = t
        self.HASH = hashlib.md5(f"[{self.EMAIL}]:[{self.TOKEN}]".encode()).hexdigest()
    def ReadInbox(self):
        return requests.get(TEMP_READ_MAIL_API % self.EMAIL,headers=TEMP_MAIL_HEADERS).json()
    def __repr__(self):
        return self.HASH

Emails:list[Email] = []

def Generate():
    global KEY
    TEMP_MAIL_HEADERS['X-RapidAPI-Key'] = RAPID_API_KEYS[KEY] #random.choice(RAPID_API_KEYS)
    response = requests.post(TEMP_NEW_MAIL_API, headers=TEMP_MAIL_HEADERS)
    email_data = response.json()
    if not email_data.get('email'):
        KEY+=1
        if KEY >= len(RAPID_API_KEYS):
            return email_data
        return Generate()
    result = Email(email_data['email'],email_data['token'])
    Emails.append(result)
    return result


@app.route('/')
def index():
    return open('assets/index.html',"rb").read().decode()  # Your HTML file goes here

@app.route('/generate')
def generate():
    email = Generate()
    return jsonify({"email": email.EMAIL,"token":email.HASH})

@app.route('/inbox')
def inbox():
    _generated = request.args.get('tk')
    email = next((e for e in Emails if e.HASH == _generated), None)

    if email == None:
        return jsonify({"messages": []})

    return jsonify({"messages": list(reversed(email.ReadInbox()))})

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5555/")
    app.run(debug=True,port=5555)