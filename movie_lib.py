#movie class
#u.item has
#    movie id, movie title
#u.data has
#    user id, movie id, rating
#u.user has
#     user id, age, gender, occupation, zip

class Movie():
    def __init__(self, movie_id, movie_name):
        self.movie_id = movie_id
        self.movie_name = movie_name

    def item_import(self):
        with open('u.item.test.csv') as f:
	        reader = cvs.DictReader(f)
	    for row in reader:
		    print(row)


#user class
class User():
    def __init__(user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
    def user_import(self):
        with open('u.user.test.csv') as f:
            reader = cvs.DictReader(f)
        for row in reader:
            print(row)
    def data_import(self):
        with open('u.data.test.csv') as f:
            reader = cvs.DictReader(f)
        for row in reader:
            print(row)

#rating class


class Rating():
    def __init__(self, movie_id, rating):
        self.movie_id = movie_id
        self.rating = rating

    def data_import(self):
        with open('u.data.test.csv') as f:
	        reader = cvs.DictReader(f)
	    for row in reader:
		    print(row)
