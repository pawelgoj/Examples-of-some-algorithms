# -----------------------------------------------------------
# Example of k-nearest neighbors algorithm implementation
# (C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


import json
from pprint import pprint


#Read users from json file
with open('users.json', 'r') as file:
    file = file.read()

users = json.loads(file)


#Create new user
new_user = {}
new_user['user'] = 'Piotr Niewiadomski'
new_user['books'] = [{ "book": "The War of the Worlds", "rating": 8, "kind": "sf"},
                    {"book": "Star Wars: Thrawn", "rating": 10, "kind": "sf"},
                    { "book": "Brave New World", "rating": 5, "kind": "sf"},
                    { "book": "The Three Musketeers by Alexandre Dumas", "rating": 6, "kind": "adventurous"}]



#this function determines list of books kinds
def get_list_of_books_kinds(users):
    book_kinds = []
 
    for user in users:
        book_list = user['books']
        for book in book_list:
            if book['kind'] in book_kinds:
                None 
            else: 
                kind = book['kind']
                book_kinds.append(kind)

    return book_kinds


def add_to_users_preferences(users, books_kinds):

    if type(users) == type([]):
        for user in users: 
            user_preferences = determinate_how_much_user_like_a_given_kind_of_book(user, books_kinds)
            user.update({'preferences': user_preferences})

    elif type(users) == type({}):
            user_preferences = determinate_how_much_user_like_a_given_kind_of_book(users, books_kinds)
            users.update({'preferences': user_preferences})

    else:
        raise Exception('Supported type list or dict!!!!')
    
    return users 


#The measure of user preferences is the ratio of books of a given kind to all user books
def determinate_how_much_user_like_a_given_kind_of_book(user, books_kinds: list):
    user_preferences = {}
    
    user_preferences ={book_kind: 0 for book_kind in books_kinds}
    books = user['books']

    number_of_books = 0 

    for book in books:
        number_of_books+=1 
        user_preferences[book['kind']] = user_preferences[book['kind']] + 1

    user_preferences = {book_kind: round(value/number_of_books, 4) for book_kind, value in user_preferences.items()}

    return user_preferences


#classification function of KNN algorithm (finds a group of users with similar preferences to new_user)
def find_k_neareartest_neighbors(new_user_with_preferences: dict, users_with_preferences: list,\
    number_of_nearest_neighbors: int, book_kinds: list):

    users = users_with_preferences.copy()
    new_user_preferences = new_user_with_preferences['preferences']
    i = 0 
    neareartest_neighbors = []

    for j in range(number_of_nearest_neighbors):
        min_distance = float('inf')
        i = 0
        for user in users:
            preferences = user['preferences']

            value = 0 

            for kind in book_kinds:
                value_1 = new_user_preferences[kind]
                value_2 = preferences[kind]

                #Euclidean distance was used in this k-NN implementation
                value += (value_1 - value_2)**2
            
            distance = value**(1/2)

            if distance < min_distance:
                min_distance = distance
                nearest_user = user
                pop = i
                       
            i+=1

        neareartest_neighbors.append(nearest_user)
        users.pop(pop)

    return neareartest_neighbors


#KNN regression, predicts what books will be liked by the new user
def get_books_proposition(nearest_neighbors, new_user, number_of_books: int):
    '''the predicted value of how much a user is interested in a given book is given by a formula:

    (number_of_occurrences/number_of_neighbors + rating_of_book/max_rating) / 2

    This model assumes that the number of appearances among neighbors and their
    aratings are equally important'''

    max_rating = 10
    books = []
    number_of_nearest_neighbors = len(nearest_neighbors)

    for user in nearest_neighbors:
        books += user['books']

    books_rating = {}

    for book in books:

        if book['book'] in books_rating:        
            books_rating[book['book']]['quantity'] = books_rating[book['book']]['quantity'] + 1 
            books_rating[book['book']]['rating'] = books_rating[book['book']]['rating'] +  book['rating']

        else:
            books_rating.update({book['book']: {'quantity': 1, 'rating': book['rating'], 'kind': book['kind']}})

    for key in books_rating:
        books_rating[key]['rating'] =  round(books_rating[key]['rating'] / books_rating[key]['quantity'], 4)
        books_rating[key]['interested_for_new_user'] = round((books_rating[key]['rating'] / max_rating + 
            books_rating[key]['quantity'] / number_of_nearest_neighbors) / 2, 4)

    max_interested_books_for_new_user = []
    
    for i in range(number_of_books):

        max_interested_for_new_user = 0 

        for key in books_rating:

            if max_interested_for_new_user < books_rating[key]['interested_for_new_user']\
                and not key in new_user['books']:
                max_interested_for_new_user = books_rating[key]['interested_for_new_user']
                book = {'name': key}
                book.update(books_rating[key])
            
        max_interested_books_for_new_user.append(book) 
        books_rating.pop(book['name'])
    
    return max_interested_books_for_new_user


books_kinds = get_list_of_books_kinds(users)

users = add_to_users_preferences(users, books_kinds)

new_user = add_to_users_preferences(new_user, books_kinds)

number_of_nearest_neighbors = 5

nearest_neighbors = find_k_neareartest_neighbors(new_user, users, number_of_nearest_neighbors, books_kinds)

max_interested_books_for_new_user = get_books_proposition(nearest_neighbors, new_user, 8)


pprint(max_interested_books_for_new_user)





