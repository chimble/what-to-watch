from movie_libb import *
import math


def main():
    menu_input = input("give me movie id: ")
    movie_datas = movie_data()
    print(movie_datas[menu_input])

    user_input = input("give me a movie ID and i'll return the ratings: ")
    dictratings = movie_ratings()
    #print(dictratings.get_rating('1'))
    print(dictratings[user_input])

    user_id_input = input("give me a user id: ")
    print(dictratings.values())
    if user_id_input in dictratings.values():
        print("yes")
        print(dictratings[user_input][0].get_rating)
    #print(.user_id)
    #print(dictratings[user_input][0].get_rating)
    sum_ratings = (int(dictratings[user_input][0].rating) + int(dictratings[user_input][1].rating))
    #print(sum_ratings/len(dictratings[user_input]))
    #print(dictratings.get_rating(user_input))
    #print(dictratings.get_rating(user_input))
    # print(len(dictratings[user_input]))
    #print((sum(dictratings[user_input])))


main()
