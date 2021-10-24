import sqlite3


def results_1(title):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, country, release_year, listed_in, description"\
                   f" FROM netflix "\
                   f" WHERE lower(title) LIKE '%{title.lower()}%' "\
                   f" ORDER BY release_year DESC LIMIT 1"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    return result


def results_2(year1, year2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, release_year"\
                   f" FROM netflix "\
                   f" WHERE release_year BETWEEN {year1} and {year2} "\
                   f" LIMIT 100"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    for line in result:
        return result


def results_3(rating):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, rating, description"\
                   f" FROM netflix "\
                   f" WHERE rating = '{rating}'"\
                   f" LIMIT 10"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    for line in result:
        return result


def results_4(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, description"\
                   f" FROM netflix "\
                   f" WHERE listed_in LIKE '%{genre}%' "\
                   f" ORDER BY release_year DESC LIMIT 10"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    return result


def results_5():
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = ''' SELECT "cast" FROM netflix'''
                   # f"AND 'cast' LIKE '%{cast2}%'"
                   # f" ORDER BY release_year DESC LIMIT 10"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    return result

def results_6(type,release_year, listed_in):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f" SELECT title, description "\
                   f" FROM netflix "\
                   f" WHERE type LIKE '%{type}%' AND release_year ='{release_year}' "\
                   f" AND listed_in LIKE '%{listed_in}%'"\
                   f" LIMIT 10"
    result = cur.execute(sqlite_query)
    result = cur.fetchall()
    return result