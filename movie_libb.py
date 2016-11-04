import csv

class Movie():

    def __init__(self, movie_name):
        self.movie_name = movie_name
    def __repr__(self):
        return (self.movie_name)
    def get_name(self, movie_id):
        return self.movie_name

class Rating():

    def __init__(self, **kwargs):
        self.rating = kwargs['rating']
        self.user_id = kwargs['user_id']
    def __repr__(self):
        return "{}, {}".format(self.rating, self.user_id)
    def get_rating(self, movie_id):
        return self.rating


# def movie_data():
#     with open('u.item.test.csv') as f:
#         fieldnames = ['movie_id', 'movie_name']
#         reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
#         dictionary_movie_ids = {}
#         for row in reader:
#             dictionary_movie_ids[row['movie_id']] = Movie(row['movie_name'][0:-7])
#         print(dictionary_movie_ids)
# movie_data()

def user_ratings():
    pass

def movie_ratings():
    with open('u.data.test.csv') as f:
        fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        dictionary_movie_ratings = {}
        for row in reader:
            dictionary_movie_ratings.setdefault(row['movie_id'], []).append(Rating(**row))
        print(type(dictionary_movie_ratings['1'][0]))
        print(dictionary_movie_ratings)
movie_ratings()



# if row['movie_id'] in dictionary_movie_ratings:
#     print("TYOE")
#     dictionary_movie_ratings[row['rating']].append(row['rating'])
# dictionary_movie_ratings[row['movie_id']] = Rating(row['rating'])


#abcd
