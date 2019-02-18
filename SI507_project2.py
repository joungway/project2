# Import statements necessary
import csv
from movies_tools import *
from flask import Flask

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    movie_count = open("movies_clean.csv", "r")
    total=0
    row_counter=csv.reader(movie_count)
    for row in row_counter:
        total+=1

    movie_count.close()
    # writer=csv.writer(csv_file, delimiter=',')
    return '<h1>{} movies recorded</h1>'.format(total)


@app.route('/movies/ratings')
def ratings():
    movies=[]
    movie_f = open("movies_clean.csv", "r")
    row_reader = csv.reader(movie_f)
    counter=0
    while counter < 6:
        movies.append(Movie(next(row_reader)))
        counter += 1
    # print(movies[0].__str__())
    movie_f.close()

    results=""
    for result in movies:
        results += result.__str__() + "<br>"

    return 'Movie Title | IMDB Rating <br>'+ results


if __name__ == '__main__':
    app.run()
