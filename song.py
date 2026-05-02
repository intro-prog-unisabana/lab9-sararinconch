class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length

    def get_length_in_seconds(self):
        song_sec = self.length*60
        return song_sec

