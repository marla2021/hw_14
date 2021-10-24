from flask import Flask, request, jsonify
import sqlite3
from functions import results_1, results_2, results_3, results_4, results_5, results_6
app = Flask(__name__)


@app.route('/movie')
def get_movie():
    title = request.args.get('title')
    if title:
        result = results_1(title)
        result_ending =[]
        result_end = {}
        result_end["title"] = result[0][0]
        result_end["country"] = result[0][1]
        result_end["release_year"] = result[0][2]
        result_end["genre"] = result[0][3]
        result_end["description"] = result[0][4]
        result_ending.append(result_end)
        return jsonify(result_ending)


@app.route('/movie/year/<int:year1>/<int:year2>')
def get_movie_by_year(year1:int,year2:int):
    result = results_2(year1, year2)
    result_2_ending =[]
    i = 0
    for movie in result:
        result_2_end = {}
        result_2_end["title"] = result[i][0]
        result_2_end["release_year"] = result[i][1]
        result_2_ending.append(result_2_end)
        i+=1
    return jsonify(result_2_ending)


@app.route('/rating/children')
def get_movie_by_rating1():
    rating = "G"
    result = results_3(rating)
    result_3_ending = []
    i = 0
    for movie in result:
        result_3_end = {}
        result_3_end["title"] = result[i][0]
        result_3_end["rating"] = result[i][1]
        result_3_end["description"] = result[i][2]
        result_3_ending.append(result_3_end)
        i += 1
    return jsonify(result_3_ending)


@app.route('/rating/family')
def get_movie_by_rating2():
    rating = "PG" or "PG-13"
    result = results_3(rating)
    result_3_ending = []
    i = 0
    for movie in result:
        result_3_end = {}
        result_3_end["title"] = result[i][0]
        result_3_end["rating"] = result[i][1]
        result_3_end["description"] = result[i][2]
        result_3_ending.append(result_3_end)
        i += 1
    return jsonify(result_3_ending)


@app.route('/rating/adult')
def get_movie_by_rating3():
    rating = "R" or "NC-17"
    result = results_3(rating)
    result_3_ending = []
    i = 0
    for movie in result:
        result_3_end = {}
        result_3_end["title"] = result[i][0]
        result_3_end["rating"] = result[i][1]
        result_3_end["description"] = result[i][2]
        result_3_ending.append(result_3_end)
        i += 1
    return jsonify(result_3_ending)


@app.route('/movie/<genre>')
def get_movie_by_genre(genre):
    result = results_4(genre)
    result_4_ending = []
    i = 0
    for movie in result:
        result_4_end = {}
        result_4_end["title"] = result[i][0]
        result_4_end["description"] = result[i][1]
        result_4_ending.append(result_4_end)
        i += 1
    return jsonify(result_4_ending)


@app.route('/cast/<cast1>/<cast2>')
def get_movie_by_casts(cast1,cast2):
    results = results_5()
    cast_list =[]
    for result in results:
        for i in result:
            i = i.replace(" ", "")
            if cast1 and cast2 in i:
                cast_list.append(i)
                print(cast_list)
                return jsonify(cast_list)


@app.route('/movie/<type>/<int:release_year>/<listed_in>')
def get_movie_by_type(type,release_year:int, listed_in):
    results = results_6(type,release_year, listed_in)
    i=0
    result_6_ending = []
    for movie in results:
        result_6_end = {}
        result_6_end["title"] = results[i][0]
        result_6_end["description"] = results[i][1]
        result_6_ending.append(result_6_end)
        i += 1
    return jsonify(result_6_ending)


if __name__ == '__main__':
    app.run()