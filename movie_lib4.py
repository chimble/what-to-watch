import csv

class Movie():

    def __init__(self, **kwargs):
        self.movie_id = movie_id
        self.movie_name = movie_name

        
def movie_data():
    with open('u.item.test.csv') as f:
        fieldnames = ['movie_id', 'movie_name']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        list_of_movie_name_id = []
        for row in reader:
            list_of_movie_name_id.append(Movie(**args))
        print(list_of_movie_name_id)

movie_data()
