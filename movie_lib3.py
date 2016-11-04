import csv

class Movie():

    def __init__(self, movie_id, movie_name):
        self.movie_id = movie_id
        self.movie_name = movie_name

    def get_name(self, movie_id):
        #return movie name given ID

        return self.movie_name
    #print(movie.get_name('1'))

def movie_data():
    with open('u.item.test.csv') as f:
        fieldnames = ['movie_id', 'movie_name']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        dict_of_movie_name_id = {}
        list_of_dicts = []
        list_of_movies = []
        for row in reader:
            #movie = movie(row)
            dict_of_movie_name_id[row['movie_id']] = row['movie_name'][0:-7]
            list_of_dicts.append({'movie_id': row['movie_id'], 'movie_name': row['movie_name'][0:-7]})
            movie = Movie(row['movie_id'], row['movie_name'][0:-7])
            list_of_movies.append(movie)
        print(list_of_movies)
        print(dict_of_movie_name_id)
        print(list_of_dicts)
        # print(dict_of_movie_name_id)
movie_data()
print(movie.get_name('3'))
