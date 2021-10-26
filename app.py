from flask import Flask, request, jsonify
from functions import make_results, results_1, results_2, results_3, results_4, results_5, results_6
app = Flask(__name__)


@app.route('/movie')
def get_movie():
    title = request.args.get('title')
    title = str(title)
    results = results_1(title)
    if title:
        results_end = make_results("title", "country", "release_year", "genre", "description", data=results)
        return jsonify(results_end)
    return jsonify("Not found")


@app.route('/movie/year/<int:year1>/<int:year2>')
def get_movie_by_year(year1:int,year2:int):
    results = results_2(year1, year2)
    return jsonify(results)


@app.route('/rating/children')
def get_movie_by_rating1():
    rating = "G"
    results = results_3(rating)
    return jsonify(results)


@app.route('/rating/family')
def get_movie_by_rating2():
    rating = "PG" or "PG-13"
    results = results_3(rating)
    return jsonify(results)


@app.route('/rating/adult')
def get_movie_by_rating3():
    rating = "R" or "NC-17"
    results = results_3(rating)
    return jsonify(results)


@app.route('/movie/<genre>')
def get_movie_by_genre(genre):
    results = results_4(genre)
    return jsonify(results)



@app.route('/movie/<type>/<int:release_year>/<listed_in>')
def get_movie_by_type(type,release_year:int, listed_in):
    results = results_6(type,release_year, listed_in)
    return jsonify(results)


if __name__ == '__main__':
    app.run(port=8000)