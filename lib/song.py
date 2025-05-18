class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes when a new song is created
        Song.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the count of songs by 1"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Ensure genres list only contains unique genres"""
        # Create a new list with unique genres
        unique_genres = []
        for genre in cls.genres:
            if genre not in unique_genres:
                unique_genres.append(genre)
        cls.genres = unique_genres

    @classmethod
    def add_to_artists(cls):
        """Ensure artists list only contains unique artists"""
        # Create a new list with unique artists
        unique_artists = []
        for artist in cls.artists:
            if artist not in unique_artists:
                unique_artists.append(artist)
        cls.artists = unique_artists

    @classmethod
    def add_to_genre_count(cls):
        """Update the genre_count histogram"""
        cls.genre_count = {}
        for genre in cls.genres:
            # Count occurrences of each genre in the full genres list
            count = cls.genres.count(genre)
            cls.genre_count[genre] = count

    @classmethod
    def add_to_artist_count(cls):
        """Update the artist_count histogram"""
        cls.artist_count = {}
        for artist in cls.artists:
            # Count occurrences of each artist in the full artists list
            count = cls.artists.count(artist)
            cls.artist_count[artist] = count
