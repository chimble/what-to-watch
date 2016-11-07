from movie_libb import *
import math


def main():
    ranked_list = ranked_movie()
    #print(ranked_dict.keys())
    ask_input = input("do you want: 1:movie name by ID, 2:ratings by ID, 3: ratings by user?, 4: Top Popular Movies, 5: EXIT (1, 2, 3, 4, 5) ")
    dictratings = movie_ratings()
    userratings = user_ratings()
    movie_datas = movie_data()
    #print(ranked_list)
    if ask_input == '4':
        top_movie_list = []
        for item in ranked_list:
            top_movie_list.append(movie_datas[item[0]].get_name(item[0]))
        print(top_movie_list)
        main()
    elif ask_input == '1':
        menu_input = input("give me movie id: ")
        print(movie_datas[menu_input].get_name(menu_input))
        main()
    elif ask_input == '2':
        decision_input = input("1: all ratings or 2: avg? (1 or 2)")
        if decision_input == '1':
            user_input = input("give me a movie ID and i'll return the ratings: ")
            i = 0
            list_ratings_all = []
            for item in dictratings[user_input]:
                list_ratings_all.append(dictratings[user_input][i])
                i+=1
            print(list_ratings_all)
            main()
        else:
            user_input = input("give me a movie ID and i'll return the avg rating: ")
            i = 0
            sum_ratings = 0
            for item in dictratings[user_input]:
                sum_ratings += (int(dictratings[user_input][i].rating))
                i+=1
            print(sum_ratings/len(dictratings[user_input]))
            main()
    elif ask_input == '3':
        user_id_input = input("give me a user id: ")
        if userratings[user_id_input]:
            print(userratings[user_id_input])
        main()

    else:
        exit()

        #print(.user_id)
        #print(dictratings[user_input][0].get_rating)

    #print(sum_ratings/len(dictratings[user_input]))
    #print(dictratings.get_rating(user_input))
    #print(dictratings.get_rating(user_input))
    # print(len(dictratings[user_input]))
    #print((sum(dictratings[user_input])))


main()
