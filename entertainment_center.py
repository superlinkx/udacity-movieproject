# Define movies and open new movies page
import fresh_tomatoes
import media

# Begin Define Movies
deadpool = media.Movie("Deadpool",
"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
"https://www.youtube.com/watch?v=ONHBaC-pfsk", 2016)

captain_america = media.Movie("Captain America: Civil War",
"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
"https://www.youtube.com/watch?v=uVdV-lxRPFo", 2016)

star_wars = media.Movie("Star Wars: The Force Awakens",
"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
"https://www.youtube.com/watch?v=sGbxmsDFVnE", 2015)

independence_day = media.Movie("Independence Day",
"https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
"https://www.youtube.com/watch?v=mGeIsCLOI-U", 1996)

lazer_team = media.Movie("Lazer Team",
"https://upload.wikimedia.org/wikipedia/en/6/69/Theatrical_poster_of_Lazer_Team.jpg",
"https://www.youtube.com/watch?v=TI455Z37o30", 2016)
# End Define Movies

# Open the movies page with defined movies
# Creating list and passing on single line since we don't reuse the list
fresh_tomatoes.open_movies_page([deadpool, captain_america, star_wars, independence_day,
lazer_team])
