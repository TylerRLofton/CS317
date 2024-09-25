import mariadb as sql
import os

# * ################
# * Helper Functions
# * ################

def printError(e):
    print(f'Error: {e}')

def connectDB(host = 'localhost', user = 'root', password = 'root', database = 'movies'):
    db = sql.connect(host = host, user = user, password = password, database = database, autocommit=True)
    return db.cursor()


# * #############
# * Main and Menu
# * #############

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
        elif choice == 5:
            queryReleaseByTitleAndYear(cursor)
        elif choice == 6:
            addMovie(cursor)
        elif choice == 7:
            addStudios(cursor)
        elif choice == 8:
            addMovieRelease(cursor)
        elif choice == 9:
            removeMovie(cursor)
        elif choice == 10:
            removeStudio(cursor)


def menu():
    try: 
        print('What would you like to do?')
        print('1. List all movies')
        print('2. List all studios')
        print('3. List all movie releases')
        print('4. Search movies')
        print('5. Search movie release by title and year')
        print('6. Add movies')
        print('7. Add studios')
        print('8. Add movie releases')
        print('9. Remove movies')
        print('10. Remove studios')
        print('0. Exit')
        return int(input('\n> '))
    except:
        choice = -1

    if choice < 0 or choice > 10:
        print('Invalid choice. Please try again.\n')
        return menu()
    

# * ##################
# * Printing Functions
# * ##################

def printMovies(tuples):
    os.system('cls')
    tableStyle = '| {:60} | {:4} | {:30} | {:30} | {:7} |'
    print()
    print(tableStyle.format('Title', 'Year', 'Director', 'Genre', 'ESRB'))
    for t in tuples:
        print(tableStyle.format(*t))
    print()

def printStudios(tuples):
    os.system('cls')
    tableStyle = '| {:30} | {:<15} | {:60} |'
    print()
    print(tableStyle.format('Name', 'Year Founded', 'Headquarter Location'))
    for t in tuples:
        print(tableStyle.format(*t))
    print()

def printMovieReleases(tuples):
    os.system('cls')
    tableStyle = '| {:60} | {:4} | {:30} | {:12} |'
    print()
    print(tableStyle.format('Title', 'Year', 'Studio', 'Release Date'))
    for t in tuples:
        print(tableStyle.format(t[0], t[1], t[2], str(t[3])))
    print()

def printMovieByRelease(tuples):
    os.system('cls')
    tableStyle = '| {:60} | {:4} | {:30} | {:30} | {:7} | {:30} | {:12} |'
    print()
    print(tableStyle.format('Title', 'Year', 'Director', 'Genre', 'ESRB', 'Studio', 'Release Date'))
    for t in tuples:
        print(tableStyle.format(t[0], t[1], t[2], t[3], t[4], t[5], str(t[6])))
    print()


# * ###################
# * Whole Table Queries
# * ###################

def queryAllMovies(cursor):
    query = 'SELECT * FROM Movies'
    cursor.execute(query)
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies found\n')

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


# * ###########################
# * Search movies by attributes
# * ###########################   

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
    elif choice == 4:
        queryMovieGenre(cursor)
    elif choice == 5:
        queryMovieESRB(cursor)

def movieSearchSubmenu():
    try:
        print('Search movie info')
        print('Which attribute do you want to search by?')
        print('1. Title')
        print('2. Release year')
        print('3. Director')
        print('4. Genre')
        print('5. ESRB')
        print('0. Return to main menu')
        return int(input('\n> '))
    except:
        choice = -1

    if choice < 0 or choice > 5:
        print('Invalid choice. Please try again.\n')
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

def queryMovieGenre(cursor):
    genre = input('Genre of the movie? > ')
    query = 'select * from Movies where genre like ?'
    fixed_genre = f'%{genre}%'
    cursor.execute(query, (fixed_genre,))
    results = cursor.fetchall()     

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching genre: ' + genre)

def queryMovieESRB(cursor):
    esrb = input('ESRB of the movie? > ')
    query = 'SELECT * FROM Movies where esrb=?'
    cursor.execute(query, (esrb,))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovies(results)
    else:
        print('No movies matching ESRB: ' + esrb)


# * ####################################
# * Search movie release by title + year
# * ####################################

def queryReleaseByTitleAndYear(cursor):
    title = input('Title of the movie? > ')
    year = input('Year of the movie? > ')

    query = 'SELECT * FROM Movies NATURAL JOIN MovieReleases where title=? and year=?'
    cursor.execute(query, (title, year))
    results = cursor.fetchall()

    if cursor.rowcount > 0:
        printMovieByRelease(results)
    else:
        print('No movie releases matching title: {} and year: {}'.format(title, year))

# * ##########
# * Add movies
# * ##########

