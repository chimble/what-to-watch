from movie_libb import *
import math


def main():
    ask_input = input("do you want: 1:movie name by ID, 2:ratings by ID, 3: ratings by user? ")
    dictratings = movie_ratings()
    userratings = user_ratings()
    if ask_input == '1':
        menu_input = input("give me movie id: ")
        movie_datas = movie_data()
        print(movie_datas[menu_input].get_name(menu_input))
    elif ask_input == '2':
        decision_input = input("1: all ratings or 2: avg? (1 or 2)")
        if decision_input == '1':
            user_input = input("give me a movie ID and i'll return the ratings: ")
            i = 0
            for item in dictratings[user_input]:
                print(dictratings[user_input][i])
                i+=1
        else:
            user_input = input("give me a movie ID and i'll return the avg rating: ")
            i = 0
            sum_ratings = 0
            for item in dictratings[user_input]:
                sum_ratings += (int(dictratings[user_input][i].rating))
                i+=1
            print(sum_ratings/len(dictratings[user_input]))
    else:
        user_id_input = input("give me a user id: ")
        if userratings[user_id_input]:
            print("yes")
            print(userratings[user_id_input])
            #print(dictratings[user_id_input][0].get_rating)

        #print(.user_id)
        #print(dictratings[user_input][0].get_rating)

    #print(sum_ratings/len(dictratings[user_input]))
    #print(dictratings.get_rating(user_input))
    #print(dictratings.get_rating(user_input))
    # print(len(dictratings[user_input]))
    #print((sum(dictratings[user_input])))


main()
