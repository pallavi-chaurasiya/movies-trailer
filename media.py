import webbrowser


class Movie():

    # poster - stores url of the poster image for the movie
    # trailer - stores url of the youtube trailer video
    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.story = story
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
