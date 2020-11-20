menu_prompt = "\n enter 'a' add movie, enter 'f' find movie  enter 's' search movie enter  'q' quit movie:      "
movies = []



def add_movies():
    title = input("enter the movie title:   ")
    director = input("the th movie director:  ")
    year = input("enter the movie year:      ")


    movies.append({
      'title': title,
       'director': director,
       'year': year
    })

def show_movies():
  for movie in movies:
      print_movie(movie)

def print_movie(movie):
    print(f"Title  : {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Relasing Year : {movie['year']}")

def find_title():
    search_title = input("enter movie title you are looking for")

    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)
user_options = {
    "a": add_movies,
    "s": show_movies,
    "f": find_title
}

def menu():
    selection = input(menu_prompt)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(menu_prompt)


menu()



