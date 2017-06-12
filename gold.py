from flask import Flask, session, request, redirect, render_template
import random

app = Flask(__name__)

app.secret_key = 'k1313k'

@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'log' in session:
		session['log'] = ''
	data = {}
	data['gold'] = session['gold']
	data['log'] = session['log']
	return render_template('gold.html', data=data)

@app.route('/process_money', methods=['POST'])
def process():
	loc = request.form['building']

	if loc == 'Farm':
		rand = random.randrange(10, 21)
		message = "<div class='won'>You visited the farm and got " + str(rand) + "coins!</div>"
	elif loc == 'Cave':
		rand = random.randrange(5, 11)
		message = "<div class='won'>You visited the cave and got " + str(rand) + " coins!</div>"
	elif loc == 'House':
		rand = random.randrange(2, 6)
		message = "<div class='won'>You visited the house and got " + str(rand) + " coins!</div>"
	elif loc == 'Casino':
		rand = random.randrange(-50, 51)
		if rand < 0:
			win_or_loss = 'lost'
		else:
			win_or_loss = 'won'
		message = "<div class='" + win_or_loss + "'>You visited the casino and " + win_or_loss + " " + str(rand) + " coins!</div>"


	log = session['log']
	session['log'] = message + log
	session['gold'] += rand
	print session['log']
	return redirect('/')

@app.route('/reset')
def reset():
	session['gold'] = 0
	session['log'] = ''
	return redirect('/')

app.run(debug=True)