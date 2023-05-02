from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def hello():
    email = request.form['email']
    password = request.form['password']
    print(email)
    print(password)
    return 'Chegou a api'

app.run()
    

