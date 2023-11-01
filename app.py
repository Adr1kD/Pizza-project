from flask import Flask, render_template, request, redirect, json
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/', methods=['GET', 'POST'])
def Register_page():
    return render_template('login.html')

@app.route('/hello')
def hello_user():
    return render_template('hello.html')

@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/registration', methods=['GET', 'POST'])
def Register_page1():
    if request.method == "POST":
        attempted_username = request.form['Username']
        attempted_password = request.form['Password']
        attempted_email = request.form['Email']

        with open('data.json', 'r') as outfile:
            data = json.load(outfile)

        for user in data:
            if user['email'] == attempted_email:
                return render_template('registration.html', error_message="User with this email already exists.")
        
        for user in data:
            if user['Username'] == attempted_email:
                return render_template('registration.html', error_message="User with this username already exists.")
            

        d = {"email": "", "pass": "", "user": ""}
        d['user'] = attempted_username
        d['pass'] = attempted_password
        d['email'] = attempted_email
        data.append(d)

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        if request.form['Username'] == '' or request.form['Password'] == '' or request.form['Email'] == '':
            return 'Invalid Credentials. Please try again.'
        else:
            return render_template('login.html')
    else:
        return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        #attempted_username = request.form['Username']
        #attempted_password = request.form['Password']
        #attempted_email = request.form['Email']

        with open('data.json', 'r') as outfile:
            data = json.load(outfile)

        for user in data:
            if request.form['Username'] == user['user'] and request.form['Password'] == user['pass'] and request.form['Email'] == user['email']:
                #return redirect('/main')
                return 'SUCCESSFULLY LOGGEDIN'

        return "User not found"


@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('bcd.html')

if __name__ == '__main__':
    app.run(debug=True)
