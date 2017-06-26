from media import Movie
import fresh_tomatoes

# class instances of some of the all time great movies
shawshank_redemption = Movie("Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_QL50_SY1000_CR0,0,672,1000_AL_.jpg", "https://www.youtube.com/watch?v=NmzuHjWmXOc")
dark_knight = Movie("The Dark Knight", "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_QL50_.jpg", "https://www.youtube.com/watch?v=g8evyE9TuYk")
fight_club = Movie("Fight Club", "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.", "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_.jpg", "https://www.youtube.com/watch?v=BdJKm16Co6M")
inception = Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
prestige = Movie("The Prestige", "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_QL50_.jpg", "https://www.youtube.com/watch?v=DHoXum3M9eE")
django_unchained = Movie("Django Unchained", "With the help of a German bounty hunter , a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=_iH0UBYDI4g")

# list of the movies initialised above
movies = [shawshank_redemption, dark_knight, fight_club, inception, prestige, django_unchained]

# call to a function to generate html file out of the list of the movies passed to it
fresh_tomatoes.open_movies_page(movies)
