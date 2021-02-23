# by Kami Bigdely
# Extract class

class MovieStar:
    def __init__(self, name, dob, movies, email):
        self.name = name
        self.dob = dob
        self.movies = movies
        self.email = email

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

def send_hiring_email(email):
    print("email sent to: ", email)

stars = []
    
for i, value in enumerate(emails):
    if birth_year[i] > 1985:
        stars.append(MovieStar(first_names[i] + " " + last_names[i], birth_year[i], movies[i], emails[i]))
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
        send_hiring_email(value)

print(stars[0].movies)