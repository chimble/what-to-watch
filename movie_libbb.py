from movie_libb import *
import math


def main():
    ask_input = input("do you want: 1:movie name by ID, 2:ratings by ID, 3: ratings by user? ")
    dictratings = movie_ratings()
    if ask_input == '1':
        menu_input = input("give me movie id: ")
        movie_datas = movie_data()
        print(movie_datas[menu_input].get_name(menu_input))
    elif ask_input == '2':
        decision_input = input("1: all ratings or 2: avg? (1 or 2)")
        if decision_input == '1':
            user_input = input("give me a movie ID and i'll return the ratings: ")
            #print(dictratings.get_rating('1'))
            i = 0
            for item in dictratings[user_input]:
                print(dictratings[user_input][i])
                i+=1
        else:
            user_input = input("give me a movie ID and i'll return the avg rating: ")
            i = 0
            sum_ratings = 0
            for item in dictratings[user_input]:
                #list_ratings.append(dictratings[user_input[i]])
                sum_ratings += (int(dictratings[user_input][i].rating))
                i+=1
            print(sum_ratings/len(dictratings[user_input]))
        #print(list_ratings)
    else:
        user_id_input = input("give me a user id: ")
        print(dictratings.values())
        if user_id_input in dictratings.values():
            print("yes")
            print(dictratings[user_input][0].get_rating)
        #print(.user_id)
        #print(dictratings[user_input][0].get_rating)

    #print(sum_ratings/len(dictratings[user_input]))
    #print(dictratings.get_rating(user_input))
    #print(dictratings.get_rating(user_input))
    # print(len(dictratings[user_input]))
    #print((sum(dictratings[user_input])))


main()
