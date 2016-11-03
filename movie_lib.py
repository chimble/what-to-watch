#movie class
#u.item has
#    movie id, movie title
#u.data has
#    user id, movie id, rating
#u.user has
#     user id, age, gender, occupation, zip
import csv


# def movie_rating_data():
#     with open('u.data.test.csv') as f:
#         reader = csv.DictReader(f, delimiter = ' ')
#         for row in reader:
#             print(row["user_id"], row["movie_id"], row["rating"], row["timestamp"])
# movie_rating_data()

def movie_data():
    with open('u.item.test.csv') as f:
        fieldnames = ['movie_id', 'movie_name']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '|')
        dict_of_movie_name_id = {}
        for row in reader:
            dict_of_movie_name_id[row['movie_id']] = row['movie_name'][0:-7]
        return(dict_of_movie_name_id)

def search_movie_by_id():
    dictdict = movie_data()
    return(dictdict[user_rating_data()])


def user_rating_data():
    with open('u.data.test.csv') as f:
        fieldnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = '\t')
        user_input = input("give me movie ID:")
        i=0
        sum_rating = 0
        for row in reader:
            if row['movie_id'] == user_input:
                i+=1
                print(row['rating'])
                sum_rating += int(row['rating'])
        print(sum_rating/i)


user_rating_data()
class Movie():
    def __init__(self, movie_id, movie_name):
        self.movie_id = movie_id
        self.movie_name = movie_name



class User():
    def __init__(user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating


class Rating():
    def __init__(self, movie_id, rating):
        self.movie_id = movie_id
        self.rating = rating














#abcdefg
