from flask import Flask, render_template, session, request
from dotenv import load_dotenv
import os, json

load_dotenv()
app = Flask(__name__)



# default page
@app.route('/')
@app.route('/index')
def index():	
	return render_template('search.html', title='Home')


@app.route('/search', methods=['POST'])
def search_movie():
	search_term = request.form['search_term']

	####### DEVELOPMENT PURPOSE #######
	search_result = json.load(open('./examples/search.json', 'rb'))['Search']

	####### PRODUCTION PURPOSE  #######
	
	
	return render_template('search.html', title='Home', movies_found=search_result)

@app.route('/movie/<string:movie_id>')
def movie_page(movie_id):

	####### DEVELOPMENT PURPOSE #######
	card_result = json.load(open('./examples/card.json', 'rb'))

	####### PRODUCTION PURPOSE  #######


	return render_template('card.html', title='Home', card = card_result)


if __name__ == "__main__":
	app.run()