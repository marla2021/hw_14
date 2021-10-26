import sqlite3

def make_results(*fields, data):
    results = []
    for line in data:
        results_line = {}
        for i, fields in enumerate(fields):
            results_line[fields]=line[i]
        results.append(results_line)
    return results


def results_1(title):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, country, release_year, listed_in, description"\
                   f" FROM netflix "\
                   f" WHERE lower(title) LIKE '%{title.lower()}%' "\
                   f" ORDER BY release_year DESC LIMIT 1"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    cur.close()
    con.close()
    return result


def results_2(year1, year2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, release_year"\
                   f" FROM netflix "\
                   f" WHERE release_year BETWEEN {year1} and {year2} "\
                   f" LIMIT 100"
    cur.execute(sqlite_query)
    result = cur.fetchall()
    result_2_ending = []
    for a, b in result:
        result_2_ending.append({
            "title": a,
            "release_year": b,
        })
    cur.close()
    con.close()
    return result_2_ending


def results_3(rating):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, rating, description"\
                   f" FROM netflix "\
                   f" WHERE rating = '{rating}'"\
                   f" LIMIT 10"
    cur.execute(sqlite_query)
    result = cur.fetchall()
    result_3_ending = []
    for a, b, c in result:
        result_3_ending.append({
            "title": a,
            "release_year": b,
            "description": c,
        })
    cur.close()
    con.close()
    return result_3_ending


def results_4(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, description"\
                   f" FROM netflix "\
                   f" WHERE listed_in LIKE '%{genre}%' "\
                   f" ORDER BY release_year DESC LIMIT 10"
    cur.execute(sqlite_query)
    result = cur.fetchall()
    result_4_ending = []
    for a, c in result:
        result_4_ending.append({
            "title": a,
            "description": c,
        })
    cur.close()
    con.close()
    return result_4_ending


def results_5(cast1,cast2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT \"cast\" FROM netflix WHERE \"cast\" LIKE '%{cast1}%' AND \"cast\" LIKE '%{cast2}%'"
    cur.execute(sqlite_query)
    result = cur.fetchall()
    print(result)
    result_set = set()
    for casts in result:
        if casts:
            data = set(casts[0].split(', '))
            data.remove(cast1)
            data.remove(cast2)
            result_set.update(data)
    cur.close()
    con.close()
    return sorted(result_set)

def results_6(type,release_year, listed_in):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, description "\
                   f" FROM netflix "\
                   f" WHERE type LIKE '%{type}%' AND release_year ='{release_year}' "\
                   f" AND listed_in LIKE '%{listed_in}%'"\
                   f" LIMIT 10"
    cur.execute(sqlite_query)
    result = cur.fetchall()
    result_6_ending = []
    for a, c in result:
        result_6_ending.append({
            "title": a,
            "description": c,
        })
    cur.close()
    con.close()
    return result_6_ending