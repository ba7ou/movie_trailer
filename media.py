import webbrowser

class Video():
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration

class Movie(Video):
    """This class provides a way to store movie related information"""
    def __init__(self, title, year, duration, imdb_id, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, year, duration)
        self.imdb_id = imdb_id
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Method used to sort movies by alphabetical order
    def __lt__(self, other):
        return self.title < other.title

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


