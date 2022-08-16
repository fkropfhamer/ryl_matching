class Mentee:    
    """ age = 12
    gender = 'divers'
    address = Address()
    school_year = 8
    ganztagsklasse = True
    school = "Schule 1"
    languages = ['English', 'German']
    dream_job = 'Astronaut'
    after_school = "FOS" # 1 of 3
    fav_subject = ['Math'] # 1 to n
    fav_movie_genres = ["Action", "Horror", "Fantasy"] # 3x  
    fav_music_genres = ["Pop", "Rock", "Electronic"] # 3x
    fav_sports = ["Soccer", "Football", "Dancing"] # 3x
    fav_hobbies = ["Sport", "Music", "Reading"] # 3x """

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

