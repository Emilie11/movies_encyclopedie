from flask import Flask, render_template, session, request
from dotenv import load_dotenv
import os, json
import requests

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
	# search_result = json.load(open('./examples/search.json', 'rb'))['Search']

	####### PRODUCTION PURPOSE  #######
	api_key = os.getenv("API_KEY")
	url = 'http://www.omdbapi.com/?apikey=' + api_key + '&s=' + search_term
	search_result = requests.get(url).json()
	search_result = search_result.get('Search')


	return render_template('search.html', title='Home', movies_found=search_result)

@app.route('/movie/<string:movie_id>')
def movie_page(movie_id):

	####### DEVELOPMENT PURPOSE #######
	# card_result = json.load(open('./examples/card.json', 'rb'))

	####### PRODUCTION PURPOSE  #######
	api_key = os.getenv("API_KEY")
	url = 'http://www.omdbapi.com/?apikey=' + api_key + '&i=' + movie_id
	card_result = requests.get(url).json()

	return render_template('card.html', title='Home', card = card_result)


if __name__ == "__main__":
	app.run()