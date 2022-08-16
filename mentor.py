from distance import create_address

class Mentor:
    """ age = 25
    gender = 'divers'
    address = Address()
    languages = ['English', 'German']
    specialization = 'Media'
    abgeschlossene_berufsausbildung = True
    abitur_zweiten_bildungsweg = False
    fav_movie_genres = ["Action", "Horror", "Fantasy"] # 3x  
    fav_music_genres = ["Pop", "Rock", "Electronic"] # 3x
    fav_sports = ["Soccer", "Football", "Dancing"] # 3x
    fav_hobbies = ["Sport", "Music", "Reading"] # 3x
    """

    def __init__(self, address, native_language, languages, movies, musics, sports, hobbies):
        self.address = address
        self.native_language = native_language
        self.languages = languages
        self.movies = movies
        self.musics = musics
        self.sports = sports
        self.hobbies = hobbies

        
    @classmethod
    def from_csv_row(cls, csv_row):
        return cls()