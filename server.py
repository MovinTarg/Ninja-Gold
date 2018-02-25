from flask import Flask, render_template, session, request, redirect
import random
import time

app = Flask(__name__)
app.secret_key = 'movintarg'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', gold=session['gold'], activity=session['activity'])

@app.route('/process_money', methods=['GET', 'POST'])
def process_money():
    if request.form['building'] == 'farm':
        number = random.randrange(10, 21)
        session['gold'] += number
        session['activity'].append('Earned {} gold from the farm!'.format(int(number)) + str(time.strftime("  (%d/%m/%Y %I:%M %p)")))
    if request.form['building'] == 'cave':
        number = random.randrange(5, 11)
        session['gold'] += number
        session['activity'].append('Earned {} gold from the cave!'.format(int(number)) + str(time.strftime("  (%d/%m/%Y %I:%M %p)")))
    if request.form['building'] == 'house':
        number = random.randrange(2, 6)
        session['gold'] += number
        session['activity'].append('Earned {} gold from the house!'.format(int(number)) + str(time.strftime("  (%d/%m/%Y %I:%M %p)")))
    if request.form['building'] == 'casino':
        number = random.randrange(-50, 51)
        session['gold'] += number
        if number < 0:
            session['activity'].append('Lost {} gold in the casino!'.format(int(number*-1)) + str(time.strftime("  (%d/%m/%Y %I:%M %p)")))
        else:
            session['activity'].append('Earned {} gold from the casino!'.format(int(number)) + str(time.strftime("  (%d/%m/%Y %I:%M %p)")))
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('activity')
    return redirect('/')

app.run(debug=True)
