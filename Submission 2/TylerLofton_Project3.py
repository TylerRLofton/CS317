import mariadb as sql
import os

def connectDB(host = 'localhost', user = 'root', password = 'root', database = 'movies'):
    db = sql.connect(host = host, user = user, password = password, database = database)
    return db.cursor()

def main():
    cursor = connectDB()

    while ((choice := menu()) != 0):
        if choice == 1:
            queryAllMovies(cursor)
        elif choice == 2:
            queryAllStudios(cursor)
        elif choice == 3:
            queryMovieReleases(cursor)
        elif choice == 4:
            movieSearch(cursor)

def menu():
    try: 
        print("What would you like to do?")
        print("1. List all movies")
        print("2. List all studios")
        # print("3. List all movie releases")
        print('4. Search movies')
        print("0. Exit")
        return int(input("\n> "))
    except:
        choice = -1

    if choice < 0 or choice > 4:
        print("Invalid choice. Please try again.\n")
        return menu()
    
# Printing

def printMovies(tuples):
    tableStyle = '| {:60} | {:4} | {:30} | {:30} | {:10} |'
    print()
    print(tableStyle.format('Title', 'Year', 'Director', 'Genre', 'ESRB'))
    for t in tuples:
        print(tableStyle.format(*t))
    print()

def printStudios(tuples):
    ## how to fix this table style so everything is left alligned
    
    tableStyle = '| {:30} | {:15} | {:60} |'
    print()
    print(tableStyle.format('Name', 'Year Founded', 'Headquarter Location'))
    for t in tuples:
        print(tableStyle.format(*t))
    print()

def printMovieReleases(tuples):
    #FIXME: Fix tablestyle so it doesnt print 15    
    tableStyle = '| {:60} | {:4} | {:30} | {:15} |'
    print(tableStyle.format('Title', 'Year', 'Studio', 'Release Date'))
    for t in tuples:
        print(tableStyle.format(*t))
    print()

# Whole table queries

def queryAllMovies(cursor):
    query = 'SELECT * FROM Movies'
    cursor.execute(query)
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print("No movies found\n")

def queryAllStudios(cursor):
    query = 'SELECT * FROM Studio'
    cursor.execute(query)
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printStudios(results)
    else:
        print('No studios found\n')

def queryMovieReleases(cursor):
    query = 'SELECT * FROM MovieReleases'
    cursor.execute(query)
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovieReleases(results)
    else:
        print('No movie releases\n')


# Search movies by attributes
        
def movieSearch(cursor):
    choice = movieSearchSubmenu()

    if choice == 0:
        return
    elif choice == 1:
        queryMovieTitle(cursor)
    elif choice == 2:
        queryMovieYear(cursor)
    elif choice == 3:
        queryMovieDirector(cursor)
    # elif choice == 4:
    #     queryMovieGenre(cursor)
    elif choice == 5:
        queryMovieESRB(cursor)

def movieSearchSubmenu():
    try:
        print('Search movie info')
        print('Which attribute do you want to search by?')
        print('1. Title')
        print('2. Release year')
        print('3. Director')
        # print('4. Genre')
        print('5. ESRB')
        print('0. Return to main menu')
        return int(input('\n> '))
    except:
        choice = -1

    if choice < 0 or choice > 5:
        print("Invalid choice. Please try again.\n")
        return menu()
    
def queryMovieTitle(cursor):
    title = input('Title of the movie? > ')
    query = 'SELECT * FROM Movies where title =?'
    cursor.execute(query, (title,))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching title: ' + title)

def queryMovieYear(cursor):
    year = input('Year of the movies release? > ')
    query = 'SELECT * FROM Movies where year =?'
    cursor.execute(query, (year,))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching year: ' + year)

def queryMovieDirector(cursor):
    director = input('Director of the movie? > ')
    query = 'SELECT * FROM Movies where director =?'
    cursor.execute(query, (director,))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching director: ' + director)

# def queryMovieGenre(cursor):
#     genre = input('Genre of the movie? > ')
        #FIXME: Fix this query
#     query = "select * from Movies where genre like '%' || ? || '%'"
#     cursor.execute(query, (genre,))
#     results = cursor.fetchall()

#     if cursor.rowcount > 0:
#         printMovies(results)
#     else:
#         print('No movies matching genre: ' + genre)

def queryMovieESRB(cursor):
    esrb = input('ESRB of the movie? > ')
    query = 'SELECT * FROM Movies where esrb=?'
    cursor.execute(query, (esrb,))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching ESRB: ' + esrb)

# Search movie release by title + year

# Add movies

# Add studios
        
# Add movie releases
        
# Remove movies
        
# Remove studios

# Remove movie releases

if __name__ == "__main__":
    os.system('cls')
    main()