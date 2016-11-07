import csv

class Movie():

    def __init__(self, movie_name):
        self.movie_name = movie_name
    def __repr__(self):
        return (self.movie_name)
    def get_name(self, movie_id):
        return self.movie_name

class Rating:

    def __init__(self, user_id, movie_id, rating,  **kwargs):
        self.rating = rating
        self.user_id = user_id
        self.movie_id = movie_id
    def __repr__(self):
        return self.rating
        #return "{}, {}".format(self.rating, self.user_id)
    def get_rating(self, movie_id):
        return self.rating
    def get_avg(self, movie_id):
        pass
    def get_user_ratings(self, user_id):
        return self.rating


class User():

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.occupation = kwargs['occupation']
        self.zipcode = kwargs['zipcode']
    def __repr__(self):
        return self.user_id

class AvgRating():

    def __init__(self, **kwargs):
        self.movie_id = kwargs['movie_id']
        self.rating = kwargs['rating']

    def __repr__(self):
        return self.rating


def movie_data():
    with open('u.item.csv') as f:
        fieldnames = ['movie_id', 'movie_name']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        dictionary_movie_ids = {}
        for row in reader:
            dictionary_movie_ids[row['movie_id']] = Movie(row['movie_name'][0:-7])
        return(dictionary_movie_ids)
movie_data()

def user_data():
    with open('u.user.test.csv') as f:
        fieldnames = ['user_id', 'age', 'gender', 'occupation', 'zipcode']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        dictionary_user_data = {}
        for row in reader:
            dictionary_user_data.setdefault(row['user_id'], []).append(User(**row))
        #print(dictionary_user_data)
user_data()


def movie_ratings():
    with open('u.data.csv') as f:
        fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        dictionary_movie_ratings = {}
        for row in reader:
            dictionary_movie_ratings.setdefault(row['movie_id'], []).append(Rating(**row))
        #print(type(dictionary_movie_ratings['1'][0]))
        return(dictionary_movie_ratings)
        #print(dictionary_movie_ratings['1'])
movie_ratings()

def user_ratings():
    with open('u.data.csv') as f:
        fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        dictionary_user_ratings = {}
        for row in reader:
            dictionary_user_ratings.setdefault(row['user_id'], []).append(Rating(**row))
        #print(type(dictionary_movie_ratings['1'][0]))
        return(dictionary_user_ratings)
user_ratings()

def ranked_movie():
    with open('u.data.csv') as f:
        fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        dictionary_ranked_movies = {}
        dictionary_ranked_top = {}
        i = 0
        for row in reader:
            dictionary_ranked_movies.setdefault(row['movie_id'], []).append(Rating(**row))
        for k in dictionary_ranked_movies:
            sum_ratings_all = 0
            i = 0
            for item in dictionary_ranked_movies[k]:
                sum_ratings_all += (int(dictionary_ranked_movies[k][i].rating))
                i += 1
            if i >= 300:
                dictionary_ranked_top[k] = sum_ratings_all/i

        return(sorted(dictionary_ranked_top.items(), key=lambda x: x[1], reverse=True))
                #dictionary_ranked_movies.setdefault(row['movie_id'], []).append(sum(new_list_ratings)/(len(new_list_ratings)))

        #(new_list_ratings)

        #print(dictionary_ranked_movies)


# if row['movie_id'] in dictionary_movie_ratings:
#     print("TYOE")
#     dictionary_movie_ratings[row['rating']].append(row['rating'])
# dictionary_movie_ratings[row['movie_id']] = Rating(row['rating'])


#abcd
