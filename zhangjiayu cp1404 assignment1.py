"""
Replace the contents of this module docstring with your own details
Name: ZHANG JIAYU 13851049
Date started: 2020/12/7
GitHub URL:https://github.com/JerryCheung1005/CP1404ASSIGNMENT1
"""
import csv


def show_all(movies_lists):
    unwatch = 0
    for movie in range(len(movies_lists)):
        # print('2. Star Wars: Episode IV - A New Hope - 1977 (Action)')
        if movies_lists[movie][-1] == 'w':
            unwatch += 1
        print('{}. {} {} - {} ({})'.format(movie, '*' if movies_lists[movie][-1] == 'u' else ' ',
                                           movies_lists[movie][0] + (34 - len(movies_lists[movie][0])) * ' ',
                                           (4 - len(str(movies_lists[movie][1]))) * ' ' + str(movies_lists[movie][1]),
                                           movies_lists[movie][2]))
    print('{} movies watched, {} movies still to watch'.format(unwatch, len(movies_lists) - unwatch))

def watch_movie(movies_lists):
    nums = 0
    for record in movies_lists:
        if record[3] == 'u':
            nums += 1
    if nums > 0:
        print('Enter the number of a movie to mark as watched')
        while True:
            dybh = input('')
            try:
                dybh = int(dybh)
                if dybh < 0:
                    print('Number must be >= 0')
                else:
                    try:
                        movie_info = movies_lists[dybh]
                        if movie_info[3] == 'u':
                            print('{} from {} watched'.format(movies_lists[dybh][0], movies_lists[dybh][1]))
                            movies_lists[dybh][3] = 'w'
                        else:
                            print('You have already watched The Fugitive')
                        break
                    except:
                        print('Invalid movie number')
            except:
                print('Invalid input; enter a valid number')
    else:
        print('No more movies to watch!')

def write_movies(movies_lists):
    # title
    while True:
        title = input('Title:')
        if title == '':
            print('Input can not be blank')
        else:
            break
    # Year
    while True:
        year = input('Year:')
        if year == '':
            print('Invalid input; enter a valid number')
        else:
            try:
                year = int(year)
                if year < 0:
                    print('Number must be >= 0')
                else:
                    break
            except:
                print('Invalid input; enter a valid number')

    # Category
    while True:
        category = input('Category:')
        if category == '':
            print('Input can not be blank')
        else:
            break

    print('{} ({} from {}) added to movie list'.format(title, category, year))
    movies_lists.append([title, year, category, 'u'])
    movies_lists.sort(key=lambda x: x[1], reverse=False)

def save_movies(movies_lists):
    filecsv = open('movies.csv', 'w', newline='')
    writer = csv.writer(filecsv)
    for i in movies_lists:
        writer.writerow(i)
    filecsv.close()
    print('{} movies saved to movies.csv'.format(len(movies_lists)))
    print('Have a nice day :)')

if __name__ == '__main__':

    print('Movies To Watch 1.0 - By ZHANG JIAYU 13851049')
    movies_lists = []
    with open('movies.csv','r')as f:
        reader = csv.reader(f)
        for row in reader:
            if '\t' in row[0]:
                lists = row[0].split('\t')
            else:
                lists = row
            lists[1] = int(lists[1])
            movies_lists.append(lists)
    movies_lists.sort(key = lambda x:x[1],reverse=False)
    print('{} movies loaded'.format(len(movies_lists)))

    while True:
        print('Menu:')
        print('L - List movies')
        print('A - Add new movie')
        print('W - Watch a movie')
        print('Q - Quit')
        choice = input('')
        if choice.lower() in ['l','a','w','q']:
            if choice.lower() == 'l':
                show_all(movies_lists)
            elif choice.lower() == 'w':
                watch_movie(movies_lists)
            elif choice.lower() == 'a':
                write_movies(movies_lists)
            elif choice.lower() == 'q':
                print("Have a nice day")
                save_movies(movies_lists)
                break
        else:
            print('Invalid menu choice')