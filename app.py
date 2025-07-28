# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from phones_data import phone_inventory
from utils import get_platform_data, check_profitability

app = Flask(__name__)
app.secret_key = 'dummy_secret_key'  # for session handling

# Dummy login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    phones = []
    for phone in phone_inventory:
        if phone['stock'] <= 0:
            continue

        platforms = get_platform_data(phone)
        profitable_platforms = [p for p in platforms if check_profitability(p)]

        phones.append({
            'name': phone['name'],
            'condition': phone['condition'],
            'stock': phone['stock'],
            'platforms': profitable_platforms
        })

    return render_template('dashboard.html', phones=phones)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