def addMovie(cursor):
    newTitle = input('\nMovie title?\n>')
    newYear = input('\nRelease year?\n>')

    check = queryKeyTitleAndYear(cursor, newTitle, newYear)
    if len(check) > 0:
        print('\n The movie {} ({}) '.format(newTitle, newYear) + 'already exists.')
        return;

    newDirector = input('\nDirector?\n>')
    newGenre = input('\nMovie genre?\n>')
    newESRB = input('\nESRB?\n>')

    confirm = insertMovie(cursor, newTitle, newYear, newDirector, newGenre, newESRB)

    if confirm == 1:
        print('\nNew movie added to the database')
        queryAllMovies(cursor)

def queryKeyTitleAndYear(cursor, title, year):
    query = 'SELECT * FROM Movies where title=? and year=?'
    cursor.execute(query, (title, year))
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        return results
    else:
        return ()

def insertMovie(cursor, title, year, director, genre, esrb):
    print('test')
    try: 
        query = 'INSERT INTO Movies VALUES (?,?,?,?,?);'
        cursor.execute(query, (title, year, director, genre, esrb))
        return 1
    except (sql.Error) as e:
        printError(e)
        return 0


# * ###########          
# * Add studios
# * ###########

def addStudios(cursor):
    newStudio = input('\nStudio name?\n>')
    newYear = input('\nYear founded?\n>')
    newLocation = input('\nHeadquarters location?\n>')

    check = queryKeyStudio(cursor, newStudio)
    if len(check) > 0:
        print('\n The studio {} '.format(newStudio) + 'alreayd exists.')
        return

    confirm = insertStudio(cursor, newStudio, newYear, newLocation)

    if confirm == 1:
        print('\nNew studio added to the database')
        queryAllStudios(cursor)

def queryKeyStudio(cursor, studio):
    query = 'SELECT * FROM Studio where studioName=?'
    cursor.execute(query, (studio,))
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        return results
    else:
        return ()
    
def insertStudio(cursor, name, year, location):
    try: 
        query = 'INSERT INTO Studio VALUES (?,?,?)'
        cursor.execute(query, (name, year, location))
        return 1
    except (sql.Error) as e:
        printError(e)
        return 0


# * ##################
# * Add movie releases
# * ##################

def addMovieRelease(cursor):
    newTitle = input('\nMovie title?\n>')
    newYear = input('\nRelease year?\n>')
    newStudio = input('\nStudio?\n>')
    newDate = input('\nRelease date (YYYY-MM-DD)?\n>')

    check = queryKeyMovieRelease(cursor, newTitle, newYear)
    if len(check) > 0:
        print('\n The movie {} ({}) '.format(newTitle, newYear) + 'alreayd exists.')
        return

    confirm = insertMovieRelease(cursor, newTitle, newYear, newStudio, newDate)

    if confirm == 1:
        print('\nNew movie release added to the database')
        queryMovieReleases(cursor)

def queryKeyMovieRelease(cursor, title, year):
    query = 'SELECT * FROM MovieReleases where title=? and year=?'
    cursor.execute(query, (title, year))
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        return results
    else:
        return ()
    
def insertMovieRelease(cursor, title, year, studio, date):
    try: 
        query = 'INSERT INTO MovieReleases VALUES (?,?,?,?)'
        cursor.execute(query, (title, year, studio, date))
        return 1
    except (sql.Error) as e:
        printError(e)
        return 0


# * #############
# * Remove movies
# * #############

def removeMovie(cursor):
    remTitle = input('\nTitle of movie you would like to remove?\n>')
    remYear = input('\nYear of movie you would like to remove?\n>')

    check = queryKeyTitleAndYear(cursor, remTitle, remYear)
    if len(check) <= 0:
        print('\n The movie {} ({}) '.format(remTitle, remYear) + 'does not exist in the database.')
        return
    
    try:
        query = 'DELETE FROM Movies WHERE title=? and year=?'
        cursor.execute(query, (remTitle, remYear))
        print('\nMovie {} ({}) removed from the database'.format(remTitle, remYear))
        queryAllMovies(cursor)
    except (sql.Error) as e:
        printError(e)


# * ##############
# * Remove studios
# * ##############

def removeStudio(cursor):
    remStudio = input('\nName of studio you would like to remove?\n>')

    check = queryKeyStudio(cursor, remStudio)
    if len(check) <= 0:
        print('\nThe studio {} '.format(remStudio) + 'does not exist in the database.')
        return
    
    try:
        query = 'DELETE FROM Studio WHERE studioName=?'
        cursor.execute(query, (remStudio,))
        print('\nStudio {} removed from the database'.format(remStudio))
        queryAllStudios(cursor)
    except (sql.Error) as e:
        printError(e)


if __name__ == '__main__':
    os.system('cls')
    main()