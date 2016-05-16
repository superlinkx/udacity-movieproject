# Define a class "Movie" that will be used to store a Movie datastructure with
# the Title, Poster URL, and Youtube Trailer URL
class Movie():
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 release_year):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year
