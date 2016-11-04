import csv

def movie_data():
    with open('u.item.test.csv') as f:
        fieldnames = ['movie_id', 'movie_name']
        reader = csv.reader(f, delimiter = '|')
        next(reader, None)
        # dict_of_movie_name_id = {}
        # list_of_movies = []
        ids = []
        names = []
        name_id_list = []
        for row in reader:
            # dict_of_movie_name_id[row['movie_id']] = row['movie_name'][0:-7]

            # list_of_movies.append([row['movie_id'], row['movie_name'][0:-7]])
            movie_id = row[0]
            movie_name = row[1][0:-7]
            names.append(movie_name)
            ids.append(movie_id)
            movie = Movie()
            name_id_list.append([movie_id, movie_name])
        print(ids)
        print(names)
        return(name_id_list)
        
class Movie():



    def __init__(self, **kwargs):
        self.movie_id = movie_id
        self.movie_name = movie_name


    def get_name(self, movie_id):
        #return movie name given ID
        return self.movie_name
        print(movie.get_name('1'))



movie_data()
movie.get_name('1')




# class User():
#
#     def __init__(self):
#         self.user_id = user_id
#         self.movie_id = movie_id
#         self.rating = rating
#
#
# class Rating():
#     user_id = ''
#     movie_id = ''
#     ratings = []
#
#     def __init__(self, user_id, movie_id, rating):
#         self.user_id = user_id
#         self.movie_id = movie_id
#         self.rating = rating
#
#
#     def all_ratings(self):
#         #from movie id, get all ratings for movie
#         return self.ratings
#
#
#     def avg_rating(self):
#         #divide all ratings from movie by num of ratings
#         return (sum(self.ratings)/len(ratings))
#
#     def user_ratings(self):
#         #for a user id, get list of all their ratings
#         return self.ratings















#ABCDEFG
