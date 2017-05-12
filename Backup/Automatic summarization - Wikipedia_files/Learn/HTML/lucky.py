from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def lucky():
	random = randint(1, 10)
	return render_template('lucky.html', lucky_num = random)

if __name__ == '__main__':
	app.run()
