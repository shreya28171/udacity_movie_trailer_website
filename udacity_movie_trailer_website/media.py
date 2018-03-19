class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, storyline, time, stars, poster_url, trailer_url):
        """ This is documentation about the method:
            self- It is the object or instance being created
            title- The title of the movie
            storyline- A short description of what the movie is about
            time- Duration of a movie
            stars- Star cast of the movie
            poster_url- The URL address of a poster of the movie
            trailer_url- A link to show the trailer of the movie
            """
        self.title = title
        self.storyline = storyline
        self.time = time
        self.stars = stars
        self.poster_url = poster_url
        self.trailer_url = trailer_url
